import pysodium

from pyblake2 import blake2b
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .encoding import scrub_input, base58_decode, base58_encode


class Purchase(BaseModel):
    nft_id: int
    buyer: str


def public_key_hash(public_point) -> str:
    """Creates base58 encoded public key hash for this key.

      :returns: the public key hash for this key
    """
    pkh = blake2b(data=public_point, digest_size=20).digest()
    prefix = b'tz1'
    return base58_encode(pkh, prefix).decode()


def signature_verification(nft_id: str, sig: str, pbkey: str, db: Session) -> bool:
    pbk = scrub_input(pbkey)
    pbk2 = base58_decode(pbk)
    pbh2 = public_key_hash(pbk2)
    pbh_of_buyer = db.query(Purchase).get(nft_id)  # to be called from database
    print("Check matching onchain PBK from buyer with consumer pbk..")
    if pbh2 == pbh_of_buyer:
        print("Verified account!")
    else:
        print("Not the same account!")
        # Change to return, but for test purposes, pass
        return False

    # verify signature to check authenticity of requester
    signature = scrub_input(sig)
    message = scrub_input(nft_id)

    signature = base58_decode(signature)

    digest = pysodium.crypto_generichash(message)
    try:
        pysodium.crypto_sign_verify_detached(signature, digest, pbk2)
        print("Signature is valid!")
        return True
    except ValueError:
        return False
        # raise ValueError('Signature is invalid.')
