import tkinter as tk
import time

def show_love():
    label.config(text="I Love You, Kukuu! 💖🥰", fg="red")
    btn.config(state="disabled")  # Disable button after clicking
    animate_hearts()

def animate_hearts():
    hearts = ["💙", "💖", "💕", "💜", "💘"]
    
    for i in range(5):
        heart_label.config(text=hearts[i % len(hearts)])  # Cycle through hearts
        root.update()
        time.sleep(0.5)

# Create window
root = tk.Tk()
root.title("A Special Message for Kukuu")
root.geometry("400x300")
root.configure(bg="skyblue")  # Kukuu's favorite color

# Label for message
label = tk.Label(root, text="Click the button for a surprise, Kukuu! 💙", font=("Arial", 14), bg="skyblue")
label.pack(pady=30)

# Heart animation label
heart_label = tk.Label(root, text="💙", font=("Arial", 40), bg="skyblue")
heart_label.pack()

# Button
btn = tk.Button(root, text="Click Me! 💕", command=show_love, font=("Arial", 14), bg="white", fg="black")
btn.pack(pady=20)

# Run app
root.mainloop()
