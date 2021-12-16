import smartpy as sp


class SignatureProcess(sp.Contract):
    def __init__(self, pbk, message):
        self.init(public_key=pbk, raw_message=message, counter=0)

    @sp.entry_point
    def verifySig(self, params):
        # c.data:Retrieve contract storage.
        k = params.pbk
        s = params.provider_sig
        m = params.message_packed
        sp.verify(sp.check_signature(k, s, m))
        self.data.counter = self.data.counter + 1


# Tests
@sp.add_test(name="Save Data")
def test():
    # Create a scenario
    scenario = sp.test_scenario()
    scenario.h1("Save public key and raw message")

    # It produces an object with the following properties: address, public_key_hash, public_key, secret_key
    # Creates a deterministic key-pair from a seed string 
    nikola = sp.test_account("Provider1")
    benz = sp.test_account("Provider2")
    ferdinand = sp.test_account("Provider3")
    gottlieb = sp.test_account("Provider4")
    henry = sp.test_account("Provider5")

    # Instantiate a contract
    dataset_root = "hashed root hash"
    c1 = SignatureProcess(nikola.public_key, dataset_root)
    # Add the contract to the scenario
    scenario += c1

    # Let's build a successful call:
    scenario.h2("Successful Call")
    dataset_root_nikola = "hashed root hash"
    message_packed = sp.pack(dataset_root_nikola)
    sig_from_provider = sp.make_signature(secret_key=nikola.secret_key, message=message_packed,
                                          message_format="Raw")
    c1.verifySig(pbk=nikola.public_key, provider_sig=sig_from_provider,
                 message_packed=message_packed).run(valid=True)

    # Packing data, Return an object of type sp.TBytes. 
    # Conversion from string to bytes is not evaluated at runtime 
    # because no such instruction exists in Michelson
    # It is only evaluated during compilation.

    # nikola_message_packed = sp.pack(nikola.raw_message)
    # nikola_sig = sp.make_signature(secret_key = nikola.secret_key,
    # message = nikola_message_packed,
    # message_format = "Raw")
    scenario.simulation(c1)


sp.add_compilation_target("my_contract_compiled",
                          SignatureProcess(sp.key("edpku5ZuqYibUQrAhove2B1bZDYCQyDRTGGa1ZwtZYiJ6nvJh4GXcE"), "message"))
