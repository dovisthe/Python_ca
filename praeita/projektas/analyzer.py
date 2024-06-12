import tkinter as tk
from tkinter import messagebox, ttk

def update_progress(progress, step_label, steps, index, number, steps_window):
    if index < len(steps):
        step_label.config(text=steps[index])
        step_value = (index + 1) * (100 / len(steps))
        
        for value in range(int(progress['value']), int(step_value)):
            progress['value'] = value
            steps_window.update()
            root.after(10)
        
        root.after(1000, update_progress, progress, step_label, steps, index + 1, number, steps_window)
    else:
        messagebox.showinfo("Result", f"Tavo numeris kuri pasirinkai buvo: {number}")
        steps_window.destroy()

def show_steps(number):
    steps_window = tk.Toplevel(root)
    steps_window.title("Processing Steps")

    progress = ttk.Progressbar(steps_window, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=20)

    step_label = tk.Label(steps_window, text="")
    step_label.pack(pady=10)

    steps = ["Reading brainwaves...", "Analyzing memories...", "Decoding thoughts..."]
    root.after(1000, update_progress, progress, step_label, steps, 0, number, steps_window)

def on_submit():
    try:
        number = int(entry.get())
        if number < 1 or number > 10:
            raise ValueError("The number must be between 1 and 10.")
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))
        return

    show_steps(number)

# Set up the main window
root = tk.Tk()
root.title("Numerio spejikas")

tk.Label(root, text="Iveskite numeri nuo 1 iki 10, as bandysiu atspeti ").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()