import random

for i in range(100):
    should_generate = input("Press enter to Generate")
    if should_generate == "":
        lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                             "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        uppercase_letters = ["A", "B", "C", "B", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                             "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        numbers_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        special_characters = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[",
                              "}", "]", "|", ":", ";", "<", ">", ".", "?", "/"]
        final_set = [str(random.choice(lowercase_letters)), str(random.choice(lowercase_letters)),
                     str(random.choice(lowercase_letters)), str(random.choice(lowercase_letters)),
                     str(random.choice(uppercase_letters)), str(random.choice(uppercase_letters)),
                     str(random.choice(uppercase_letters)), str(random.choice(uppercase_letters)),
                     str(random.choice(numbers_digits)), str(random.choice(numbers_digits)),
                     str(random.choice(numbers_digits)), str(random.choice(numbers_digits)),
                     str(random.choice(special_characters)), str(random.choice(special_characters)),
                     str(random.choice(special_characters)), str(random.choice(special_characters))]
        print(random.choice(final_set) + random.choice(final_set) + random.choice(final_set) + random.choice(
            final_set) + random.choice(final_set) + random.choice(final_set) + random.choice(final_set) + random.choice(
            final_set) + random.choice(final_set) + random.choice(final_set) + random.choice(final_set) + random.choice(
            final_set) + random.choice(final_set) + random.choice(final_set) + random.choice(final_set) + random.choice(
            final_set))
    else:
        exit()
