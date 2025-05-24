import tkinter as tk
import random

# Candy elements with their point values
CANDY_POINTS = {
    '🍎': 3,  # Apple
    '🍌': 4,  # Banana
    '🍇': 5,  # Grapes
    '🍒': 6,  # Cherry
    '🍍': 7   # Pineapple
}

class CandyCrush:
    def __init__(self, master, rows=8, cols=8):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.board = []
        self.buttons = []
        self.selected = None
        self.score = 0
        # Random moves between 15 and 25
        self.moves_left = random.randint(15, 25)
        # Random target score based on moves and minimum possible points
        min_target = self.moves_left * 6  # Minimum points possible (all apple matches)
        self.target_score = random.randint(min_target, min_target + 50)
        
        # Create the buttons first
        self.create_widgets()
        # Then create and display the board
        self.create_board()
        self.display_board()
        self.update_ui()

    def create_widgets(self):
        """Create grid of buttons and info labels for the game."""
        # Create info frame
        info_frame = tk.Frame(self.master)
        info_frame.grid(row=0, column=0, columnspan=self.cols, pady=10)
        
        # Left side - Score and Target
        score_frame = tk.Frame(info_frame)
        score_frame.pack(side=tk.LEFT, padx=20)
        
        self.score_label = tk.Label(score_frame, text=f"Score: {self.score}", font=('Arial', 16, 'bold'))
        self.score_label.pack()
        
        self.target_label = tk.Label(score_frame, text=f"Target: {self.target_score}", font=('Arial', 14), fg='red')
        self.target_label.pack()
        
        # Right side - Moves and Points Guide
        moves_frame = tk.Frame(info_frame)
        moves_frame.pack(side=tk.RIGHT, padx=20)
        
        self.moves_label = tk.Label(moves_frame, text=f"Moves Left: {self.moves_left}", font=('Arial', 14))
        self.moves_label.pack()
        
        # Points guide
        for candy, points in CANDY_POINTS.items():
            tk.Label(moves_frame, text=f"{candy}: {points}", font=('Arial', 12)).pack(side=tk.LEFT, padx=5)

        # Create game board
        game_frame = tk.Frame(self.master)
        game_frame.grid(row=1, column=0, columnspan=self.cols)
        
        for r in range(self.rows):
            button_row = []
            for c in range(self.cols):
                btn = tk.Button(game_frame, text='', width=4, height=2, font=('Arial', 20))
                btn.grid(row=r, column=c, padx=1, pady=1)
                btn.bind('<Button-1>', lambda e, r=r, c=c: self.on_candy_click(r, c))
                button_row.append(btn)
            self.buttons.append(button_row)

    def create_board(self):
        """Initialize the game board with random candies."""
        candies = list(CANDY_POINTS.keys())
        self.board = [[random.choice(candies) for _ in range(self.cols)] for _ in range(self.rows)]
        # Update the buttons with initial candies
        for r in range(self.rows):
            for c in range(self.cols):
                if self.buttons:  # Only update if buttons exist
                    self.buttons[r][c]['text'] = self.board[r][c]

    def display_board(self):
        """Update the display of all candies on the board."""
        for r in range(self.rows):
            for c in range(self.cols):
                self.buttons[r][c]['text'] = self.board[r][c]
        self.master.update()

    def update_ui(self):
        """Update all UI elements."""
        # Update the board display
        self.display_board()
        # Update score and moves
        self.score_label.config(text=f"Score: {self.score}")
        self.moves_label.config(text=f"Moves Left: {self.moves_left}")
        
        # Check win/lose conditions
        if self.score >= self.target_score:
            self.game_over(won=True)
        elif self.moves_left <= 0:
            self.game_over(won=False)

    def game_over(self, won):
        """Handle game over state."""
        # Disable all buttons
        for r in range(self.rows):
            for c in range(self.cols):
                self.buttons[r][c]['state'] = 'disabled'
        
        # Create game over window
        game_over_window = tk.Toplevel(self.master)
        game_over_window.title("Victory!" if won else "Game Over")
        
        # Game over message
        message = f"{'Congratulations! You reached the target!' if won else 'Out of moves!'}\n"
        message += f"Final Score: {self.score}\nTarget Score: {self.target_score}"
        
        tk.Label(
            game_over_window,
            text=message,
            font=('Arial', 16),
            pady=20,
            padx=20
        ).pack()
        
        # Play again button
        tk.Button(
            game_over_window,
            text="Play Again",
            command=lambda: [game_over_window.destroy(), self.reset_game()]
        ).pack(pady=10)

    def reset_game(self):
        """Reset the game with new random values."""
        self.score = 0
        self.moves_left = random.randint(15, 25)
        min_target = self.moves_left * 6
        self.target_score = random.randint(min_target, min_target + 50)
        self.selected = None
        
        # Enable all buttons and clear them
        for r in range(self.rows):
            for c in range(self.cols):
                self.buttons[r][c]['state'] = 'normal'
                self.buttons[r][c]['bg'] = 'SystemButtonFace'
        
        # Create new board and update display
        self.create_board()
        self.display_board()
        self.update_ui()

    def highlight_cell(self, r, c):
        """Highlight selected cell."""
        self.buttons[r][c]['bg'] = 'yellow'

    def clear_highlights(self):
        """Clear all highlights."""
        for row in self.buttons:
            for btn in row:
                btn['bg'] = 'SystemButtonFace'

    def swap_candies(self, r1, c1, r2, c2):
        """Swap two candies."""
        self.board[r1][c1], self.board[r2][c2] = self.board[r2][c2], self.board[r1][c1]
        self.update_ui()

    def find_matches(self):
        """Find matches of 2 adjacent candies."""
        matches = set()
        
        # Check horizontal matches (only pairs)
        for r in range(self.rows):
            for c in range(self.cols - 1):
                if (self.board[r][c] != ' ' and
                    self.board[r][c] == self.board[r][c+1]):
                    matches.add((r, c))
                    matches.add((r, c+1))
                    return matches  # Return only the first match found
        
        # Check vertical matches (only pairs)
        for c in range(self.cols):
            for r in range(self.rows - 1):
                if (self.board[r][c] != ' ' and
                    self.board[r][c] == self.board[r+1][c]):
                    matches.add((r, c))
                    matches.add((r+1, c))
                    return matches  # Return only the first match found
        
        return matches

    def calculate_match_score(self, matches):
        """Calculate score for matched candies."""
        if not matches:
            return 0
        
        # Get the first candy's value and multiply by 2 (for the pair)
        r, c = next(iter(matches))
        candy = self.board[r][c]
        pair_score = CANDY_POINTS[candy] * 2
        print(f"Matched pair of {candy} worth {CANDY_POINTS[candy]} each. Total: {pair_score}")
        return pair_score

    def remove_matches(self, matches):
        """Remove matched candies by setting them to empty."""
        # First make the matched candies disappear visually
        for r, c in matches:
            self.board[r][c] = ' '
            self.buttons[r][c]['text'] = ' '
            # Flash effect for disappearing
            self.buttons[r][c]['bg'] = 'white'
            self.master.update()
        
        # Short pause to show the disappearing effect
        self.master.after(100)
        
        # Reset button colors
        for r, c in matches:
            self.buttons[r][c]['bg'] = 'SystemButtonFace'
        self.master.update()

    def collapse_board(self):
        """Make candies fall down after removal."""
        # Process each column
        for c in range(self.cols):
            # Get non-empty candies in this column
            candies = []
            for r in range(self.rows-1, -1, -1):  # Start from bottom
                if self.board[r][c] != ' ':
                    candies.append(self.board[r][c])
            
            # Fill from bottom up
            r = self.rows - 1  # Start from bottom
            while r >= 0:
                if candies:
                    self.board[r][c] = candies.pop(0)
                else:
                    self.board[r][c] = ' '
                # Update the button immediately
                self.buttons[r][c]['text'] = self.board[r][c]
                self.master.update()
                r -= 1
            
            # Short pause after each column falls
            self.master.after(50)

    def refill_board(self):
        """Fill empty spaces with new random candies."""
        candies = list(CANDY_POINTS.keys())
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == ' ':
                    self.board[r][c] = random.choice(candies)
                    # Update the button immediately with animation
                    self.buttons[r][c]['bg'] = 'lightblue'
                    self.buttons[r][c]['text'] = self.board[r][c]
                    self.master.update()
                    self.master.after(50)
                    self.buttons[r][c]['bg'] = 'SystemButtonFace'
        
        self.master.update()

    def on_candy_click(self, r, c):
        """Handle user clicking on candies."""
        if self.moves_left <= 0:
            return
            
        if self.selected is None:
            # First click - just select the candy
            self.selected = (r, c)
            self.highlight_cell(r, c)
        else:
            r2, c2 = self.selected
            # Check if clicking the same candy - deselect it
            if r == r2 and c == c2:
                self.clear_highlights()
                self.selected = None
                return
                
            # Check if adjacent and same type of candy
            if abs(r - r2) + abs(c - c2) == 1 and self.board[r][c] == self.board[r2][c2]:
                # Same type of candy - match them
                candy = self.board[r][c]
                match_score = CANDY_POINTS[candy] * 2  # Add values of both candies
                self.score += match_score
                self.moves_left -= 1  # Decrease moves only on successful match
                
                # Show the points earned
                self.show_points_earned(match_score, r, c)
                
                # Remove the matched candies
                self.board[r][c] = ' '
                self.board[r2][c2] = ' '
                self.buttons[r][c]['text'] = ' '
                self.buttons[r2][c2]['text'] = ' '
                
                # Flash effect for disappearing
                self.buttons[r][c]['bg'] = 'white'
                self.buttons[r2][c2]['bg'] = 'white'
                self.master.update()
                self.master.after(100)
                
                # Reset colors
                self.buttons[r][c]['bg'] = 'SystemButtonFace'
                self.buttons[r2][c2]['bg'] = 'SystemButtonFace'
                
                # Make candies fall
                self.collapse_board()
                self.refill_board()
            else:
                # Not a match - select new candy
                self.clear_highlights()
                self.selected = (r, c)
                self.highlight_cell(r, c)
                return
            
            # Clear selection after move
            self.clear_highlights()
            self.selected = None
            
        # Update score display and check win/lose conditions
        self.update_ui()

    def show_points_earned(self, points, r, c):
        """Show floating points animation."""
        # Create a temporary label to show points
        points_label = tk.Label(
            self.master,
            text=f"+{points}",
            font=('Arial', 14, 'bold'),
            fg='green'
        )
        
        # Get the button's position on screen
        button = self.buttons[r][c]
        x = button.winfo_rootx() - self.master.winfo_rootx() + button.winfo_width()//2
        y = button.winfo_rooty() - self.master.winfo_rooty()
        points_label.place(x=x, y=y)
        
        # Animate the label moving up and fading
        def animate_points(step=0):
            if step < 10:  # Animation duration
                points_label.place(y=y - step*2)  # Move up
                self.master.after(50, lambda: animate_points(step + 1))
            else:
                points_label.destroy()  # Remove the label
        
        animate_points()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Candy Match")
    game = CandyCrush(root)
    root.mainloop()