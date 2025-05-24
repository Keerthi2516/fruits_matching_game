# fruits_matching_game
# Candy Crush Game

A simple implementation of a Candy Crush-style matching game using Python and Tkinter.

## Description

This is a desktop version of the popular Candy Crush game where players match identical candies/fruits to score points. The game features:
- 5 different types of candies with different point values
- Random moves limit per game
- Target score to achieve
- Score tracking
- Visual effects for matches

## Game Elements

### Candies and Points
- 🍎 Apple: 3 points
- 🍌 Banana: 4 points
- 🍇 Grapes: 5 points
- 🍒 Cherry: 6 points
- 🍍 Pineapple: 7 points

### Game Rules
1. Match two identical adjacent candies
2. Each match adds the combined value of the candies to your score
   - Example: Matching two apples (3 points each) gives 6 points
3. You have a random number of moves (15-25) to reach the target score
4. Game ends when you either:
   - Reach the target score (Win!)
   - Run out of moves (Game Over)

## How to Play

1. **Starting the Game**
   - Run `python candyCrush.py`
   - The game board appears with random candies
   - Note your target score and moves remaining

2. **Making Moves**
   - Click on a candy to select it (highlighted in yellow)
   - Click an adjacent candy to attempt a match
   - If the candies match:
     - They disappear
     - You get points
     - New candies fall from above
   - If they don't match:
     - The second candy becomes selected instead

3. **Scoring**
   - Each successful match:
     - Adds the combined value of the matched candies
     - Decreases moves remaining by 1
   - Track your progress toward the target score

4. **Game End**
   - Win by reaching the target score
   - Lose if you run out of moves
   - Click "Play Again" to start a new game with new random values

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```

2. Navigate to the project directory:
   ```bash
   cd CandyCrush
   ```

3. Run the game:
   ```bash
   python candyCrush.py
   ```

## Game Features

1. **Random Elements**
   - Random candy placement
   - Random number of moves (15-25)
   - Random target score based on minimum possible points

2. **Visual Feedback**
   - Selected candy highlighting
   - Match disappearing animation
   - Score and points display
   - Moves counter

3. **Game States**
   - Initial board setup
   - Move validation
   - Win/lose conditions
   - Game reset functionality

## Tips for Playing

1. **Strategic Matching**
   - Focus on higher-value candies when possible
   - Plan your moves to reach the target score
   - Keep track of your remaining moves

2. **Efficient Scoring**
   - Pineapples (7+7 = 14 points) give the highest score
   - Cherries (6+6 = 12 points) are second best
   - Plan matches based on point values needed

## Development

This game was developed using:
- Python for game logic
- Tkinter for GUI
- Object-oriented programming principles
- Event-driven programming for user interactions

## Future Improvements

Potential features that could be added:
1. Sound effects
2. High score tracking
3. Different board sizes
4. Special candy combinations
5. Level progression system
