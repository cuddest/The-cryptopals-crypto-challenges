MOD = 256

def KSA(key):
    key_length = len(key)
    S = list(range(MOD))  
    j = 0
    for i in range(MOD):
        j = (j + S[i] + key[i % key_length]) % MOD
        S[i], S[j] = S[j], S[i]  
    return S
    
def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % MOD
        j = (j + S[i]) % MOD
        S[i], S[j] = S[j], S[i]  
        K = S[(S[i] + S[j]) % MOD]
        yield K 

def get_keystream(key):
    S = KSA(key)
    return PRGA(S)

def encrypt(key, text):
    if isinstance(key, str):
        key_bytes = key.encode('utf-8')
    else:
        key_bytes = key

    if isinstance(text, str):
        text_bytes = text.encode('utf-8')
    else:
        text_bytes = text
    key_list = list(key_bytes)
    keystream = get_keystream(key_list)
    cipher_bytes = bytes([b ^ next(keystream) for b in text_bytes])
    return cipher_bytes.hex().upper()

def decrypt(key, ciphertext):
    ciphertext_bytes = bytes.fromhex(ciphertext)

    if isinstance(key, str):
        key_bytes = key.encode('utf-8')
    else:
        key_bytes = key

    key_list = list(key_bytes)
    keystream = get_keystream(key_list)
    
    plain_bytes = bytes([b ^ next(keystream) for b in ciphertext_bytes])
    return plain_bytes.decode('utf-8')

def main():
    key = 'random very random randomy key'  
    plaintext = 'normal very normal normaly plaintext'  
    ciphertext = encrypt(key, plaintext)
    print('plaintext:', plaintext)
    print('ciphertext:', ciphertext)

    ciphertext_fixed = "0AF4976455BDE99221AD90DBD73B74037D2579DE03EB49358F0DE38C34A15F890E6E1771"
    decrypted = decrypt(key, ciphertext_fixed)
    print('decrypted:', decrypted)

    if plaintext == decrypted:
        print('\nRC4ing goes brrrrr')
    else:
        print('Something is wrong mhmmmmmm :/')

if __name__ == '__main__':
    main()
