import string
def cipher(word, msg):
    wstr = word
    count = 0
    cmsg =[]
    frstlen = len(word)
    #repeat the codeword until length of message
    while len(wstr) != len(msg):
        wstr+=wstr[len(wstr)%frstlen]
    #create the cipher table
    oglist = list(string.ascii_lowercase)
    char = [[oglist[(x+y)%26] for x in range(26)] for y in range(26)]
    #generate the coded message
    while len(cmsg) != len(msg):
        cmsg+=char[ord(wstr[count])-97][ord(msg[count])-97]
        count+=1
    print(''.join(cmsg))

cipher(input('Enter the code word: '),input('Enter the message to encrypt: '))