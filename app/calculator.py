"""Simple calculator app — logic + CLI in one file."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(operation: str, a: float, b: float) -> float:
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return operations[operation](a, b)


def get_number(prompt: str) -> float | None:
    value = input(prompt).strip()
    if value.lower() == "q":
        return None
    return float(value)


def main():
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide")
    print('Enter "q" at any prompt to quit.\n')
    while True:
        operation = input("Enter operation: ").strip().lower()
        if operation == "q":
            print("Goodbye!")
            break
        a = get_number("Enter first number: ")
        if a is None:
            print("Goodbye!")
            break
        b = get_number("Enter second number: ")
        if b is None:
            print("Goodbye!")
            break
        try:
            result = calculate(operation, a, b)
            print(f"Result: {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
