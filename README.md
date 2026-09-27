Digital ATM Machine & Card Generator

A beginner-friendly Python console project that generates sample card details and simulates basic ATM transactions.

## Features

- Prompts for your name when generating card details.
- Generates a 16-digit card number, a 4-digit PIN, and a 6-character security code made from uppercase letters and digits.
- Starts with a sample balance of 80,000.
- Provides a menu to check the balance, deposit money, withdraw money, view transaction history, display card details, or close the program.
- Keeps deposit and withdrawal entries in transaction history while the program is running.

## Requirements

- Python 3.10 or later (the program uses `match`/`case` syntax).
- No external packages are required; the program uses Python's built-in `random` and `string` modules.

## Run the program

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python Digital_Transaction.py
   ```

   On some systems, use `python3 Digital_Transaction.py` instead.

## How to use

1. Enter your name when prompted.
2. The program generates card details for the demo.
3. Enter a menu number to select an action:

   | Choice | Action |
   | --- | --- |
   | 1 | Check the current balance |
   | 2 | Deposit an amount and add it to the balance |
   | 3 | Withdraw an amount and subtract it from the balance |
   | 4 | Display deposits and withdrawals made during this run |
   | 5 | Display the generated card number, PIN, and security code |
   | 6 | Close the program |

4. Enter another choice to continue, or choose `6` to exit.

## Important note

This project is for learning and demonstration only. It does not connect to a bank or payment network. The generated card number, PIN, and security code are random demo values and are not real or valid payment credentials. Do not use real financial or personal information with this program.

## Author

Gurpreet Kaushal
