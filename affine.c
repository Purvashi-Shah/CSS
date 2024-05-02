#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ALPHABET_SIZE 26

int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int modInverse(int a, int m) {
    for (int x = 1; x < m; x++)
        if ((a * x) % m == 1)
            return x;
    return -1;
}

void affine_encrypt(char *plaintext, int a, int b) {
    int len = strlen(plaintext);
    for (int i = 0; i < len; i++) {
        if (plaintext[i] >= 'A' && plaintext[i] <= 'Z') {
            plaintext[i] = ((a * (plaintext[i] - 'A') + b) % ALPHABET_SIZE) + 'A';
        } else if (plaintext[i] >= 'a' && plaintext[i] <= 'z') {
            plaintext[i] = ((a * (plaintext[i] - 'a') + b) % ALPHABET_SIZE) + 'a';
        }
    }
}

void affine_decrypt(char *ciphertext, int a, int b) {
    int len = strlen(ciphertext);
    int a_inv = modInverse(a, ALPHABET_SIZE);
    for (int i = 0; i < len; i++) {
        if (ciphertext[i] >= 'A' && ciphertext[i] <= 'Z') {
            ciphertext[i] = (a_inv * (ciphertext[i] - 'A' - b + ALPHABET_SIZE)) % ALPHABET_SIZE + 'A';
        } else if (ciphertext[i] >= 'a' && ciphertext[i] <= 'z') {
            ciphertext[i] = (a_inv * (ciphertext[i] - 'a' - b + ALPHABET_SIZE)) % ALPHABET_SIZE + 'a';
        }
    }
}

int main() {
    char plaintext[100], ciphertext[100];
    int a, b, choice;

    printf("Enter the value of 'a' (must be co-prime with 26): ");
    scanf("%d", &a);

    if (gcd(a, ALPHABET_SIZE) != 1) {
        printf("Error: 'a' must be co-prime with 26.\n");
        return 1;
    }

    printf("Enter the value of 'b': ");
    scanf("%d", &b);

    printf("Enter the plaintext: ");
    scanf(" %[^\n]s", plaintext);

    printf("Choose operation:\n");
    printf("1. Encryption\n");
    printf("2. Decryption\n");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            affine_encrypt(plaintext, a, b);
            printf("Encrypted text: %s\n", plaintext);
            break;
        case 2:
            printf("Enter the ciphertext: ");
            scanf(" %[^\n]s", ciphertext);
            affine_decrypt(ciphertext, a, b);
            printf("Decrypted text: %s\n", ciphertext);
            break;
        default:
            printf("Invalid choice.\n");
    }

    return 0;
}
-----------------------------
Suppose we choose 
a=5 and b=8.

Encryption:Input:
Plain text: "Hello"

Output:
Encrypted text: "Czggv"

Decryption:Input:
Cipher text: "Czggv"

Output:
Decrypted text: "Hello"
