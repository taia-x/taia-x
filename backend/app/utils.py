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

def get_tz_address(pbkey: str) -> bool:
    pbk = scrub_input(pbkey)
    pbk2 = base58_decode(pbk)
    pbh2 = public_key_hash(pbk2)
    return pbh2

def signature_verification(sig: str, pbkey: str, message: str) -> bool:
    pbk = scrub_input(pbkey)
    pbk2 = base58_decode(pbk)

    # verify signature to check authenticity of requester
    signature = scrub_input(sig)
    message = scrub_input(message)

    signature = base58_decode(signature)

    digest = pysodium.crypto_generichash(message)
    try:
        pysodium.crypto_sign_verify_detached(signature, digest, pbk2)
        print("Signature is valid!")
        return True
    except ValueError:
        return False