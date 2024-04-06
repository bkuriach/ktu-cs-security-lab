#  Implement MD5 Hashing algorithm from scratch

"""
This code is a low-level implementation of the MD5 algorithm and is not meant to be
easily understandable without a good knowledge of how MD5 works. For most practical 
purposes, you would use a library function like hashlib.md5() to compute MD5 hashes.
"""
import math

def left_rotate(x, n):
    """
    This function performs a left bitwise rotation on x by n bits. The & 0xFFFFFFFF 
    ensures that the result is a 32-bit number.
    Args:
        x (int): _description_
        n (int): _description_

    Returns:
        int: _description_
    """
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def pad_message(message):
    """
    This function pads the input message to ensure its length is a multiple of 512 bits, 
    as required by the MD5 algorithm. It first appends the bit '1' to the message, 
    then appends enough '0' bits until the length of the message is 448 (mod 512). 
    Finally, it appends the original length of the message as a 64-bit little-endian integer.

    Args:
        message (_type_): _description_

    Returns:
        _type_: _description_
    """
    original_length = len(message) * 8
    message += b'\x80'
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')
    return message

def md5(message):
    # Initialize variables
    # Initializes four 32-bit variables (h0, h1, h2, h3) to specific values defined by the MD5 standard.
    h0, h1, h2, h3 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476
    
    """
    Initializes two lists: s contains the shift amounts used in each round of the algorithm, 
    and K contains 64 constant values derived from the sine function.
    """
    s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
    K = [int(2**32 * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]

    # Preprocess the message
    message = pad_message(message)

    # Process each 512-bit block
    """
    Processes the message in 512-bit chunks. For each chunk, 
    it performs four rounds of a complex function that includes bitwise 
    operations and modular addition on the chunk and the variables 
    a, b, c, d (initialized to h0, h1, h2, h3 respectively).
    """
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        a, b, c, d = h0, h1, h2, h3

        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * j) % 16

            temp = d
            d = c
            c = b
            b = (b + left_rotate((a + f + K[j] + int.from_bytes(chunk[4 * g:4 * (g + 1)], 'little')), s[j])) & 0xFFFFFFFF
            a = temp
        """
        After processing each chunk, it adds the variables a, b, c, d to h0, h1, h2, h3 respectively
        """
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF

    # Produce the final hash value
    return (h0.to_bytes(4, 'little') + h1.to_bytes(4, 'little') +
            h2.to_bytes(4, 'little') + h3.to_bytes(4, 'little')).hex()

# Example usage
message_to_hash = b'Hello, world!'
hashed_value = md5(message_to_hash)
print(f"The MD5 hash of '{message_to_hash.decode()}' is: {hashed_value}")