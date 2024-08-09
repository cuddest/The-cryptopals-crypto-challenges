def hamming_distance(str1, str2):
    str1_bytes = str1.encode()
    str2_bytes = str2.encode()
    max_len = max(len(str1_bytes), len(str2_bytes))
    str1_bytes = str1_bytes.ljust(max_len, b"\x00")
    str2_bytes = str2_bytes.ljust(max_len, b"\x00")
    hamming = 0
    for b1, b2 in zip(str1_bytes, str2_bytes):
        hamming += bin(b1 ^ b2).count("1")
    return hamming


print(hamming_distance("this is a test", "wokka wokka!!!"))
