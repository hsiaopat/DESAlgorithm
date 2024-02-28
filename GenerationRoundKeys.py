def apply_PC1(pc1_table,keys_64bits):
    """ This function takes Permutation table and initial key as input and return 56 bits key as output"""
    keys_56bits = ""
    for index in pc1_table:
        keys_56bits += keys_64bits[index-1] 
    return keys_56bits

#This is PC1
PC1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
keys_64bits = "0100110001001111010101100100010101000011010100110100111001000100" #our key
keys_56bits = apply_PC1(PC1,keys_64bits)

def split_in_half(keys_56bits):
    """ Split the 56 bits key into two equal half """
    left_keys, right_keys = keys_56bits[:28],keys_56bits[28:]
    return left_keys, right_keys
left56 , right56 = split_in_half(keys_56bits)

def circular_left_shift(bits,numberofbits):
    """This method will circularly shift the given bit string according to the number of bits"""
    shiftedbits = bits[numberofbits:] + bits[:numberofbits]
    return shiftedbits


def apply_PC2(pc2_table,keys_56bits):
    """ This will take Compression table and combined both half as input and return a 48-bits string as output"""
    keys_48bits = ""
    for index in pc2_table:
        keys_48bits += keys_56bits[index-1]
    return keys_48bits
PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2, 41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]


def generate_keys(key_64bits):
    round_keys = list() 
    pc1_out = apply_PC1(PC1,key_64bits) 
    L0,R0 = split_in_half(pc1_out)
    for roundnumber in range(16):
        newL = circular_left_shift(L0,round_shifts[roundnumber])
        newR = circular_left_shift(R0,round_shifts[roundnumber])
        roundkey = apply_PC2(PC2,newL+newR)
        round_keys.append(roundkey)
        L0 = newL
        R0 = newR
    return round_keys
round_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
key_64bits = "0001001100110100010101110111100110011011101111001101111111110001"
subkeys = generate_keys(key_64bits)
# The subkeys will have all 16 keys as Python list
for i in subkeys:
    print(i)