# ✨ Python Code Autotyper

Auto-type code into CodeTantra with customizable delays and random patterns. Features pause, resume, and stop controls. Perfect for timed coding challenges and online judges. Choose your hotkey and boost your productivity!

---

## 🚀 Features

- **Auto-type code** directly into any editor (CodeTantra, online judges, etc.)
- **Customizable delays** - control character and line delays
- **Human-like typing** - optional random delay variation
- **Multiple hotkeys** - Start with Right Ctrl, Esc, or Right Shift
- **Pause/Resume** - Left Shift to pause, Right Shift to resume
- **Emergency Stop** - Red STOP button for instant termination
- **Vibrant UI** - Neon cyberpunk-themed interface

---

## 📋 Requirements

```
Python 3.x
pyautogui
keyboard
tkinter (usually included with Python)
```

## 🔧 Installation

```bash
pip install pyautogui keyboard
```

---

## 🎮 How to Use

1. **Paste your code** in the text editor
2. **Adjust timing settings** (character and line delays)
3. **Select your hotkey** (Right Ctrl, Esc, or Right Shift)
4. **Click START** or press your chosen hotkey
5. **Click inside CodeTantra editor** within 5 seconds
6. **Watch your code auto-type!**

### Controls

| Action | Shortcut |
|--------|----------|
| Start Typing | Right Ctrl / Esc / Right Shift (configurable) |
| Pause | Left Shift |
| Resume | Right Shift |
| Stop | STOP button |

---

## ⚙️ Settings

- **Char Delay (sec):** Delay between typing individual characters (default: 0.02)
- **Line Delay (sec):** Delay between lines (default: 0.25)
- **Human-like random delay:** Adds random variation (0-0.03s) per character

---

## 🚨 Important Notes

- ⚠️ **Do NOT change focus** while typing is in progress
- ⚠️ **Allow 5 seconds** after pressing START to click the target editor
- ✅ Tested with CodeTantra, but works with any text input field
- ✅ Emergency stop available anytime with STOP button

---

## 📝 Files

- `autotyper.py` - Main application
- `test.cpp` & `test_newline.cpp` - Sample test files

---

## 🎨 UI Theme

- **Background:** Dark navy (`#1a1a2e`)
- **Accent Colors:** Cyan, lime green, gold, hot pink
- **Text:** Neon green on dark blue
- **Buttons:** Color-coded for easy identification

---

## 💡 Tips

- Use shorter character delays for simpler code
- Increase delays if experiencing typing errors
- Test with a small snippet first
- Keep the editor window accessible at all times

---

**Made with ❤️ for CodeTantra and online judge enthusiasts!**
