from base64 import b64decode, b64encode, b16decode, b16encode


def hex_to_base64(hex_string):
    decoded_hex = b16decode(hex_string.upper())
    encoded_b64 = b64encode(decoded_hex)
    return encoded_b64
