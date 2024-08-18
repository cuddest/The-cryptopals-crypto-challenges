from xor_brute_force import xor_brute_force


def hamming_distance(str1, str2):
    if not isinstance(str1, bytes) or not isinstance(str2, bytes):
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
with open("Break_repeating_key_XOR.txt", "r") as file:
    str1 = file.read()


def find_key_size(str1):
    best_avg = 0
    avg = 0
    start = 0
    end = start + keylength
    results = []
    for i in range(2, 40):
        while end + i <= len(str1):
            chunk1 = str1[start:end]
            chunk2 = str1[start + i : end + i]
            normalized_hamming_distance = hamming_distance(chunk1, chunk2) / i
            results.append(normalized_hamming_distance)
            avg = sum(results) / len(results)
            start = end + i
            end = start + i
            results = []
        if avg < best_avg:
            best_avg = avg
            best_key = i
    return {"best_avg": best_avg, "best_key": best_key}


def blocks_of_keysize_length(str1):
    best_key = find_key_size(str1)["best_key"]
    blocks = []
    for i in range(0, len(str1), best_key):
        blocks.append(str1[i : i + best_key])
    return blocks


def transpose(blocks):
    best_key = find_key_size(str1)["best_key"]
    transposed = []
    word = ""
    for j in range(best_key):
        word = ""
        for i in range(len(blocks)):
            k = blocks[i][j]
            word = word + k
        transposed.append(word)

    return transposed
