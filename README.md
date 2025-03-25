# 🎵 Python Metronome App (Tkinter + Pygame)

A visually engaging and fully interactive metronome built with **Tkinter** for GUI and **Pygame** for sound playback. Designed for musicians who want intuitive tempo control, time signature flexibility, and responsive tap tempo.

---

## 🚀 Features

- 🎚️ **Tempo Control**: Adjustable from 30 to 230 BPM via slider or arrow keys.
- 🔁 **Time Signatures**: Select from common and compound meters, or choose custom.
- 🖱️ **Tap Tempo**: Press `T` to estimate tempo by tapping.
- 🎧 **Audio Feedback**: 
  - Strong beat
  - Weak beat
  - Subdivision for compound meters
- ⏱️ **Real-time Beat Counter**: Visual cue of current beat in the measure.
- 🎼 **Musical Markings**: Displays tempo markings (e.g., Allegro, Adagio) based on BPM.
- ⌨️ **Keyboard Shortcuts**:
  - `Spacebar`: Start/Stop
  - `T`: Tap tempo
  - `M`: Cycle time signatures
  - `Q`: Quit the app
  - Arrow Keys: Adjust tempo

---

## 📸 Screenshots

> _You can add screenshots here by uploading images and linking them like:_
```md
![Screenshot](screenshots/metronome_ui.png)
```

---

## 🛠️ Requirements

- Python 3.7+
- `pygame`
- `tkinter` (usually comes pre-installed with Python)

Install dependencies via pip:

```bash
pip install pygame
```

---

## 📁 File Structure

```
metronome/
├── metronome.py              # Main Python script
├── metronomes/
│   ├── Synth_Bell_A_hi.wav   # Strong beat
│   ├── Synth_Bell_A_lo.wav   # Weak beat
│   └── Synth_Bell_B_hi.wav   # Subdivision beat
```

---

## 🧠 How It Works

- Uses `pygame.mixer` to play beat sounds at intervals calculated from BPM and time signature.
- `tkinter.Scale` widget lets you set the tempo dynamically.
- Beat subdivision logic supports simple and compound meters.
- Tap tempo logic measures time intervals between key presses to estimate BPM.
- Keyboard event binding provides an efficient user experience for musicians.

---

## ⚙️ Run It

```bash
python metronome.py
```

Then interact with the UI, or use keyboard shortcuts to control playback.

---

## ⌨️ Keyboard Shortcuts

| Key        | Action                    |
|------------|---------------------------|
| `Space`    | Start / Stop playback     |
| `T`        | Tap to estimate tempo     |
| `M`        | Cycle through time sigs   |
| `Q`        | Quit the application      |
| `↑ ↓ ← →`  | Fine/coarse tempo control |

---

## 📝 Notes

- Make sure sound files exist in the `metronomes/` folder or update the paths.
- Tap tempo requires 2–6 taps in rhythm to estimate BPM.
- Custom time signatures (`* / 4`, `* / 2`, etc.) are placeholders and can be extended for user input.

---

## 📦 Packaging (Optional)

To package into a standalone app:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed metronome.py
```

---

## 📄 License

MIT License. Feel free to modify and use for personal or educational projects.

---

## 🎻 Made for Musicians by Musicians 🎶
