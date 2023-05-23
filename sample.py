from math import pow

a = int(input("a: "))
b = int(input("b: "))

def exponential_value(x, y):
    """This function will help us to 
    return the exponential value"""
    return pow(x, y)

if __name__ == "__main__":
    print(exponential_value(a, b))