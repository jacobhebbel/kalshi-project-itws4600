from misc.env import read_env

import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, ed25519, rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key

def load_private_key():

    file_path = read_env('kalshi_pem_path')
    with open(file_path, "rb") as key_file:
        return load_pem_private_key(key_file.read(), password=None)

def sign_request(private_key, timestamp: str, method: str, path: str) -> str:
    """
    Constructs the message string (timestamp + method + path) 
    and signs it using either Ed25519 or RSA-PSS.
    """
    
    # Message format: timestamp + uppercase_method + path (no query params)
    msg_string = f"{timestamp}{method.upper()}{path}"
    message_bytes = msg_string.encode("utf-8")

    if isinstance(private_key, ed25519.Ed25519PrivateKey):
        # Ed25519 signs the message directly
        signature_bytes = private_key.sign(message_bytes)
    
    elif isinstance(private_key, rsa.RSAPrivateKey):
        # RSA signs using RSA-PSS with SHA-256
        signature_bytes = private_key.sign(
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
    else:
        raise TypeError("Unsupported private key type.")

    return base64.b64encode(signature_bytes).decode("utf-8")

