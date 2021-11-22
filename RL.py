#EXERCISE 4 (version 2)

from collections import OrderedDict

def RL(input):
    dict = OrderedDict.fromkeys(input,0)
    for ch in input:
        dict[ch]+=1

    output = ''
    for key,value in dict.items():
        output = output+key+str(value)
    return  output

input = str(input("Please enter the strings: "))
print("The encoded string is: ", RL(input))