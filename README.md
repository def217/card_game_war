# War - Card Game

## Overview
This program will simulate the card game "War" using Python and Object-Oriented Programming (OOP).

## Requirements

### What the Program Does
1. Uses a standard 52-card deck.
2. Splits the deck between two players.
3. Players reveal the top card from their decks each round:
   - The higher card wins, and the winner takes both cards.
   - If the cards tie, a "war" happens:
     - Each player plays extra cards to decide the winner.
4. The game ends when one player has all the cards or a set number of rounds is played.
5. The program announces the winner at the end.

### Code Structure
- **Classes**:
  - `Card`: Represents a single card.
  - `Deck`: Handles shuffling and dealing cards.
  - `Player`: Keeps track of a player's cards.
  - `Game`: Runs the game logic.

## How to Use
1. Clone the repository.
2. Run the program: `python war_game.py`.
3. (Optional) Run tests to check everything works: `pytest`.