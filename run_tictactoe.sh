#!/bin/bash

# Activate the virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Run the Tic Tac Toe game
python3 /Users/muham/Documents/GitHub/TicTacToe-Mac-OS/main.py
chmod +x /Users/muham/Documents/GitHub/TicTacToe-Mac-OS/run_tictactoe.sh
