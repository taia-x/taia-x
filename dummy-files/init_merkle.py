import sys
import argparse
from cryptography.main import hash_measurements as Hash
from cryptography.merkletree import merkle
from os import listdir


def root(dir_p) -> bytes:
    for ind in dir_l:
        h = Hash(dir_p + ind)
        vehicle_m_tree.update(record=h)
    # print(vehicle_m_tree.rootHash)
    return vehicle_m_tree.rootHash


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
        directory_path = input("\nDir Path:\n")
        root_hash = root(directory_path)
        print(root_hash)
    else:
        raise NotImplementedError(
            "Sub-command not implemented: {}".format(subparser_name)
        )
    return None


if __name__ == "__main__":
    vehicle_m_tree = merkle.initMerkleTree()
    dir_path = "./test-measurements-sensorwise/2021-12-2-13-38-9/"
    dir_l = listdir(dir_path)
    if sys.stdin.isatty():
        main()
    else:
        root(dir_path)
