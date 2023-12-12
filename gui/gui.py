
import tkinter as tk
from tkinter import messagebox
from optiwrite_ai import OptiWriteAI

class OptiWriteGUI:
    def __init__(self):
        self.optiwrite_ai = OptiWriteAI()

        self.window = tk.Tk()
        self.window.title("OptiWrite AI")
        self.window.geometry("800x600")
        self.window.configure(bg="#f2f2f2")

        self.title_label = tk.Label(self.window, text="OptiWrite AI", font=("Helvetica", 24), bg="#f2f2f2")
        self.title_label.pack(pady=20)

        self.text_label = tk.Label(self.window, text="Enter your text:", font=("Helvetica", 14), bg="#f2f2f2")
        self.text_label.pack()

        self.text_entry = tk.Text(self.window, height=10, width=60, font=("Helvetica", 12))
        self.text_entry.pack(pady=10)

        self.optimize_button = tk.Button(self.window, text="Optimize", command=self.optimize_text, font=("Helvetica", 14), bg="#4CAF50", fg="white", relief="flat")
        self.optimize_button.pack(pady=10)

    def optimize_text(self):
        input_text = self.text_entry.get("1.0", tk.END).strip()
        if input_text:
            optimized_text = self.optiwrite_ai.optimize_text(input_text)
            messagebox.showinfo("Optimized Text", optimized_text)
        else:
            messagebox.showwarning("Empty Text", "Please enter some text.")

if __name__ == "__main__":
    optiwrite_gui = OptiWriteGUI()
    optiwrite_gui.window.mainloop()

