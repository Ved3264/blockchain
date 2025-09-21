import hashlib
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed


def sha256_hash(message: str) -> str:
    """Generate SHA-256 hash of input message."""
    return hashlib.sha256(message.encode()).hexdigest()


def generate_key_pair():
    """Generate RSA public–private key pair."""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key


def sign_message(private_key, message: str) -> bytes:
    """Sign message using private key."""
    message_bytes = message.encode()
    signature = private_key.sign(
        message_bytes,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256(),
    )
    return signature


def verify_signature(public_key, message: str, signature: bytes) -> bool:
    """Verify digital signature with public key."""
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )
        return True
    except Exception:
        return False
