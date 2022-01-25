##### **Install pymerkle**

`pip install pymerkle`

##### **Extract root hash of merkle-tree out of a given directory**
The root hash is then saved in the same directory as a .txt file

`python init_merkle.py root`

##### **Sign root hash**
`signature.py` signs the hashed root of the merkle tree and verifies the authenticity.
It also creates a signature.txt file with the Signature, 
Pubkey X-Point an Y-Point in a given curve and the Message in hex.


##### **Create Dummy-Files**
First create a directory and copy the path to the _directory_path_ 
variable inside the main.py file.