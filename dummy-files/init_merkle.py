import os
import sys
import argparse
from cryptography.main import hash_measurements as Hash
from cryptography.merkletree import merkle
from os import listdir


def root(dir_p, root_type="hex"):
    dir_list = listdir(dir_p)
    vehicle_m_tree = merkle.initMerkleTree()
    for ind in dir_list:
        h = Hash(dir_p + ind)
        vehicle_m_tree.update(record=h)
    # print(vehicle_m_tree.rootHash)
    if root_type == "bytes":
        return vehicle_m_tree.rootHash
    elif root_type == "hex":
        return vehicle_m_tree.rootHash.hex()


def main():
    parser = argparse.ArgumentParser(description="command-line interface")
    subparsers = parser.add_subparsers(dest="subparser_name")

    keygen_parser = subparsers.add_parser(
        "root",
        help="Returns Merkle root from the directory",
    )

    args = parser.parse_args()
    subparser_name = args.subparser_name

    if subparser_name == "root":
        directory_path = input("\nDir Path: (format is (...)/test-measurements/(...)/ )\n")
        root_hash = root(directory_path, "hex")
        if not os.path.exists(f"{directory_path}roothash.txt"):
            with open(f"{directory_path}roothash.txt", "w") as f:
                f.write(root_hash)

    else:
        raise NotImplementedError(
            "Sub-command not implemented: {}".format(subparser_name)
        )
    return None


if __name__ == "__main__":
    if sys.stdin.isatty():
        main()
    else:
        dir_path = "./"
        dir_l = listdir(dir_path)
        r = root(dir_path, "hex")
        print("Root of the merkle tree in hex: ", r)
        if not os.path.exists(f"{dir_path}roothash.txt"):
            with open(f"{dir_path}roothash.txt", "w") as outfile:
                outfile.write(r)
