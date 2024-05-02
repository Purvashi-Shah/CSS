#include<stdio.h>

void encrypt(char message[], int key) {
    int i;
    char ch;
    for(i = 0; message[i] != '\0'; ++i){
        ch = message[i];
        if(ch >= 'a' && ch <= 'z'){
            ch = ((ch - 'a') * key) % 26 + 'a';
            message[i] = ch;
        }
        else if(ch >= 'A' && ch <= 'Z'){
            ch = ((ch - 'A') * key) % 26 + 'A';
            message[i] = ch;
        }
    }
    printf("Encrypted message: %s\n", message);
}

void decrypt(char message[], int key) {
    int i, inverse;
    char ch;
    // Calculate the multiplicative inverse of the key
    for (inverse = 1; inverse < 26; ++inverse) {
        if ((key * inverse) % 26 == 1) {
            break;
        }
    }
    for(i = 0; message[i] != '\0'; ++i){
        ch = message[i];
        if(ch >= 'a' && ch <= 'z'){
            ch = ((ch - 'a') * inverse) % 26 + 'a';
            message[i] = ch;
        }
        else if(ch >= 'A' && ch <= 'Z'){
            ch = ((ch - 'A') * inverse) % 26 + 'A';
            message[i] = ch;
        }
    }
    printf("Decrypted message: %s\n", message);
}

int main() {
    char message[100];
    int key;
    
    printf("Enter a message: ");
    fgets(message, sizeof(message), stdin);
    printf("Enter key (must be co-prime with 26): ");
    scanf("%d", &key);
    
    encrypt(message, key);
    decrypt(message, key);

    return 0;
}

---------------------
/tmp/wUC3yNacHQ.o
Enter a message: Hello
Enter key (must be co-prime with 26): 9
Encrypted message: Lkvvw

Decrypted message: Hello
