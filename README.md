# Basic Calculator

A lightweight, modular, and interactive Python command-line calculator. This application provides core arithmetic operations with color-coded terminal outputs, robust input validation, and a user-friendly control loop.

## Features

- **Core Arithmetic**: Supports addition, subtraction, multiplication, and division.
- **Robust Validation**: Detects and handles non-numeric inputs gracefully.
- **Safety**: Built-in exception handling for zero-division errors.
- **State Management**: Dedicated options to clear the terminal screen or exit.
- **Testable Architecture**: Calculation logic is separated into independent functions.
- **Visual Clarity**: ANSI color codes enhance terminal readability.

## Project Structure

```text
├── basiccalculator.py   # Main application script containing core logic and loop
└── README.md            # Project documentation
```

## Requirements

- Python 3.6 or higher
- Cross-platform support (Windows, macOS, Linux)

## Getting Started

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com
   ```
2. Navigate to the project directory:
   ```bash
   cd command-line-calculator
   ```

### Running the Application

Execute the script directly using Python:
```bash
python basiccalculator.py
```

## How to Use

1. **Select an Operator**: Choose from `+`, `-`, `*`, `/`, `clear`, or `exit`.
2. **Enter Numbers**: Provide the first and second numeric values when prompted.
3. **View Result**: The calculated output displays instantly in green text.
4. **Clear Session**: Type `clear` to reset the interface and start fresh.
5. **Terminate**: Type `exit` to close the program.

## Architecture & Code Quality

The project separates the user interface from core business logic to ensure maintainability:
- **Pure Functions**: Operational logic functions like `add()`, `subtract()`, `multiply()`, and `divide()` are independent of terminal inputs.
- **Exception Isolation**: Division validation prevents program crashes by isolating `ZeroDivisionError` handling within the menu runner loop.
