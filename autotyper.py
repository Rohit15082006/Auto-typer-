import pyautogui
import keyboard
import time
import random
import threading
import tkinter as tk
from tkinter import messagebox

# =========================================================
# ===================== DEFAULT SETTINGS ==================
# =========================================================

DEFAULT_CHAR_DELAY = 0.02
DEFAULT_LINE_DELAY = 0.25
DEFAULT_RANDOM = True
FOCUS_WAIT_SECONDS = 5

PAUSE_KEY  = 'left shift'
RESUME_KEY = 'right shift'
STOP_KEY   = 'esc'

pyautogui.FAILSAFE = False

paused = threading.Event()
paused.set()
stop_flag = threading.Event()
typing_thread = None
current_start_hotkey = None

# =========================================================
# ===================== TYPING ENGINE =====================
# =========================================================

def type_text(text, char_delay, line_delay, random_delay):
    time.sleep(FOCUS_WAIT_SECONDS)

    for line in text.splitlines():
        if stop_flag.is_set():
            return

        paused.wait()

        for char in line:
            if stop_flag.is_set():
                return

            paused.wait()
            pyautogui.write(char)

            delay = char_delay
            if random_delay:
                delay += random.uniform(0, 0.03)
            time.sleep(delay)

        pyautogui.press('enter')
        time.sleep(line_delay)

# =========================================================
# ===================== GUI ACTIONS =======================
# =========================================================

