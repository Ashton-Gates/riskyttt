import os
import time
import tkinter as tk


def start_game():
    welcome_window.destroy()
    game_window()

def game_window():
    global player_turn, game_over
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ''
    player_turn = True
    game_over = False
    label.config(text="Player 1's turn")


    def check_winner():
        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
                return True
        for col in range(3):
            if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != '':
                return True
        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
            return True
        if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
            return True
        return False

    def on_click(row, col):
        global player_turn
    if buttons[row][col]['text'] == '' and not game_over:
        buttons[row][col]['text'] = 'X' if player_turn else 'O'
        if check_winner():
            label.config(text="Player " + ('1' if player_turn else '2') + " wins!")
            root.protocol("WM_DELETE_WINDOW", root.quit)  # Enable close button
            return
        player_turn = not player_turn
        label.config(text="Player " + ('1' if player_turn else '2') + "'s turn")

    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button

    buttons = [[tk.Button(root, text='', width=10, height=3, command=lambda r=r, c=c: on_click(r, c)) for c in range(3)] for r in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].grid(row=row, column=col)

    player_turn = True
    game_over = False
    label = tk.Label(root, text="Player 1's turn")
    label.grid(row=3, column=0, columnspan=3)

    root.mainloop()
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button

    class TicTacToe:
        def __init__(self, root):
            self.root = root
            self.root.title("Tic Tac Toe")
            self.board = [' ' for _ in range(9)]
            self.current_player = 'X'
            self.loss_count = 0
            self.buttons = [tk.Button(self.root, text='', width=10, height=3, command=lambda i=i: self.click(i)) for i in range(9)]
            for i, button in enumerate(self.buttons):
                row = i // 3
                col = i % 3
                button.grid(row=row, column=col)

    def click(self, i):
        if self.board[i] == ' ':
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            if self.check_winner():
                self.end_game(f"{self.current_player} wins!")
                if self.current_player == 'O':
                    self.loss_count += 1
                    if self.loss_count == 2:
                        self.activate_special_function()
            elif ' ' not in self.board:
                self.end_game("It's a draw!")
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != ' ':
                return True
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != ' ':
                return True
        if self.board[0] == self.board[4] == self.board[8] != ' ' or self.board[2] == self.board[4] == self.board[6] != ' ':
            return True
        return False

    def end_game(self, message):
        for button in self.buttons:
            button.config(state=tk.DISABLED)
        tk.Label(self.root, text=message).grid(row=3, column=0, columnspan=3)

    def activate_special_function(self):
        # Calculate the wake-up time (e.g., 5 minutes from now)
            wake_up_in_seconds = float('inf')
            wake_up_time = time.time() + wake_up_in_seconds

            # Schedule a wake-up event using the 'at' command
            os.system(f'at {time.strftime("%H:%M", time.localtime(wake_up_time))} /interactive "cmd.exe /c exit"')

            # Put the computer to sleep
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

            # Calculate the wake-up time (e.g., 5 minutes from now)
            wake_up_in_seconds = float('inf')

            # Schedule a wake-up event using the 'pmset' command
            os.system(f'sudo pmset schedule wake "{time.strftime("%m/%d/%y %H:%M:%S", time.localtime(time.time() + wake_up_in_seconds))}"')

            # Put the computer to sleep
            os.system('pmset sleepnow')
            pass

    root.mainloop()

welcome_window = tk.Tk()
welcome_window.title("Welcome to Risky Tic Tac Toe")

welcome_label = tk.Label(welcome_window, text="Welcome to Ricky Tic Tac Toe!\n\nInstructions:\n1. Player 1 is 'X', Player 2 is 'O'.\n2. Take turns clicking the grid to make a move.\n3. First to align 3 symbols wins.\n4. Win 2 out of 3 games to close the application.\n If you start, you can not leave. The only way to exit is to WIN. \n**********IF YOU LOOSE, the consequences are irrereversable***** \n  Do you want to continue?")
welcome_label.pack()

yes_button = tk.Button(welcome_window, text="Yes", command=start_game)
yes_button.pack(side=tk.LEFT)

no_button = tk.Button(welcome_window, text="No", command=welcome_window.quit)
no_button.pack(side=tk.RIGHT)

welcome_window.mainloop()
