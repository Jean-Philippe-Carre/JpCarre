def compute_sum(x):
    # Convert the integer x to a string to form the repeated patterns
    x_str = str(x)

    # Generate the terms x, xx, xxx, and xxxx as integers
    term1 = int(x_str)
    term2 = int(x_str * 2)
    term3 = int(x_str * 3)
    term4 = int(x_str * 4)

    # Compute the sum of the terms
    result = term1 + term2 + term3 + term4

    return result


# Example usage:
x = int(input("Enter an integer: "))
print(f"The result of x + xx + xxx + xxxx for x = {x} is: {compute_sum(x)}")
