print("Welcome to... (snarky welcome message)")
print("Quick Reminder: base 2 = binary, base 8 = octal, base 10 = decimal, base 16 = hex")

number_what_to = input("First of all, would you like to convert your number to 1: binary, 2: octal, 3: hex?: ")


"""Convert decimal base number to binary base:"""
def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = []
    while n > 0:
        remainder = n % 2
        binary.append(str(remainder))
        n //= 2

    binary.reverse()
    return ''.join(binary)

if number_what_to == "1":
    num_str = input("Enter a decimal number that you would like to convert to binary: ").strip()
    num = int(num_str)
    binary_number = decimal_to_binary(num)
    print(f"The decimal number {num_str} converted to binary is: {binary_number}")


"""Convert decimal base number to octal base:"""
def decimal_to_octal(n):
    if n == 0:
        print("Uhm... the answer should be obvious...0")
        return "0"
    
    digits = []
    while n > 0:
        remainder = n % 8
        digits.append(str(remainder))
        n //= 8

    digits.reverse()
    return ''.join(digits)

if number_what_to == "2":
    num_str = input("Enter a decimal number that you would like to convert to octal: ").strip()
    num = int(num_str) 
    octal_number = decimal_to_octal(num)
    print(f"The decimal number {num_str} converted to octal is: {octal_number}")



def decimal_to_hex(n):
    if n == 0:
        print("Uhm... the answer should be obvious...0")
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hex = []

    while n > 0:
        remainder = n % 16
        hex.append(digits[remainder])
        n //= 16

    hex.reverse()
    return ''.join(hex)

if number_what_to == "3":
    num_str = input("Enter a decimal number that you would like to convert to hex: ").strip()
    num = int(num_str) 
    hex_number = decimal_to_hex(num)
    print(f"The decimal number {num_str} converted to hex is: {hex_number}")
