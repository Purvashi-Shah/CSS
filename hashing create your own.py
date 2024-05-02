from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization

# Function to perform a simple hash (not cryptographically secure)
def simple_hash(message):
    hash_value = 0
    for char in message:
        # Add the ASCII value of the character multiplied by its position
        hash_value += (hash_value << 3) + ord(char)
    # Use a mask to ensure the hash is within a specific range, for example, a 32-bit integer
    return hash_value & 0xFFFFFFFF

# Test the simple hash function with the user's name
test_message = "Hello World, AV!"
hash_result = simple_hash(test_message)

# Generate private and public keys for RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Sign a message using RSA
def sign_message(message, private_key):
    message = message.encode('utf-8')
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# Verify RSA signature
def verify_signature(message, signature, public_key):
    message = message.encode('utf-8')
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False

# Create a signature for the test message
signature = sign_message(test_message, private_key)

# Now verify the signature
verification_result = verify_signature(test_message, signature, public_key)

# To output in terminal-like format, we will print the results
print(f"Hash result: {hash_result}")
print(f"Signature: {signature}")
print(f"Verification result: {verification_result}")

# Returning values just for the notebook output cell, this line can be removed for terminal output.
hash_result, signature, verification_result

