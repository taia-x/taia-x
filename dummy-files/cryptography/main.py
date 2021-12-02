import sys
import argparse
import os
import hashlib
from zokrates_pycrypto import eddsa
from Crypto.PublicKey import ECC as ecc
from Crypto.Hash import SHA256
from Crypto.Signature import DSS


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
    save_file(key)
    return None


def save_file(key, dir_path="./keys"):
    i = 0
    if not os.path.exists(f"{dir_path}" + f"{i}"):
        os.mkdir(dir_path + f"{i}")
    else:

        while os.path.exists(f"{dir_path}" + f"{i}"):
            i = i + 1
        os.mkdir(f"{dir_path}" + f"{i}")

    with open(f"{dir_path}" + f"{i}/" + "p.pem", "wt") as f:
        # The key will be encoded in a PEM envelope (ASCII).
        f.write(key.export_key(format='PEM'))
    with open(f"{dir_path}" + f"{i}/" + "pbk.pem", "wt") as f:
        pbk = key.public_key()
        f.write(pbk.export_key(format="PEM"))
    print()


def hash_measurements(dir_path):
    hash_object = SHA256.new(data=b'First')
    # for file in os.listdir(dir_path):
    # with open(file, "rb", buffering=0) as f:


def sign(dir_path, file="p.pem"):
    # Instantiate a new signer object for the desired algorithm
    with open(dir_path + file, "rt") as f:
        key = ecc.import_key(f.read())
    # in bytes
    m = b'hi mom!'
    h = SHA256.new(m)

    # The signature generation is randomized and carried out according to FIPS 186-3
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(h)
    print(signature)


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
    path_test = "../test-measurements-sensorwise/2021-12-2-13-38-9/"
    hash_measurements(path_test)
    sign("./keys0/", "p.pem")
    # main()
