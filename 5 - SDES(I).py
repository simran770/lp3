"""

Consider the 10 bit input key as: 1010000010, apply permuted choice 1, then circular
left shift and finally permuted choice 2 and generate 8 bit round keys for TWO
rounds

"""


def PC(ip, pc):
    result = ""
    for i in pc:
        result += ip[i-1]

    return result


def leftShift(key, bits):
    result = key
    for i in range(bits):
        result = result[1:] + result[0]
    return result


if __name__ == '__main__':
    P10table = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
    P8table = (6, 3, 7, 4, 8, 5, 10, 9)
    IPKey = '1010000010'

    print(f"\nInput 10-bit Key: {IPKey}")

    print(f"\n*****PC1*****")
    PC10Key = PC(IPKey, P10table)
    print(f"Key after P10 Permutation: {PC10Key[:5]} {PC10Key[5:]}")
    leftHalf = PC10Key[:5]
    rightHalf = PC10Key[5:]
    left = leftShift(leftHalf, 1)
    right = leftShift(rightHalf, 1)
    print(f"Key after left shift(1 bit): {left} {right}")
    SubKey1 = PC(left+right, P8table)
    print(f"First Subkey: {SubKey1[:4]} {SubKey1[4:]}")

    print(f"\n*****PC2*****")
    left = leftShift(left, 2)
    right = leftShift(right, 2)
    print(f"Key after left shift(2 bits): {left} {right}")
    SubKey2 = PC(left + right, P8table)
    print(f"Second Subkey: {SubKey2[:4]} {SubKey2[4:]}")
