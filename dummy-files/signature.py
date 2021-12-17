import os
from os import listdir
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS
from init_merkle import root
from Crypto.Util.asn1 import DerSequence
from Crypto.Math.Numbers import Integer


def sign(root_hash, pvk_path):
    # for file in os.listdir(dir_path):
    # Instantiate a new signer object for the desired algorithm
    with open(pvk_path, "rt") as f:
        key = ECC.import_key(f.read())
    # print("Curve", key._curve, "\n\n")
    file_hash_obj = SHA256.new(root_hash)
    # The signature generation is randomized and carried out according to FIPS 186-3
    signer = DSS.new(key, 'fips-186-3', encoding='der')
    signature = signer.sign(file_hash_obj)
    print(signature.hex())
    return signature


def verify_signature(signature, msghash, pbk_path):
    pubkey = ECC.import_key(open(pbk_path).read())
    verifier = DSS.new(pubkey, 'fips-186-3', encoding='der')
    der_seq = DerSequence().decode(signature, strict=True)
    # Extra cryptographic information:
    print("from pubkey:\n", pubkey.public_key())
    r_prime, s_prime = Integer(der_seq[0]), Integer(der_seq[1])
    try:
        verifier.verify(msghash, signature)
        print("The message is authentic.")
        os.mkdir("./signature_file/")
        msghash_hex = msghash.hexdigest()
        with open(f"./signature_file/" + "signature.txt", "wt") as f:
            # The key will be encoded in a PEM envelope (ASCII).
            f.write("Signature: ")
            f.write(signature.hex())
            f.write("\nPubkey: ")
            f.write(pubkey.public_key())
            f.write("\nMessage hex: ")
            f.write(msghash_hex)
    except ValueError:
        print("The message is not authentic")


if __name__ == "__main__":
    key_path = "./cryptography/keys0/p.pem"
    pbk_key_path = "./cryptography/keys0/pbk.pem"

    try:
        dirpath = "./test-measurements/2021-12-17-1-8-27/"
        dir_l = listdir(dirpath)
        root_hash = root(dirpath, root_type="bytes")
        h = SHA256.new(root_hash)
        # Verify the signature:
        verify_signature(sign(root_hash, key_path), h, pbk_key_path)
    except FileNotFoundError:
        print("Give a valid file and keypair path!")
