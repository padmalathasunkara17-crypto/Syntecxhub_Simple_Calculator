import sys
import os

#colors for terminal output
RESET  = "\033[0m"
HEADER = "\033[95m"
MENU   = "\033[96m"
RESULT = "\033[92m"
ERROR  = "\033[91m"
INPUT  = "\033[93m"


def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    return x / y



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"{ERROR}Invalid input. Please enter a valid number.{RESET}")


#main function to run the calculator
def main():
    if os.name == 'nt':
        os.system('')
        
    print(f"{HEADER}================================={RESET}")
    print(f"{HEADER}|=== Command Line Calculator ===|{RESET}")
    print(f"{HEADER}================================={RESET}")
    
    while True:
        print(f"\nSelect any operator: {MENU}+, -, *, /, clear, exit{RESET}")
        operator = input(f"{INPUT}Enter operator: {RESET}").strip().lower()

        if operator == 'exit':
            print(f"{HEADER}Goodbye!{RESET}")
            sys.exit()
            
        if operator == 'clear':
            clear_screen()
            print(f"{MENU}Calculator cleared.{RESET}")
            continue

        if operator not in ['+', '-', '*', '/']:
            print(f"{ERROR}Invalid operator. Please try again.{RESET}")
            continue

        num1 = get_number(f"{INPUT}Enter first number: {RESET}")
        num2 = get_number(f"{INPUT}Enter second number: {RESET}")

        try:
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
                
            print(f"\n{RESULT}Result: {num1} {operator} {num2} = {result}{RESET}")
            
        except ZeroDivisionError as e:
            print(f"{ERROR}{e}{RESET}")

if __name__ == "__main__":
    main()
