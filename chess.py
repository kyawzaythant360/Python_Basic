import tkinter as tk
from tkinter import messagebox
import chess
import cairosvg

from PIL import Image, ImageTk
import io

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Chess Game")
        
        self.board = chess.Board()
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        
        self.status_label = tk.Label(root, text="White to move", font=("Arial", 14))
        self.status_label.pack()
        
        self.load_board_image()
        self.canvas.bind("<Button-1>", self.on_click)
        
        self.selected_square = None
    
    def load_board_image(self):
        """Render chess board and pieces as an image in Tkinter."""
        svg_data = chess.svg.board(self.board).encode("utf-8")
        png_data = cairosvg.svg2png(bytestring=svg_data)
        image = Image.open(io.BytesIO(png_data))
        image = image.resize((400, 400), Image.ANTIALIAS)
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
    
    def on_click(self, event):
        """Handle click event for piece movement."""
        x, y = event.x, event.y
        file = x // 50
        rank = 7 - (y // 50)
        square = chess.square(file, rank)
        
        if self.selected_square is None:
            # First click: Select piece
            if self.board.piece_at(square):
                self.selected_square = square
        else:
            # Second click: Try to move piece
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.update_status()
            else:
                messagebox.showwarning("Invalid Move", "That move is not allowed!")
            
            self.selected_square = None
            self.load_board_image()
    
    def update_status(self):
        """Update status label and check game over conditions."""
        if self.board.is_checkmate():
            winner = "Black" if self.board.turn else "White"
            self.status_label.config(text=f"Checkmate! {winner} wins!")
        elif self.board.is_stalemate():
            self.status_label.config(text="Stalemate! It's a draw.")
        else:
            turn = "White" if self.board.turn else "Black"
            self.status_label.config(text=f"{turn} to move")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()
