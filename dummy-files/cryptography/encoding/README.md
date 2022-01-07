
### **Requirements**

_Windows_

I recommend using WSL for Windows because it gets buggy when trying to install it from scratch.


_Linux_

`$ sudo apt install libsodium-dev libsecp256k1-dev libgmp-dev`

### **Installation**
`$ pip install pytezos`

Try installing these libraries if necessary: 
base58check
base58
pysodium

### **Get account from faucet**

Get it from [here](https://teztnets.xyz/hangzhounet-faucet). Follow the instructions and activate it. 
Then save it in the same directory as _signature_v2.py_. 

_signature_v2_ contains the base58 encoding-, keypair generation-, secret exponent- ( from mnemonic),
public key hash- and sign -function.

Run:

`python3 signature_v2.py`

Only for test purposes the secret_key will be exposed! Comment it out otherwise.
Check the created _./keys_sig/keys_sig.txt_ file.
