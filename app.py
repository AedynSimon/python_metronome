import time
import tkinter as tk
from tkinter import Frame
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load metronome sounds
strong_beat = pygame.mixer.Sound('metronomes/Synth_Bell_A_hi.wav')
weak_beat = pygame.mixer.Sound('metronomes/Synth_Bell_A_lo.wav')
sub_strong_beat = pygame.mixer.Sound('metronomes/Synth_Bell_B_hi.wav')

# Theme and defaults
theme_colors = {'bg': '#52767D', 'text': '#FFFFE6',
                'label_bg': '#3D998D', 'scale_through': '#A3CEC5'}
theme_fonts = ['Helvetica']
tempo_range = [30, 230]
defaults = {'tempo': 120, 'scale_length': 550}

# Main window
window = tk.Tk()
window.title('Metronome')
window.geometry('900x300')

# Frames
leftFrame = Frame(window, bg=theme_colors['bg'])
leftFrame.pack(side='left', fill='both')
midFrame = Frame(window)
midFrame.pack(side='left', fill='both')
rightFrame = Frame(window)
rightFrame.pack(side='left', fill='both', expand=1)

# Time signatures
time_signatures = {
    0: [' 2 / 4', (2, 4)], 1: [' 3 / 4', (3, 4)], 2: [' 4 / 4', (4, 4)],
    3: [' 2 / 2', (2, 2)], 4: [' 6 / 8', (6, 8)], 5: [' 9 / 8', (9, 8)],
    6: ['12/ 8', (12, 8)], 7: [' * / 4', (-1, 4)], 8: [' * / 2', (-1, 2)],
    9: [' * / 8', (-1, 8)]
}

ts_mode = tk.IntVar(leftFrame)
for mode in time_signatures.keys():
    radio_button = tk.Radiobutton(leftFrame, text=time_signatures[mode][0], variable=ts_mode,
                                  value=mode, fg=theme_colors['text'], bg=theme_colors['bg'],
                                  anchor='w', font=(theme_fonts[0], 17))
    if time_signatures[mode][-1] == (4, 4):
        radio_button.select()
    radio_button.pack(fill='x')

# Tempo label and marking
tempo_label = tk.Label(midFrame, text='120', font=(theme_fonts[0], 90, 'bold'),
                       fg=theme_colors['text'], bg=theme_colors['label_bg'], anchor='s')
tempo_label.pack(fill='both', expand=1)

marking_label = tk.Label(midFrame, text='Allegretto', font=(theme_fonts[0], 90, 'bold'),
                         fg=theme_colors['text'], bg=theme_colors['label_bg'], anchor='n')
marking_label.pack(fill='both', expand=1)

markings = {
    'Largo': [40, 60], 'Adagio': [66, 76], 'Andante': [76, 108],
    'Allegretto': [112, 120], 'Allegro': [120, 156],
    'Presto': [168, 200], 'Prestissimo': [200, 330]
}

scale_var = tk.IntVar(midFrame)


def tempo_marking_of(tempo):
    for key in markings:
        if markings[key][0] <= tempo <= markings[key][1]:
            return key
    return ''


def update(*args):
    global tempo, interval_ms
    tempo = scale_var.get()
    interval_ms = int((60 / tempo) * (4 / time_signature[-1]) * 1000)
    tempo_label['text'] = f'{tempo}'
    marking_label['text'] = tempo_marking_of(tempo)


# Tempo scale
scale = tk.Scale(midFrame, from_=tempo_range[0], to=tempo_range[1], orient=tk.HORIZONTAL,
                 length=defaults['scale_length'], showvalue=0,
                 troughcolor=theme_colors['scale_through'], bd=0,
                 activebackground=theme_colors['text'], bg=theme_colors['label_bg'],
                 sliderlength=30, font=(theme_fonts[0]),
                 variable=scale_var, command=update)
scale.set(defaults['tempo'])
scale.pack(side='bottom', fill='both', expand=0)

# Count label
count_label = tk.Label(rightFrame, text='0', fg=theme_colors['text'], bg=theme_colors['bg'],
                       width=3, font=(theme_fonts[0], 180, 'bold'), justify='left')
count_label.pack(fill='both', expand=1)


def update_time_signature(*args):
    global time_signature, count, interval_ms
    time_signature = time_signatures[ts_mode.get()][-1]
    interval_ms = int((60 / tempo) * (4 / time_signature[-1]) * 1000)
    count = 0


ts_mode.trace_add('write', update_time_signature)

# Init values
time_signature = time_signatures[ts_mode.get()][-1]
tempo = defaults['tempo']
interval_ms = int((60 / tempo) * (4 / time_signature[-1]) * 1000)
count = 0
ON = True


def play():
    global count, time_signature, count_label, ON
    try:
        if ON:
            count += 1
            count_label['text'] = str(count)
            if time_signature[0] == -1:
                strong_beat.play()
            else:
                if count == 1:
                    strong_beat.play()
                elif time_signature[-1] == 8 and count % 3 == 1:
                    sub_strong_beat.play()
                else:
                    weak_beat.play()
            if count == time_signature[0]:
                count = 0
        window.after(interval_ms, play)
    except Exception as e:
        print("Error in play():", e)
        window.destroy()


time_list = []


def tap_estimate():
    global time_list, scale
    time_list.append(time.time())
    if len(time_list) > 1:
        if time_list[-1] - time_list[-2] > 2:
            time_list = [time_list[-1]]
        else:
            N = 6
            if len(time_list) < N:
                interval = (time_list[-1] - time_list[0]
                            ) / (len(time_list) - 1)
            else:
                interval = (time_list[-1] - time_list[-N]) / (N - 1)
            tempo_est = int(60 / interval)
            scale.set(tempo_est)


def key_pressed(event):
    global ON
    if event.char == ' ':
        ON = not ON
    elif event.char == 't':
        tap_estimate()
    elif event.char == 'm':
        ts_mode.set((ts_mode.get() + 1) % len(time_signatures))
    elif event.char == 'q':
        pygame.mixer.quit()
        exit()


def arrow_down(event):
    global tempo
    if tempo - 1 >= tempo_range[0]:
        tempo -= 1
    scale.set(tempo)


def arrow_up(event):
    global tempo
    if tempo + 1 <= tempo_range[1]:
        tempo += 1
    scale.set(tempo)


def arrow_left(event):
    global tempo
    tempo = max(tempo - 10, tempo_range[0])
    scale.set(tempo)


def arrow_right(event):
    global tempo
    tempo = min(tempo + 10, tempo_range[1])
    scale.set(tempo)


# Bindings
window.bind("<Key>", key_pressed)
window.bind('<Down>', arrow_down)
window.bind('<Up>', arrow_up)
window.bind('<Left>', arrow_left)
window.bind('<Right>', arrow_right)

# Start loop
window.after(interval_ms, play)
window.mainloop()
