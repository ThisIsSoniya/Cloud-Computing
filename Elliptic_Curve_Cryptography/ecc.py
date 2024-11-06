from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
 
# Generate ECC private key using SECP256R1 curve
private_key = ec.generate_private_key(ec.SECP256R1())
 
# Generate public key from the private key
public_key = private_key.public_key()
 
# Serialize the public key to PEM format
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
 
print("Public Key in PEM format:\n", public_pem.decode())
 
# Take user input for the message to be signed
message = input("Enter a message to be signed: ").encode()
 
# Sign the message using the private key and ECDSA with SHA-256
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)
 
print("Signature:", signature)
 
# Verify the signature using the public key
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("Signature is valid!")
except Exception as e:
    print("Signature verification failed.", e)
