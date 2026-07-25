# 📈 Stock Portfolio Tracker

## About the Project
This is my Stock Portfolio Tracker project, made as part of my Python internship task at CodeAlpha.  
It’s a simple command‑line program where you enter stock names and quantities, and the program calculates the total investment value. The stock prices are stored in a hardcoded dictionary. You can also choose to save the results into a `.txt` or `.csv` file.

## What It Can Do
- Lets you input stock symbols (like AAPL for Apple, TSLA for Tesla).
- Uses a dictionary with hardcoded prices to calculate values.
- Multiplies stock price × quantity to get the investment value.
- Shows a portfolio summary with each stock and the total.
- Optionally saves the results into a `.txt` or `.csv` file.

## Concepts I Used
Since this task was meant to practice a few core Python basics, here’s where each one shows up in my code:
- **dictionary** → stores stock prices for quick lookup.
- **input/output** → takes user input and prints results.
- **basic arithmetic** → calculates value = price × quantity.
- **file handling (optional)** → saves portfolio summary to a file.

## How to Run It
1. Install Python 3 if you don’t already have it.
2. Download `stock_tracker.py` from this repo.
3. Open a terminal in that folder and type:
   ```bash
   python3 stock_tracker.py
