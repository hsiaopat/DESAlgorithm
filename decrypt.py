import textwrap

EXPANSION_TABLE = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
                   16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

def apply_Expansion(expansion_table, bits32):
    """ This will take the expansion table and a 32-bit binary string as input and output a 48-bit binary string"""
    bits48 = ""
    for index in expansion_table:
        bits48 += bits32[index-1]
    return bits48

def XOR(bits1, bits2):
    """ Perform a XOR operation and return the output"""
    # Assuming both bit strings are of the same length
    xor_result = ""
    for index in range(len(bits1)):
        if bits1[index] == bits2[index]:
            xor_result += '0'
        else:
            xor_result += '1'
    return xor_result

SBOX = [
# Box-1
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
# Box-2

[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],

# Box-3

[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

],

# Box-4
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],

# Box-5
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
# Box-6

[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

],
# Box-7
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
# Box-8

[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]
]

def apply_IP(plaintext):
    """ Apply the Initial Permutation (IP) """
    ip_permutation_table = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]

    ip_result = ""
    for index in ip_permutation_table:
        ip_result += plaintext[index - 1]

    return ip_result

def apply_FP(final_result):
    """ Apply the Final Permutation (FP) """
    fp_permutation_table = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]

    fp_result = ""
    for index in fp_permutation_table:
        fp_result += final_result[index - 1]

    return fp_result

def split_in_6bits(XOR_48bits):
    """ Split 48 bits into 6 bits each """
    list_of_6bits = textwrap.wrap(XOR_48bits, 6)
    return list_of_6bits

def get_first_and_last_bit(bits6):
    """ Return the first and last bit from a binary string"""
    twobits = bits6[0] + bits6[-1]
    return twobits

def get_middle_four_bit(bits6):
    """ Return the middle four bits from a binary string"""
    fourbits = bits6[1:5]
    return fourbits

def binary_to_decimal(binarybits):
    """ Convert binary bits to decimal"""
    # Helps during list access
    decimal = int(binarybits, 2)
    return decimal

def decimal_to_binary(decimal):
    """ Convert decimal to binary bits"""
    binary4bits = bin(decimal)[2:].zfill(4)
    return binary4bits

def sbox_lookup(sboxcount, first_last, middle4):
    """ Take three parameters and access the S-box accordingly and return the value"""
    d_first_last = binary_to_decimal(first_last)
    d_middle = binary_to_decimal(middle4)

    sbox_value = SBOX[sboxcount][d_first_last][d_middle]
    return decimal_to_binary(sbox_value)

PERMUTATION_TABLE = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
                     2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

def apply_Permutation(permutation_table, sbox_32bits):
    """ It takes S-boxes output and a permutation table and returns a 32-bit binary string"""
    final_32bits = ""
    for index in permutation_table:
        final_32bits += sbox_32bits[index-1]
    return final_32bits

def functionF(pre32bits, key48bits):
    """ This is the main function to perform function F """
    result = ""
    expanded_left_half = apply_Expansion(EXPANSION_TABLE, pre32bits)
    xor_value = XOR(expanded_left_half, key48bits)
    bits6list = split_in_6bits(xor_value)
    for sboxcount, bits6 in enumerate(bits6list):
        first_last = get_first_and_last_bit(bits6)
        middle4 = get_middle_four_bit(bits6)
        sboxvalue = sbox_lookup(sboxcount, first_last, middle4)
        result += sboxvalue
    final32bits = apply_Permutation(PERMUTATION_TABLE, result)
    return final32bits

def split_in_half(bits_64):
    """ Split the 64 bits into left and right halves """
    left, right = bits_64[:32], bits_64[32:]
    return left, right

def decrypt_round_keys(ciphertext, round_keys):
    # Initial Permutation (IP)
    initial_permutation_result = apply_IP(ciphertext)

    # Split the 64-bit ciphertext into left and right halves
    left64, right64 = split_in_half(initial_permutation_result)

    # Perform 16 rounds of decryption
    for round_number in range(16):
        # Apply Function F using the current round key
        round_key = round_keys[round_number]
        function_f_result = functionF(right64, round_key)
        #print(function_f_result)

        # XOR the result with the corresponding left half from the previous round
        xor_result = XOR(left64, function_f_result)

        # Swap the left and right halves
        left64, right64 = right64, xor_result

    # Swap the final left and right halves before applying Final Permutation (FP)
    final_result = right64 + left64

    # Final Permutation (FP)
    decrypted_result = apply_FP(final_result)

    return decrypted_result

# Assume apply_IP and apply_FP functions are defined elsewhere in your code
# Example usage:


#I reversed them
subkeys = ["101000001001001011000010101100111110000011011110", "101000010001001001010010110000110010111000011111", "001001010101101011011000001110110011001010011000", "000101110111000111010000001100010101000000100111", "000111100100110111011001000000100010100010100110", "010111110110000100001101101001000010100110010101", "000010101000110110000101001001110000001111010011", "010110010010100000101111010101111000000101000011", "010010011000111010101100011101001000001101001110", "001100001000111001101010010010001011010001101001", "111000000111100000100110001010101111110000101000", "101000011010111101010100001010000101110000110010", "010001000111011010111011100010010100100000110010", "010111110100001110110111111100101110011100111010", "111101101001010101111000100000010100101100010000", "100100101101100110110011100101010000101000010000"]
subkeys.reverse()
ciphertext = "1100101011101101101000100110010101011111101101110011100001110011"
decrypted_result = decrypt_round_keys(ciphertext, subkeys)

print("Decrypted Result:", decrypted_result)