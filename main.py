# PyArt by MohamadKh75
# 2017-10-05
# ********************

import func

user_text = input("Please Enter Your String:\n")
arr = list(user_text)

for x in range(0, len(arr)):
    func.letter_reader(arr[x])
