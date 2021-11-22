
#EXERCISE 4 (version 1)

def runlength(bits):
    counter=1
    for i in range(len(bits)):
        if len(bits) <= i:
            break
        if bits[i]==0:
            while bits[i+1] == 0: #while the next position is a 0
                counter += 1 #we count the number of 0s
                bits.pop(i + 1) #we get rid of this 0 in the copy list
                if i+1>=len(bits):
                    break
            bits.insert(i+1,counter) #we insert the number of 0s after the first 0
            counter=1

    return (bits)

list = str(input("Please enter the items, separated by comas: "))
bits = list.split(",")
for i in range(len(bits)):
    bits[i]=int(bits[i])

print("The original code is:", bits)
print("After the run length encoding the code is:", runlength(bits))





