class Calcurator:
    # A simple calculator class to perform basic arithmetic operations.
    def __init__(self, name: str):
        self.name = name
        print(f"{self.name} initialized.")

    def add(self, a : float, b : float) -> float:
        print(f"Adding {b} to {a} = ")
        return a + b
    
    def substract(self, a : float, b : float) -> float:
        print(f"Subtracting {b} from {a} = ")
        return a - b
    
    def multiply(self, a : float, b : float) -> float:
        print(f"Multiplying {a} with {b} = ")
        return a * b
    
    def divide(self, a : float, b : float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        else:
            print(f"Dividing {a} by {b} = ")
            return a / b
        
    def exponentiation(self, a : int, b : int) -> int:
        print(f"Exponentiation {a} to the power of {b} = ")
        return a ** b
    
    def square_root(self, a : float) -> float:
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number.")
        else:
            print(f"Calculating square root of {a} = ")
            return a ** 0.5