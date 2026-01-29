# error_handling.py
# Program to demonstrate complete error handling in Python

import logging

# -------------------------------
# Logging configuration (save logs to file)
# -------------------------------
logging.basicConfig(
    filename="error.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Program started")

try:
    # -------------------------------
    # User input
    # -------------------------------
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    logging.debug(f"a = {a}, b = {b}")

    # -------------------------------
    # Simulate runtime error
    # -------------------------------
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    result = a / b
    print("Result =", result)

    # -------------------------------
    # Custom error
    # -------------------------------
    age = int(input("Enter age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above")

    print("Access granted")

# -------------------------------
# Multiple exception handling
# -------------------------------
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero")
    logging.error(e)

except ValueError as e:
    print("Value Error:", e)
    logging.error(e)

except Exception as e:
    print("Unexpected Error:", e)
    logging.error(e)

# -------------------------------
# Else block
# -------------------------------
else:
    print("Program executed successfully")
    logging.debug("No errors occurred")

# -------------------------------
# Finally block
# -------------------------------
finally:
    print("Program finished")
    logging.debug("Program ended")
