base = int(input("Enter your base: "))
exp = int(input("Enter your exponent: "))
N = int(input("Enter your modulus: "))
result = 1

while exp > 0:
    if exp % 2 == 1:              
        result = (result * base) % N
    base = (base * base) % N      
    exp //= 2                   

print("Result:", result)
