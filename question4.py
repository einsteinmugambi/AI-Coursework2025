def check_case(char):
    
    if char.isupper():
        return "Uppercase"
    elif char.islower():
        return "Lowercase"
    else:
        return "Not a letter"
    
character = input("Enter a character: ")
result = check_case(character)
print(f"The character is {result}.")