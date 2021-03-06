import base58check
import base58
import hashlib
import os
import pysodium
import json
from fastecdsa.ecdsa import sign
from fastecdsa.encoding.util import int_to_bytes, bytes_to_int
from pyblake2 import blake2b
from mnemonic import Mnemonic

from encoding import scrub_input, base58_decode, base58_encode

ed25519_public_key_hash_prefix = b"\006\161\159"  # tz1(36)
ed25519_public_key_prefix = b"\013\015\037\217"  # edpk(54)
ed25519_seed = b"\013\015\058\007"  # edsk(54)
ed25519_secret_key = b"\043\246\078\007"  # edsk(98)
ed25519_signature = b"\009\245\205\134\018"  # edsig(99)

p256_public_key_hash_prefix = b"\006\161\164"  # tz3(36)
p256_secret_key = b"\016\081\238\189"  # p2sk(54)
p256_public_key = b"\003\178\139\127"  # p2pk(55)
p256_signature = b"\054\240\044\052"  # p2sig(98)


def blake2b_32(v=b''):
    return blake2b(scrub_input(v), digest_size=32)


def keypair(path_to_file):
    with open(path_to_file, 'r') as f:
        data = json.load(f)
        mnemonic = data["mnemonic"]
        password = data.get('password', '')
        email = data.get('email', '')

    if isinstance(mnemonic, list):
        mnemonic = ' '.join(mnemonic)
    seed = Mnemonic.to_seed(mnemonic, passphrase=email + password)
    public_point, secret_exponent = pysodium.crypto_sign_seed_keypair(seed=seed[:32])
    prefix_s = b'ed' + b'sk'  # ed25519 curve prefix
    prefix_p = b'ed' + b'pk'  # ed25519 curve prefix
    private_key = pysodium.crypto_sign_sk_to_seed(secret_exponent)
    private_key58 = base58_encode(private_key, prefix_s).decode()  # Encode:
    public_key58 = base58_encode(public_point, prefix_p).decode()
    return private_key58, public_key58


def secret_exponent(path_to_file):
    with open(path_to_file, 'r') as f:
        data = json.load(f)
        mnemonic = data["mnemonic"]
        password = data.get('password', '')
        email = data.get('email', '')

    if isinstance(mnemonic, list):
        mnemonic = ' '.join(mnemonic)
    seed = Mnemonic.to_seed(mnemonic, passphrase=email + password)
    public_point, secret_exponent = pysodium.crypto_sign_seed_keypair(seed=seed[:32])
    return public_point, secret_exponent


def base58encoding(prefix: bytes, key_bytes: bytes):
    message = prefix + key_bytes
    m = hashlib.sha256()
    m.update(message)
    print("m =", m.hexdigest())
    m2 = hashlib.sha256()
    m2.update(m.digest())
    print("m2=", m2.hexdigest())
    final_message = message + m2.digest()[:4]
    print("m2 digest [:4]= ", m2.digest()[:4].hex())
    encoded_final_message = base58.b58encode(final_message)

    return encoded_final_message


def public_key_hash(public_point) -> str:
    """Creates base58 encoded public key hash for this key.

    :returns: the public key hash for this key
    """
    pkh = blake2b(data=public_point, digest_size=20).digest()
    prefix = b'tz1'
    return base58_encode(pkh, prefix).decode()


def sign(message, file_path):
    """Sign a raw sequence of bytes.

    :param message: sequence of bytes, raw format or hexadecimal notation
    :returns: signature in base58 encoding
    """
    encoded_message = scrub_input(message)

    # Ed25519
    digest = pysodium.crypto_generichash(encoded_message)
    signature = pysodium.crypto_sign_detached(digest, secret_exponent(file_path)[1])

    prefix = b'ed' + b'sig'
    return base58_encode(signature, prefix).decode()


def verify_sig(signature, message, public_key):
    """
    Verify signature, raise exception if it is not valid
    :param message: sequance of bytes, raw format or hexadecimal notation
    :param signature: a signature in base58 encoding
    """
    signature = scrub_input(signature)
    message = scrub_input(message)
    pbk = scrub_input(public_key)

    signature = base58_decode(signature)
    pbk = base58_decode(pbk)

    # Ed25519
    digest = pysodium.crypto_generichash(message)
    try:
        pysodium.crypto_sign_verify_detached(signature, digest, pbk)
    except ValueError:
        raise ValueError('Signature is invalid.')
    print("Signature is valid!")

    return None


def save_as_txt(faucet_path: str, message: str):
    os.mkdir("./keys_sig/")
    keypair_temp = keypair(faucet_path)
    secret_key = keypair_temp[0]
    public_key = keypair_temp[1]
    with open(f"./keys_sig/" + "keys_sig.txt", "wt") as f:
        f.write("Secret key: ")
        f.write(secret_key)
        f.write("\nPublic key: ")
        f.write(public_key)
        f.write("\nPublic key hash: ")
        f.write(public_key_hash(secret_exponent(faucet_path)[0]))
        f.write(f"\nMessage in hex: ")
        f.write(message.encode().hex())
        f.write("\nSignature: ")
        f.write(sign(message=message, file_path=faucet_path))


print("secret key: ", keypair("./hangzhounet.json")[0])
print("public key: ", keypair("./hangzhounet.json")[1])
print("public key hash: ", public_key_hash(secret_exponent("./hangzhounet.json")[0]))
print("sig: ", sign("Hi :D", "./hangzhounet.json"))

save_as_txt("./hangzhounet2.json", "Hi :D")
