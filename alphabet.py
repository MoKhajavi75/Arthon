# PyArt by MohamadKh75
# 2017-10-05
# ********************

from pathlib import Path


# Set the Alphabet folder path
folder_path = Path("Alphabet").resolve()


# Read all Capital Letters - AA is Capital A
def capital_letter_reader(letter):
    letter_file = open(str(folder_path) + str("\\") + str(letter) + str(letter) + ".txt", 'r')
    letter_txt = letter_file.read()
    print(letter_txt)
