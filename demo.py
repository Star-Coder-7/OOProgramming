# a_string = "this is\na string split\t\t and tabbed"
# print(a_string)
#
# rawString = r"this is\na string split\t\t and tabbed"
# print(rawString)
#
# b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
# print(b_string)
#
# backslashString = "this is a backslash \followed by some text"
# print(backslashString)
#
# backslashString = "this is a backslash \\followed by some text"
# print(backslashString)
#
# errorString = r"this string ends with \\"
# print(errorString)

import random

highest = 10
answer = random.randint(1, highest)
print(answer)  # todo: remover after testing
print("Please guess the number between 1 and {}: ".format(highest))

for i in range(4):