def start_typing():
    global typing_thread
    stop_flag.clear()
    paused.set()

    text = code_box.get("1.0", tk.END).rstrip()
    if not text:
        messagebox.showerror("Error", "No code to type.")
        return

    try:
        char_delay = float(char_delay_entry.get())
        line_delay = float(line_delay_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid delay values.")
        return

    random_delay = random_var.get()

    messagebox.showinfo(
        "Ready",
        f"Click inside CodeTantra editor NOW.\n"
        f"Typing starts in {FOCUS_WAIT_SECONDS} seconds.\n\n"
        f"Emergency stop: STOP button"
    )

    typing_thread = threading.Thread(
        target=type_text,
        args=(text, char_delay, line_delay, random_delay),
        daemon=True
    )
    typing_thread.start()


def pause_typing():
    paused.clear()


def resume_typing():
    paused.set()


def stop_typing():
    stop_flag.set()
    paused.set()

# =========================================================
# ================= HOTKEY MANAGEMENT =====================
# =========================================================

def update_start_hotkey():
    global current_start_hotkey

    selected = start_key_var.get()

    # Remove old hotkey
    if current_start_hotkey:
        keyboard.remove_hotkey(current_start_hotkey)

    # Map GUI choice to keyboard key
    key_map = {
        "Right Ctrl": "right ctrl",
        "Esc": "esc",
        "Right Shift": "right shift"
    }

    new_key = key_map[selected]
    keyboard.add_hotkey(new_key, start_typing)
    current_start_hotkey = new_key

# Fixed hotkeys
keyboard.add_hotkey(PAUSE_KEY, pause_typing)
keyboard.add_hotkey(RESUME_KEY, resume_typing)

# =========================================================
# ===================== GUI LAYOUT ========================
# =========================================================

root = tk.Tk()
root.title("🚀 PYTHON CODE AUTOTYPER 🚀")
root.geometry("900x700")
root.configure(bg="#1a1a2e")

# Header label
header = tk.Label(root, text="✨ PASTE YOUR CODE BELOW ✨", font=("Arial", 16, "bold"), bg="#16213e", fg="#00d4ff", pady=15)
header.pack(fill=tk.X)

code_box = tk.Text(root, wrap="none", font=("Consolas", 11), bg="#0f3460", fg="#00ff88", insertbackground="#ff006e")
code_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# ---------------- SETTINGS ----------------

settings_frame = tk.Frame(root, bg="#16213e")
settings_frame.pack(pady=10, fill=tk.X, padx=10)

tk.Label(settings_frame, text="⚡ Char Delay (sec):", font=("Arial", 10, "bold"), bg="#16213e", fg="#ffd60a").grid(row=0, column=0, padx=5)
char_delay_entry = tk.Entry(settings_frame, width=8, font=("Arial", 10), bg="#0f3460", fg="#00ff88", insertbackground="#ff006e")
char_delay_entry.insert(0, str(DEFAULT_CHAR_DELAY))
char_delay_entry.grid(row=0, column=1, padx=5)

tk.Label(settings_frame, text="⚡ Line Delay (sec):", font=("Arial", 10, "bold"), bg="#16213e", fg="#ffd60a").grid(row=0, column=2, padx=5)
line_delay_entry = tk.Entry(settings_frame, width=8, font=("Arial", 10), bg="#0f3460", fg="#00ff88", insertbackground="#ff006e")
line_delay_entry.insert(0, str(DEFAULT_LINE_DELAY))
line_delay_entry.grid(row=0, column=3, padx=5)

random_var = tk.BooleanVar(value=DEFAULT_RANDOM)
tk.Checkbutton(settings_frame, text="🎲 Human-like random delay", font=("Arial", 10, "bold"), variable=random_var, bg="#16213e", fg="#ff006e", selectcolor="#0f3460", activebackground="#16213e", activeforeground="#00d4ff")\
    .grid(row=0, column=4, padx=10)

# ---------------- HOTKEY SELECTOR ----------------

hotkey_frame = tk.LabelFrame(root, text="🎮 SHORTCUT KEY (START TYPING)", font=("Arial", 11, "bold"), bg="#16213e", fg="#00d4ff")
hotkey_frame.pack(pady=10, fill=tk.X, padx=10)

start_key_var = tk.StringVar(value="Right Ctrl")

tk.Radiobutton(hotkey_frame, text="Right Ctrl", font=("Arial", 10, "bold"),
               variable=start_key_var, value="Right Ctrl",
               command=update_start_hotkey, bg="#16213e", fg="#00ff88", selectcolor="#0f3460", activebackground="#16213e", activeforeground="#ffd60a").pack(side=tk.LEFT, padx=15)

tk.Radiobutton(hotkey_frame, text="Esc", font=("Arial", 10, "bold"),
               variable=start_key_var, value="Esc",
               command=update_start_hotkey, bg="#16213e", fg="#00ff88", selectcolor="#0f3460", activebackground="#16213e", activeforeground="#ffd60a").pack(side=tk.LEFT, padx=15)

tk.Radiobutton(hotkey_frame, text="Right Shift", font=("Arial", 10, "bold"),
               variable=start_key_var, value="Right Shift",
               command=update_start_hotkey, bg="#16213e", fg="#00ff88", selectcolor="#0f3460", activebackground="#16213e", activeforeground="#ffd60a").pack(side=tk.LEFT, padx=15)

# Initialize default hotkey
update_start_hotkey()

# ---------------- BUTTONS ----------------

buttons = tk.Frame(root, bg="#1a1a2e")
buttons.pack(pady=12)

tk.Button(buttons, text="▶ START", width=12, font=("Arial", 11, "bold"), bg="#00ff88", fg="#1a1a2e",
          command=start_typing, activebackground="#00d4ff", activeforeground="#1a1a2e").grid(row=0, column=0, padx=5)

tk.Button(buttons, text="⏸ PAUSE", width=12, font=("Arial", 11, "bold"), bg="#ffd60a", fg="#1a1a2e",
          command=pause_typing, activebackground="#ffb400", activeforeground="#1a1a2e").grid(row=0, column=1, padx=5)

tk.Button(buttons, text="▶ RESUME", width=12, font=("Arial", 11, "bold"), bg="#00d4ff", fg="#1a1a2e",
          command=resume_typing, activebackground="#00b8d4", activeforeground="#1a1a2e").grid(row=0, column=2, padx=5)

tk.Button(buttons, text="⛔ STOP", width=12, font=("Arial", 11, "bold"), bg="#ff006e", fg="white",
          command=stop_typing, activebackground="#cc0055", activeforeground="white").grid(row=0, column=3, padx=5)

# ---------------- INFO ----------------

info = tk.Label(
    root,
    text=(
        "📋 HOW TO USE:\n"
        "① Paste code in the editor  |  ② Select START shortcut key  |  ③ Press START  |  ④ Click CodeTantra editor\n"
        "⚠️  DO NOT change focus while typing!  |  🎯 Emergency: Press STOP button\n\n"
        "🎹 Shortcuts: Pause [Left Shift] | Resume [Right Shift]"
    ),
    font=("Arial", 9, "bold"),
    fg="#00ff88",
    bg="#0f3460",
    pady=10
)
info.pack(pady=8, fill=tk.X, padx=10)

root.mainloop()
