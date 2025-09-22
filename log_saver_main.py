import customtkinter as ctk
import tkinter as tk
import os

###############################################################################

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

###############################################################################

app = ctk.CTk()
app.title("Logs Viewer")
app.geometry("1200x800")

###############################################################################

label = ctk.CTkLabel(app, text="LOMFL - Log Viewer", font=("Arial", 20, "bold"))
label.pack(pady=10)

###############################################################################

logs_file = "logs.txt"
logs = []

###############################################################################

if os.path.exists(logs_file):
    with open(logs_file, "r", encoding="utf-8") as f:
        logs = [line.strip() for line in f.readlines()]

###############################################################################

frame = ctk.CTkFrame(app)
frame.pack(pady=10, padx=10, fill="both", expand=True)

textbox = tk.Text(frame, width=80, height=25, wrap="word")
textbox.configure(bg="#302e2e")
textbox.configure(font=("Arial", 15, "bold"))
textbox.pack(fill="both", expand=True)

###############################################################################

textbox.tag_config("INFO", foreground="yellow")
textbox.tag_config("PROCESS", foreground="orange")
textbox.tag_config("ERROR", foreground="red")

###############################################################################

def add_log_to_textbox(log):
    textbox.configure(state="normal")
    if log.startswith("[INFO]"):
        tag = "INFO"
    elif log.startswith("[PROCESS]"):
        tag = "PROCESS"
    elif log.startswith("[ERROR]"):
        tag = "ERROR"
    else:
        tag = ""
    textbox.insert("end", "\n" + log, tag)
    textbox.see("end")
    textbox.configure(state="disabled")

###############################################################################

for log in logs:
    add_log_to_textbox(log)

###############################################################################

def save_logs_to_file():
    with open(logs_file, "w", encoding="utf-8") as f:
        for log in logs:
            f.write(log + "\n")

###############################################################################

entry = ctk.CTkEntry(app, placeholder_text="Wpisz nowy log...")
entry.pack(pady=5, padx=10, fill="x")

def add_log_from_entry():
    log_text = entry.get().strip()
    if log_text:
        logs.append(log_text)           
        add_log_to_textbox(log_text)    
        save_logs_to_file()             
        entry.delete(0, "end")

button_add = ctk.CTkButton(app, text="Dodaj log", command=add_log_from_entry)
button_add.pack(pady=5, padx=10)

###############################################################################

def clear_logs():
    logs.clear()
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.configure(state="disabled")
    save_logs_to_file()

button_clear = ctk.CTkButton(app, text="Wyczyść logi", command=clear_logs)
button_clear.pack(pady=5, padx=10)

app.mainloop()
