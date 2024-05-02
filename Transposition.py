def encrypt_transposition(plain_text):
    text_length = len(plain_text)
    num_columns = 3
    num_rows = -(-text_length // num_columns)
    transposition_grid = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]
    index = 0
    for col in range(num_columns):
        for row in range(num_rows):
            if index < text_length:
                transposition_grid[row][col] = plain_text[index]
                index += 1
    encrypted_text = ''.join(''.join(row) for row in transposition_grid)
    return encrypted_text

def decrypt_transposition(encrypted_text):
    text_length = len(encrypted_text)
    num_columns = 3
    num_rows = -(-text_length // num_columns)
    transposition_grid = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]
    index = 0
    for row in range(num_rows):
        for col in range(num_columns):
            if index < text_length:
                transposition_grid[row][col] = encrypted_text[index]
                index += 1
    decrypted_text = ''.join(''.join(row) for row in zip(*transposition_grid))
    return decrypted_text

plain_text = input("Enter the value: ")
encrypted_text = encrypt_transposition(plain_text)
print("Encrypted:", encrypted_text)
decrypted_text = decrypt_transposition(encrypted_text)
print("Decrypted:", decrypted_text)





A transposition cipher is a cryptographic technique that involves rearranging the characters in a message to conceal its meaning. Unlike substitution ciphers, which replace each letter with another according to a fixed system, transposition ciphers manipulate the order of the characters while keeping the characters themselves unchanged.

One of the simplest transposition ciphers is the columnar transposition cipher. In this method, the plaintext is written out in rows of a fixed length, and then the columns are rearranged according to a certain permutation. The resulting ciphertext consists of the characters read out column by column.

For example, consider the plaintext "HELLO WORLD" and a permutation of 2-1-3 for a three-column arrangement:

```
H E L
L O  
W O R
L D
```

After rearranging the columns according to the permutation, the ciphertext would be "ELOLWOHLRO D".

Transposition ciphers offer a different level of security compared to substitution ciphers. While they do not alter the characters themselves, they obscure the original message by rearranging them. Breaking transposition ciphers typically involves finding the correct permutation used to rearrange the columns or rows.

One approach to breaking transposition ciphers is through brute force, where all possible permutations are tested until the correct one is found. However, this method becomes computationally impractical for longer messages or larger key spaces.

Another method for breaking transposition ciphers is through frequency analysis or other statistical techniques applied to the ciphertext. While transposition ciphers do not directly alter the frequency distribution of characters like substitution ciphers do, certain patterns may still emerge depending on the specific transposition method used.

Despite their vulnerabilities, transposition ciphers have been used historically and continue to be studied in cryptography. They serve as an important concept in understanding cryptographic principles and are often combined with other techniques to create more secure encryption methods. Additionally, transposition ciphers are valuable for educational purposes, helping individuals learn about encryption and decryption techniques and the importance of key management in cryptography.

