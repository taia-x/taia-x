import sys
import argparse
import os
import hashlib
import base58
from zokrates_pycrypto import eddsa
from Crypto.PublicKey import ECC as ecc
from Crypto.Hash import SHA256
from Crypto.Signature import DSS

BLOCK_SIZE = 65536  # Size of each read from the file


def keygen():
    sk = eddsa.PrivateKey.from_rand()
    pk = eddsa.PublicKey.from_private(sk)
    pk_hex = pk.p.compress().hex()
    sk_hex = hex(sk.fe.n)[2:]

    print("PrivateKey PublicKey", file=sys.stderr)
    print("{} {}".format(sk_hex, pk_hex))
    return sk, pk


def keygen2():
    # Use Elliptic Curve Cryptography for key generation
    # NIST P-256
    key = ecc.generate(curve='P-256')
    save_keys(key)
    return None


def save_keys(key, dir_path="./keys"):
    i = 0
    if not os.path.exists(f"{dir_path}" + f"{i}"):
        os.mkdir(dir_path + f"{i}")
    else:
        # Save in separate directories for each sensor
        while os.path.exists(f"{dir_path}" + f"{i}"):
            i = i + 1
        os.mkdir(f"{dir_path}" + f"{i}")

    with open(f"{dir_path}" + f"{i}/" + "p.pem", "wt") as f:
        # The key will be encoded in a PEM envelope (ASCII).
        f.write(key.export_key(format='PEM'))
    with open(f"{dir_path}" + f"{i}/" + "pvtDER.pem", "wt") as f:
        f.write(str(key.export_key(format='PEM', use_pkcs8=False)))
    with open(f"{dir_path}" + f"{i}/" + "pbk.pem", "wt") as f:
        pbk = key.public_key()
        f.write(pbk.export_key(format="PEM"))
    with open(f"{dir_path}" + f"{i}/" + "pbk58.pem", "wt") as f:
        pbk = key.public_key()
        pbk58 = base58.b58encode(pbk.export_key(format="DER"))
        f.write(str(pbk58))
    with open(f"{dir_path}" + f"{i}/" + "pbk.der", "wt") as f:
        pbk = key.public_key()
        pbk_der = pbk.export_key(format="DER")
        f.write(str(pbk_der))


def hash_measurements(file_path) -> bytes:
    sha256_obj = hashlib.sha256()
    with open(file_path, "rb", buffering=0) as f:
        fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
        while len(fb) > 0:  # While there is still data being read from the file
            sha256_obj.update(fb)  # Update the hash
            fb = f.read(BLOCK_SIZE)  # Read the next block from the file
        # print(sha256_obj.hexdigest())  # Get the hexadecimal digest of the hash
    return sha256_obj.digest()


def sign(file_path, pvk_path):
    # for file in os.listdir(dir_path):
    # Instantiate a new signer object for the desired algorithm
    with open(pvk_path, "rt") as f:
        key = ecc.import_key(f.read())
    file_digest = hash_measurements(file_path)
    file_digest58 = base58.b58encode(file_digest)
    print("file digest base 58", file_digest58)
    file_hash_obj = SHA256.new(file_digest)
    print("file digest", file_digest)
    print("file hash obj", file_hash_obj)
    # The signature generation is randomized and carried out according to FIPS 186-3
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(file_hash_obj)  # The signature as a *byte string*
    print("signature", signature)
    print("signature base 58", base58.b58encode(signature))
    return signature


def verify_signature(signature, msghash, pbk_path):
    pubkey = ecc.import_key(open(pbk_path).read())
    # print(pubkey)
    verifier = DSS.new(pubkey, 'fips-186-3')
    try:
        verifier.verify(msghash, signature)
        print("The message is authentic.")
    except ValueError:
        print("The message is not authentic")


def main():
    parser = argparse.ArgumentParser(description="command-line interface")
    subparsers = parser.add_subparsers(dest="subparser_name")

    keygen_parser = subparsers.add_parser(
        "keygen",
        help="Returns space separated hex-string for a random private/public keypair on BabyJubJub curve",
    )
    keygen_parser = subparsers.add_parser(
        "keygen2",
        help="generate a new ECC key",
    )

    args = parser.parse_args()
    subparser_name = args.subparser_name

    if subparser_name == "keygen":
        keygen()

    elif subparser_name == "keygen2":
        keygen2()

    else:
        raise NotImplementedError(
            "Sub-command not implemented: {}".format(subparser_name)
        )
    return None


if __name__ == "__main__":
    path_test = ""
    secret_key_path = ""
    pbk_key_path = ""

    try:
        if sys.stdin.isatty():
            main()
        else:
            # Verify the signature:
            file_digest = hash_measurements(path_test)
            h = SHA256.new(file_digest)
            verify_signature(sign(path_test, secret_key_path), h, pbk_key_path)
    except FileNotFoundError:
        print("Give a valid file and keypair path!")
