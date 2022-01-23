from pymerkle import MerkleTree


def initMerkleTree(*args, hash_type='sha256'):
    """
    The .raw_bytes attribute refers to the tree’s ability of consuming arbitrary binary data,
    which is the default choice (True).
    If False, the tree will only accept byte sequences falling under its configured encoding type.
    """
    m_tree = MerkleTree(*args, hash_type=hash_type, encoding='utf-8', raw_bytes=True, security=True)
    return m_tree
