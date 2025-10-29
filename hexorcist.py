
"""Converts from any base that the user listed as their current numbers base, into decimal (base-10)"""
def to_decimal (number_string, original_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_string = number_string.upper()
    total_value = 0
    power = 0

    for char in number_string[::-1]:
        char_value = digits.index(char)
        total_value += (char_value * (original_base ** power))
        power += 1

    return total_value
        
"""Converts from decimal (base-10) to the base the user entered as their target converting base"""
def from_decimal(decimal_number, target_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if decimal_number == 0:
        return '0'
    
    result_string = ""

    while decimal_number > 0:
        remainder = decimal_number % target_base
        decimal_number = decimal_number // target_base
        char_to_add = digits[remainder]
        result_string = char_to_add + result_string
    return result_string
    

if __name__ == "__main__":
    print("Welcome to the base converter... you probably only needed this if your dumb... but anyways. ")
    print("Since you probably didn't know, here's a quick reminder: base 2 = binary, base 8 = octal, base 10 = decimal, base 16 = hex. This program allows you to input any base (2-36).")
    number = input("OK, now what is the number you would like to convert?: ")


    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    """Loop for all inputs to validate user inputs"""
    while True:
        """Asks user what base their number they want to convert is in"""
        while True:
            try:
                from_what_base = int(input("What is your number's current base?: "))
                if 2 <= from_what_base <= 36:
                    break
                else:
                    print("Invalid input! Must be a NUMBER from 2-36. Try again!")
            except ValueError:
                print("Invalid input! ")

        """Asks user what base they want to convert to"""
        while True:
            try:
                to_what_base = int(input("Alright, what base would you like to convert this number to?: "))
                if 2 <= to_what_base <= 36 and to_what_base != from_what_base:
                    break
                elif from_what_base == to_what_base:
                    print(f"Converting to the same base... the answer would obviously be {number}. Try again using a seperate target base.")
                    exit
                else:
                    print("Invalid input! Base must be a NUMBER from 2-36. Try again.")
            except ValueError:
                print("Invalid input! Base must be either 2, 8, 10, or 16. Try again.")

        """When the conversion is at work"""
        decimal_value = to_decimal(number, from_what_base)
        new_converted_number = from_decimal(decimal_value, to_what_base)

        print(f"{number} from base {from_what_base}, converted to base {to_what_base} = {new_converted_number}. This might literally be the easiest conversion ever, but whatever. ")

        """Asks user if they want to re-play the code and convert another number"""
        play_again = input("Would you like to convert another number (*please say no, please say no*)!? Enter 'y' if yes, and 'n' if no: ")
        if play_again != 'y':
            print("Thanks for asking your stupid questions! Bye...!")
            break