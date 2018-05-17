#not working. Need to work out why j isn't working for my index and instead is giving me the same thing. 
import string
def decipher(word, cmsg):
    print(cmsg)
    wstr = word
    count = 0
    msg =[]
    frstlen = len(word)
    while len(wstr) != len(cmsg):
        wstr+=wstr[len(wstr)%frstlen]
    oglist = list(string.ascii_lowercase)
    char = [[oglist[(x+y)%26] for x in range(26)] for y in range(26)]

    while count != len(cmsg):
        j = ord(wstr[count])-97
        for x in char[j]:
            print(x)
            i = ord(x)-97
            if cmsg[count] == char[j][i]:
                msg+=char[j][i]
        count+=1
    print(''.join(cmsg))

decipher(input('Enter the code word: '),input('Enter the message to decrypt: '))