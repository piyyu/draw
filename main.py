import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing Tool")

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.drawing = False
        self.x = 0
        self.y = 0
        self.eraser_mode = False

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw_or_erase)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack()

        self.eraser_button = tk.Button(self.root, text="Eraser", command=self.toggle_eraser)
        self.eraser_button.pack()

    def start_drawing(self, event):
        self.drawing = True
        self.x = event.x
        self.y = event.y

    def draw_or_erase(self, event):
        if self.drawing:
            if self.eraser_mode:
                self.erase(event)
            else:
                self.canvas.create_line(self.x, self.y, event.x, event.y, width=2)
            self.x = event.x
            self.y = event.y

    def stop_drawing(self, event):
        self.drawing = False

    def clear_canvas(self):
        self.canvas.delete("all")

    def toggle_eraser(self):
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.eraser_button.config(text="Draw")
        else:
            self.eraser_button.config(text="Eraser")

    def erase(self, event):
        self.canvas.create_rectangle(event.x - 10, event.y - 10, event.x + 10, event.y + 10, fill="white", outline="white")


root = tk.Tk()
app = DrawingApp(root)

root.mainloop()
