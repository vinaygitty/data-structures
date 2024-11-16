"""
check password strength
"""
def multi_password_strength_counter(passwords):
    special_characters = "!@#$%^&*()-+"
    result = []
    for password in passwords:
        strength={'length': False, 'digit': False, 'lowercase': False, 'uppercase': False, 'special_char': False}
        if len(password) >= 8:
            strength['length'] = True
        for char in password:
            if char.isdigit():
                strength['digit'] = True
            elif char.islower():
                strength['lowercase'] = True
            elif char.isupper():
                strength['uppercase'] = True
            elif char in special_characters:
                strength['special_char'] = True

        result.append(strength)
    return(result)


passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)
for result in results:
    print(result)

# The expected output is:
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
# {'length': True, 'digit': True, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': False, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
