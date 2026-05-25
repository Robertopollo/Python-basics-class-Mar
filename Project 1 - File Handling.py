import math

class Calculator:
    def __init__(self):
        # Dictionary attribute to store operations
        self.operations = {}
        # Automatically initialize with basic operations
        self.initialize_basic_operations()

    def initialize_basic_operations(self):
        # Basic mathematical operations using lambda functions
        self.add_operation('+', lambda x, y: x + y)
        self.add_operation('-', lambda x, y: x - y)
        self.add_operation('*', lambda x, y: x * y)
        self.add_operation('/', lambda x, y: x / y if y != 0 else float('nan'))

    def add_operation(self, symbol, func):
        """Adds a new operation and function to the dictionary."""
        self.operations[symbol] = func

    def calculate(self, num1, symbol, num2):
        """Performs calculation with error handling for types and symbols."""
        # Use isinstance() to check if inputs are numbers
        if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
            print("Error: Input values must be numbers.")
            raise ValueError("Non-numeric input encountered.")

        # Check if the operation symbol is valid
        if symbol not in self.operations:
            print(f"Error: Operation symbol '{symbol}' is not valid.")
            raise KeyError(f"Invalid operation: {symbol}")

        try:
            result = self.operations[symbol](num1, num2)
            
            # Check for math errors like division by zero
            if isinstance(result, float) and math.isnan(result):
                print("Error: Mathematical error (e.g., division by zero or invalid log).")
                raise ArithmeticError("Invalid mathematical operation.")
                
            return result
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

# Separate functions for advanced mathematical operations
def exponentiation(x, y):
    return math.pow(x, y)

def square_root(x, y=None):
    # sqrt typically uses one number; num2 is ignored or can be 0
    return math.sqrt(x)

def logarithm(x, base):
    # math.log(x, base)
    return math.log(x, base)

def main():
    calc = Calculator()

    # Using add_operation to add advanced math library functions
    calc.add_operation('**', exponentiation)
    calc.add_operation('sqrt', square_root)
    calc.add_operation('log', logarithm)

    print("--- Python Dictionary Calculator ---")
    print("Available: +, -, *, /, ** (exp), sqrt (num1 only), log (num1=val, num2=base)")

    while True:
        choice = input("\nType 'exit' to quit or press Enter to continue: ").lower()
        if choice == 'exit':
            break

        try:
            # Getting user input
            raw_n1 = input("Enter first number: ")
            op_symbol = input("Enter operation symbol: ")
            raw_n2 = input("Enter second number: ")

            # Conversion to float (input is always string)
            n1 = float(raw_n1)
            n2 = float(raw_n2)

            # Execution
            res = calc.calculate(n1, op_symbol, n2)
            print(f"Result: {res}")

        except ValueError:
            print("Error: Please enter actual numbers.")
        except Exception:
            # Specific error messages are handled inside calculate()
            continue

if __name__ == "__main__":
    main()

