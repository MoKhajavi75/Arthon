# Arthon by MohamadKh75
# 2017-10-05
# ********************

from pathlib import Path
import linecache


# Set the Alphabet folder path
alphabet_folder_path = Path("Alphabet").resolve()
number_folder_path = Path("Number").resolve()
symbol_folder_path = Path("Symbol").resolve()


# Find the Path of Symbol
def pathFinder(letter):
    return {
        '!': str(symbol_folder_path) + str("\\") + "!.txt"
    }[letter]


# Create Pure Arthon [ Art + Python ]
def arthonize(user_text):
    result = open("Result.txt", 'w')

    for line_number in range(1, 10):

        arr = list(user_text)
        for x in range(0, len(arr)):
            letter = arr[x]

            # if it's Capital - AA is Capital A
            if 65 <= ord(letter) <= 90:
                letter_file = str(alphabet_folder_path) + str("\\") + str(letter) + str(letter) + ".txt"
                letter_txt = linecache.getline(letter_file, line_number).strip('\n')
                result.write(letter_txt)

            # if it's small - a is small a
            elif 97 <= ord(letter) <= 122:
                letter_file = str(alphabet_folder_path) + str("\\") + str(letter) + ".txt"
                letter_txt = linecache.getline(letter_file, line_number).strip('\n')
                result.write(letter_txt)

            # if it's Number
            elif 48 <= ord(letter) <= 57:
                letter_file = str(number_folder_path) + str("\\") + str(letter) + ".txt"
                letter_txt = linecache.getline(letter_file, line_number).strip('\n')
                result.write(letter_txt)

            # if it's Space
            elif ord(letter) == 32:
                result.write("   ")

            # if it's Symbol
            elif ord(letter) == 33 or 35 or 44 or 46 or 45 or 64 or 95 or 46 or 58:
                letter_file = pathFinder(letter)
                letter_txt = linecache.getline(letter_file, line_number).strip('\n')
                result.write(letter_txt)

            # if it's some kind of special symbol
            # NOT SUPPORTED in Ver. 3.0 - Will Be Added in Ver. 3.1 Someday Maybe...!
            else:
                print("Sorry, Some Symbols are NOT supported yet :)\n"
                      "Someday I'll Add them in Ver. 3.1, Maybe!")
                return

        result.write('\n')

    result.close()


def terminalize(user_text):
    """Coming Soon!"""


def lower(user_text):
    arr = list(user_text)
    arr = [element.lower() for element in arr]
    arthonize(arr)


def upper(user_text):
    arr = list(user_text)
    arr = [element.upper() for element in arr]
    arthonize(arr)


def toggle(user_text):
    arr = list(user_text)
    arr = [element.swapcase() for element in arr]
    arthonize(arr)
