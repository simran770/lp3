"""

Consider the sub-key for round 0 is **Key0 = w0w1 = 0100 1010 1111 0101**. Take a 16-bit Plaintext as **P: 1101 0111 0010 1000**. Perform the add round 0 key operation, followed by Nibble substitution (S-Boxes), and finally display the output after shift row operation

"""

sbox = [9, 4, 10, 11, 13, 1, 8, 5, 6, 2, 0, 3, 12, 14, 15, 7]


# Add round key 0
def addRound(key, plain):
    x = [key[:4], key[4:8], key[8:12], key[12:16]]

    for i in range(4):  # binary to decimal for each nible
        x[i] = list(map(int, x[i]))
        x[i] = x[i][0] * 8 + x[i][1] * 4 + x[i][2] * 2 + x[i][3]
    keylist = [x[0], x[1], x[2], x[3]]

    y = [plain[:4], plain[4:8], plain[8:12], plain[12:16]]

    for i in range(4):  # binary to decimal for each nible
        y[i] = list(map(int, y[i]))
        y[i] = y[i][0] * 8 + y[i][1] * 4 + y[i][2] * 2 + y[i][3]
    plainlist = [y[0], y[1], y[2], y[3]]
    result1 = [x[0] ^ y[0], x[1] ^ y[1], x[2] ^ y[2], x[3] ^ y[3]]
    return result1


# Nibble Substitution
def substitution(result1):
    slist = []
    for i in range(4):
        slist.append(sbox[result1[i]])
    # print(slist)
    return slist


# Shift Row
def shift(slist):
    temp = slist[3]
    slist[3] = slist[1]
    slist[1] = temp
    return slist


if __name__ == '__main__':
    plain = "1101011100101000"
    key = "0100101011110101"
    result1 = addRound(key, plain)
    res1 = [bin(i) for i in result1]
    print(f"Add Round Key 0 Operation: {res1}\n")
    result2 = substitution(result1)
    res2 = [bin(i) for i in result2]
    print(f"Nibble substitution: {res2}\n")
    result3 = shift(result2)
    res3 = [bin(i) for i in result3]
    print(f"Shift Operation: {res3}")
