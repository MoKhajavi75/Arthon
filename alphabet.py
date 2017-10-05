# PyArt by MohamadKh75
# 2017-10-05
# ********************

from pathlib import Path


# Set the Alphabet folder path
folder_path = Path("Alphabet").resolve()


# Read all Capital Letters - AA is Capital A
def letter_reader(letter):
    if 65 <= ord(letter) <= 90:
        letter_file = open(str(folder_path) + str("\\") + str(letter) + str(letter) + ".txt", 'r')
        letter_txt = letter_file.read()

    elif 97 <= ord(letter) <= 122:
        letter_file = open(str(folder_path) + str("\\") + str(letter) + ".txt", 'r')
        letter_txt = letter_file.read()

    print(letter_txt)
    letter_file.close()
