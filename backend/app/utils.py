import pysodium

from pyblake2 import blake2b
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .encoding import scrub_input, base58_decode, base58_encode


class Purchase(BaseModel):
  nft_id : int
  buyer : str


def public_key_hash(public_point) -> str:
    """Creates base58 encoded public key hash for this key.

    :returns: the public key hash for this key
    """
    pkh = blake2b(data=public_point, digest_size=20).digest()
    prefix = b'tz1'
    return base58_encode(pkh, prefix).decode()

# verify signature to check authenticity of requester
def signature_verification(nft_id: str, sig: str, pbkey: str) -> str:
    try:
        pbk = scrub_input(pbkey)
        pbk2 = base58_decode(pbk)
        signature = scrub_input(sig)
        message = scrub_input(nft_id)

        signature = base58_decode(signature)
        digest = pysodium.crypto_generichash(message)   
        pysodium.crypto_sign_verify_detached(signature, digest, pbk2)
        
        print("Signature is valid!")
        return public_key_hash(pbk2)
    
    except ValueError:
        raise ValueError