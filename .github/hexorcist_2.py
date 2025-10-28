print("Welcome to... (snarky welcome message)")
print("Quick Reminder: base 2 = binary, base 8 = octal, base 10 = decimal, base 16 = hex")

number_string = input("What is the number you would like to convert?: ")
new_char_value = number_string.upper()
from_what = int(input("Ok, what is your numbers current base?: "))
to_what = int(input("Alright... what base would you like to convert this number to?: "))


digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_decimal (number_string, from_what):
    total_value = 0
    power = 0
    for char in number_string:
        number_string[::-1]
    total_value += (total_value * (from_what ** power))
    power += 1
    return total_value
        
def from_decimal(to_decimal, number_string):
    result_string = ""
    if number_string == 0:
        return '0'
    else:
        while number_string > 0:
            remainder = number_string % to_decimal
            number_string = number_string // to_decimal
            char_to_add = digits[remainder]
        result_string = char_to_add + result_string
        return result_string
    
print(f"{number_string} (originally input number) , {from_what} (curren base input) {to_decimal(number_string, from_what)} (returns integer) , {from_decimal(to_decimal, number_string)}")