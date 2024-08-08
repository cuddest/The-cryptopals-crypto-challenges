def repeating_xor(bin1, bin2):
    str1 = bin1.encode()
    str2 = bin2.encode()
    result = b""

    for i in range(len(str1)):
        result += bytes([str1[i] ^ str2[i % len(str2)]])

    return result


output = repeating_xor(
    "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal",
    "ICE",
)


print(output.hex())
"""
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
"""
