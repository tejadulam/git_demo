from math import pow

a = int(input("a: "))
b = int(input("b: "))

def exponential_value(x, y):
    return pow(x, y)

if __name__ == "__main__":
    print(exponential_value(a, b))