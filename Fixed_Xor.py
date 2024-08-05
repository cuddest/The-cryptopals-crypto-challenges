from itertools import cycle


def xor(bin1, bin2):
    result = [int(bit1) ^ int(bit2) for bit1, bit2 in zip(bin1, bin2)]

    return "".join(str(bit) for bit in result)


def hex_to_xor(hex_string, key):
    binary_hex = bin(int(hex_string, 16))[2:]
    key_binary = bin(int(key, 16))[2:]
    desired_length = (
        len(binary_hex) if len(binary_hex) > len(key_binary) else len(key_binary)
    )
    binary_hex = binary_hex.zfill(desired_length)
    key_binary = key_binary.zfill(desired_length)
    encoded_xor = xor(binary_hex, key_binary)
    return hex(int(encoded_xor, 2))[2:]
