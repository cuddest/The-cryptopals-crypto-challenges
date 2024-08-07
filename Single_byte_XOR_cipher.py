from base64 import b64decode, b64encode, b16decode, b16encode

char_fr = {
    "a": 0.0651738,
    "b": 0.0124248,
    "c": 0.0217339,
    "d": 0.0349835,
    "e": 0.1041442,
    "f": 0.0197881,
    "g": 0.0158610,
    "h": 0.0492888,
    "i": 0.0558094,
    "j": 0.0009033,
    "k": 0.0050529,
    "l": 0.0331490,
    "m": 0.0202124,
    "n": 0.0564513,
    "o": 0.0596302,
    "p": 0.0137645,
    "q": 0.0008606,
    "r": 0.0497563,
    "s": 0.0515760,
    "t": 0.0729357,
    "u": 0.0225134,
    "v": 0.0082903,
    "w": 0.0171272,
    "x": 0.0013692,
    "y": 0.0145984,
    "z": 0.0007836,
    " ": 0.1918182,
}


def xor_to_one_char(bin1, bin2):
    result = b""
    for char in bin1:
        result += bytes([char ^ bin2])

    return result


def calculate_frenquency(char):
    score = 0
    for i in char:
        score += char_fr.get(chr(i).lower(), 0)
    return score


def xor_brute_force(hex_string):
    results = []
    hex_string_byte = bytes.fromhex(hex_string)
    print(hex_string_byte)
    highest_frequency = {"key": 0, "score": 0.0, "text": "blalala"}
    for i in range(256):
        result = xor_to_one_char(hex_string_byte, i)
        result_frenquency = calculate_frenquency(result)
        if result_frenquency > highest_frequency["score"]:
            highest_frequency["key"] = i
            highest_frequency["score"] = result_frenquency
            highest_frequency["text"] = result
    return highest_frequency


print(
    xor_brute_force(
        "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    )
)
# here's the result after running the code :
# {'key': 88, 'score': 2.2641049, 'text': b"Cooking MC's like a pound of bacon"}
# https://www.youtube.com/watch?v=rog8ou-ZepE
