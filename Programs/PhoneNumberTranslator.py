# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

TRANSLATOR = {
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"],
}

# def phoneTranslator(digits):
#     if 1 > len(digits) > 4:
#         return [""]
#     possible = []
#     for digit in digits:
#         if digit not in range(2, 10):
#             return [""]
#         possible.append(TRANSLATOR[digit])