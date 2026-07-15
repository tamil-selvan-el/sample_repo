import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Python UI App")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")
        
        # Title Label
        title_label = tk.Label(
            root,
            text="Welcome to My App",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=20)
        
        # Input Frame
        input_frame = tk.Frame(root, bg="#f0f0f0")
        input_frame.pack(pady=10)
        
        label = tk.Label(
            input_frame,
            text="Enter your name:",
            font=("Arial", 12),
            bg="#f0f0f0"
        )
        label.pack(side=tk.LEFT, padx=5)
        
        self.entry = tk.Entry(input_frame, width=20, font=("Arial", 11))
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.bind("<Return>", lambda e: self.on_greet())
        
        # Button Frame
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=15)
        
        greet_btn = tk.Button(
            button_frame,
            text="Greet",
            command=self.on_greet,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=8
        )
        greet_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame,
            text="Clear",
            command=self.on_clear,
            bg="#2196F3",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=8
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Output Label
        self.output_label = tk.Label(
            root,
            text="",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#1976D2",
            wraplength=350
        )
        self.output_label.pack(pady=20)
        
        # Counter Section
        counter_frame = tk.Frame(root, bg="#ffffff", relief=tk.SUNKEN, bd=1)
        counter_frame.pack(pady=15, padx=20, fill=tk.X)
        
        counter_label = tk.Label(
            counter_frame,
            text="Click Counter:",
            font=("Arial", 10),
            bg="#ffffff"
        )
        counter_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.counter_display = tk.Label(
            counter_frame,
            text="0",
            font=("Arial", 12, "bold"),
            bg="#ffffff",
            fg="#FF5722"
        )
        self.counter_display.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.click_count = 0
    
    def on_greet(self):
        name = self.entry.get().strip()
        if name:
            greeting = f"Hello, {name}! 👋"
            self.output_label.config(text=greeting)
            self.click_count += 1
            self.counter_display.config(text=str(self.click_count))
        else:
            messagebox.showwarning("Input Error", "Please enter your name!")
    
    def on_clear(self):
        self.entry.delete(0, tk.END)
        self.output_label.config(text="")
        self.click_count = 0
        self.counter_display.config(text="0")
        self.entry.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()
