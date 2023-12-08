import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x400")

        self.player_name = tk.StringVar()

        self.create_name_screen()

    def create_name_screen(self):
        name_frame = tk.Frame(self.root)
        name_frame.pack(pady=20)

        tk.Label(name_frame, text="Enter Your Name:").grid(row=0, column=0, padx=10)
        entry_name = tk.Entry(name_frame, textvariable=self.player_name)
        entry_name.grid(row=0, column=1, padx=10)

        tk.Button(name_frame, text="Continue", command=self.create_game_list_screen).grid(row=1, columnspan=2, pady=10)

    def create_game_list_screen(self):
        if not self.player_name.get():
            tk.messagebox.showerror("Error", "Please enter your name.")
            return

        game_list_frame = tk.Frame(self.root)
        game_list_frame.pack(pady=20)

        tk.Label(game_list_frame, text=f"Welcome, {self.player_name.get()}!").grid(row=0, columnspan=2)

        tk.Label(game_list_frame, text="Game List").grid(row=1, columnspan=2, pady=10)

        games = []  # You may replace this list with actual game data

        for game in games:
            tk.Label(game_list_frame, text=game).grid(row=games.index(game) + 2, columnspan=2)

        tk.Button(game_list_frame, text="Create Game", command=self.create_game_screen).grid(row=len(games) + 2,
                                                                                             columnspan=2, pady=10)

    def create_game_screen(self):
        game_screen = tk.Toplevel(self.root)
        game_screen.title("Tic Tac Toe Game")

        board_size_frame = tk.Frame(game_screen)
        board_size_frame.pack(pady=10)

        tk.Label(board_size_frame, text="Game Name:").grid(row=0, column=0, padx=10)
        entry_game_name = tk.Entry(board_size_frame)
        entry_game_name.grid(row=0, column=1, padx=10)

        tk.Label(board_size_frame, text="Board Color:").grid(row=1, column=0, padx=10)
        entry_board_color = tk.Entry(board_size_frame)
        entry_board_color.grid(row=1, column=1, padx=10)

        tk.Button(board_size_frame, text="Start Game", command=lambda: self.start_game(entry_game_name.get(),
                                                                                      entry_board_color.get())).grid(
            row=2, columnspan=2, pady=10)

    def start_game(self, game_name, board_color):
        game = GameWindow(self.root, game_name, board_color)


class GameWindow:
    def __init__(self, root, game_name, board_color):
        self.root = root
        self.root.withdraw()  # Hide the main window while the game window is active

        self.game_name = game_name
        self.board_color = board_color

        self.game_screen = tk.Toplevel(self.root)
        self.game_screen.title(self.game_name)
        self.game_screen.configure(bg=self.board_color)

        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.game_screen, text='', font=('normal', 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.click(row, col),
                                   bg=self.board_color)
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = 'X'
            self.update_board()

            if self.check_winner('X'):
                tk.messagebox.showinfo("Game Over", f"{self.game_name} won!")
                self.root.deiconify()
                self.game_screen.destroy()
            elif self.is_board_full():
                tk.messagebox.showinfo("Game Over", "It's a tie!")
                self.root.deiconify()
                self.game_screen.destroy()
            else:
                self.computer_move()

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        if empty_cells:
            computer_move = random.choice(empty_cells)
            self.board[computer_move[0]][computer_move[1]] = 'O'
            self.update_board()

            if self.check_winner('O'):
                tk.messagebox.showinfo("Game Over", "Computer won!")
                self.root.deiconify()
                self.game_screen.destroy()
            elif self.is_board_full():
                tk.messagebox.showinfo("Game Over", "It's a tie!")
                self.root.deiconify()
                self.game_screen.destroy()

    def update_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text=self.board[i][j], state=tk.DISABLED if self.board[i][j] != ' ' else tk.NORMAL)

    def check_winner(self, marker):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.board[i][j] == marker for j in range(3)) or all(self.board[j][i] == marker for j in range(3)):
                return True
        if all(self.board[i][i] == marker for i in range(3)) or all(self.board[i][2 - i] == marker for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))


if __name__ == "__main__":
    root = tk.Tk()
    tic_tac_toe = TicTacToe(root)
    root.mainloop()


