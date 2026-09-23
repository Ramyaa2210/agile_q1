def multiply(a, b):
    # For the first run (Passing):
    return a * b
    
    # For the second run (Failing):
    # return a * b + 1 

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
