import tkinter as tk
from tkinter import messagebox
import webbrowser
import pyautogui
import time

MAX_BOTS = 10  # maximum allowed bots

def start_cheesy_puffs():
    try:
        game_id = game_id_entry.get()
        num_bots = int(num_bots_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Number of bots must be an integer")
        return

    if num_bots > MAX_BOTS:
        messagebox.showwarning("Warning", f"Number of bots cannot exceed {MAX_BOTS}")
        return  # refuse to continue

    page_load_wait = 5
    tab_delay = 0.5

    messagebox.showinfo("Info", "Make sure Chrome is focused. You have 5 seconds...")
    time.sleep(5)

    for idx in range(1, num_bots + 1):
        webbrowser.open_new_tab("https://play.blooket.com/")
        time.sleep(page_load_wait)

        pyautogui.typewrite(game_id)
        pyautogui.press('enter')
        time.sleep(2)

        pyautogui.typewrite(f"Cheesy Puff {idx}")
        pyautogui.press('enter')
        time.sleep(tab_delay)

    messagebox.showinfo("Done", "All Cheesy Puffs entered sequentially.")

def disable_event():
    # Prevent the window from being closed via the X button
    pass

def close_app():
    root.destroy()  # Close the app via the button

# Tkinter GUI
root = tk.Tk()
root.title("Cheesy Puff Bot Maker")

# Disable resizing / fullscreen
root.resizable(False, False)
root.geometry("300x180")

# Disable the close button (X)
root.protocol("WM_DELETE_WINDOW", disable_event)

tk.Label(root, text="Game ID:").grid(row=0, column=0, padx=5, pady=5)
game_id_entry = tk.Entry(root)
game_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text=f"Number of Bots (max {MAX_BOTS}):").grid(row=1, column=0, padx=5, pady=5)
num_bots_entry = tk.Entry(root)
num_bots_entry.grid(row=1, column=1, padx=5, pady=5)

start_button = tk.Button(root, text="Start Cheesy Puffs", command=start_cheesy_puffs)
start_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Add Close button
close_button = tk.Button(root, text="Close", command=close_app, bg="red", fg="white")
close_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
