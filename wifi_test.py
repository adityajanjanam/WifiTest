import tkinter as tk
from tkinter import ttk
import subprocess

def get_wifi_details():
    result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    return "Failed to retrieve WiFi details."

def update_details():
    details = get_wifi_details()
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, details)

# Create the GUI
app = tk.Tk()
app.title("WiFi Performance Monitor")
app.geometry("600x400")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

text_box = tk.Text(frame, wrap="word", height=20, width=70)
text_box.grid(row=0, column=0)

refresh_button = ttk.Button(frame, text="Refresh", command=update_details)
refresh_button.grid(row=1, column=0, pady=10)

# Initial load
update_details()

app.mainloop()
