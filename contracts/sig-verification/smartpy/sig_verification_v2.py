import smartpy as sp


class SignatureProcess(sp.Contract):
    def __init__(self, pbk, message, owner):
        self.init(public_key=pbk, raw_message=message, owner=owner, counter=0, m={})

    @sp.entry_point
    def verifySig1(self, params):
        # c.data:Retrieve contract storage.
        k = params.pbk
        s = params.provider_sig
        m = params.message_packed

        sp.verify(sp.check_signature(k, s, m), message="FAILED")
        self.data.counter = self.data.counter + 1

    @sp.entry_point
    def verifySig2(self, k, s, m):
        # First set types
        sp.set_type(k, sp.TKey)
        sp.set_type(s, sp.TSignature)
        sp.set_type(m, sp.TString)
        # s = sp.signature(provider_sig_unp)
        # m_u = params.message_unp
        # m_p = sp.pack(m_u)
        # k_p = self.data.public_key
        m_p = sp.pack(m)
        sp.verify(sp.check_signature(k, s, m_p))
        self.data.counter = self.data.counter + 1

    @sp.entry_point
    def verifySig3(self, params):
        # tests whether a certifier added a certificate for a dataset that is being bought by a consumer.
        k = params.pbk
        s = params.provider_sig
        m_root = self.data.m[k]

        sp.verify(sp.check_signature(k, s, m_root), message="FAILED")
        self.data.counter = self.data.counter + 1

    @sp.entry_point
    def save_cert(self, pbk, root_hash):
        # save certificate
        sp.set_type(pbk, sp.TKey)
        sp.set_type(root_hash, sp.TBytes)
        sp.verify(sp.source == self.data.owner, message="Condition is false")  # only certifier can call function
        # self.data.m = sp.update_map(self.data.m, pbk, sp.some(root_hash))
        self.data.m[pbk] = root_hash
        a = sp.len(self.data.m)  # remove in later versions
        self.data.counter = self.data.counter + a


# Tests
@sp.add_test(name="Save Data")
def test():
    # Create a scenario
    scenario = sp.test_scenario()
    scenario.h3("Save public key and raw message")

    # It produces an object with the following properties: address, public_key_hash, public_key, secret_key
    # Creates a deterministic key-pair from a seed string
    nikola = sp.test_account("Provider1")
    benz = sp.test_account("Provider2")
    ferdinand = sp.test_account("Provider3")
    gottlieb = sp.test_account("Provider4")
    henry = sp.test_account("Provider5")
    owner_adress = sp.address("tz1PTp1gCGTUVKJ4YZ6mQBRpfovR5m6TmTee")

    # Instantiate a contract
    dataset_root = "hashed root hash"
    c1 = SignatureProcess(nikola.public_key, dataset_root, owner_adress)
    # Add the contract to the scenario
    scenario += c1

    # Let's build a successful call:
    scenario.h3("Successful Call")
    dataset_root_nikola = "hashed root hash"
    message_packed = sp.pack(dataset_root_nikola)
    sig_from_provider = sp.make_signature(secret_key=nikola.secret_key, message=message_packed,
                                          message_format="Raw")
    c1.verifySig1(pbk=nikola.public_key, provider_sig=sig_from_provider,
                  message_packed=message_packed).run(valid=True)

    # Test pack function inside the smart contract:
    scenario.h3("Test function inside the smart contract")
    dataset_root_benz = "hashed root hash2"
    message_packed2 = sp.pack(dataset_root_benz)
    sig_from_provider = sp.make_signature(secret_key=benz.secret_key, message=message_packed2,
                                          message_format="Raw")
    c1.verifySig2(k=benz.public_key, s=sig_from_provider,
                  m=dataset_root_benz).run(valid=True)

    # Packing data, Return an object of type sp.TBytes.
    # Conversion from string to bytes is not evaluated at runtime
    # because no such instruction exists in Michelson
    # It is only evaluated during compilation.

    scenario.h3("Save hash-pbk pair resembling certificate!")
    message_packed3 = sp.pack("test")
    c1.save_cert(pbk=ferdinand.public_key, root_hash=message_packed3).run(valid=False)

    scenario.h3("Save hash-pbk pair resembling certificate!")
    message_packed4 = sp.pack("test")
    c1.save_cert(pbk=gottlieb.public_key, root_hash=message_packed4).run(valid=False)

    scenario.h3("Check sig3")
    sig3 = sp.make_signature(secret_key=ferdinand.secret_key, message=message_packed3,
                             message_format="Raw")
    c1.verifySig3(pbk=ferdinand.public_key, provider_sig=sig3).run(valid=True)

    scenario.simulation(c1)


sp.add_compilation_target("my_contract_compiled",
                          SignatureProcess(sp.key("edsk3JRacRgUiZY7ciHsqRbPEqBcHASQpvoHoUAvmB1uq7Fu5RHzam"), "asd",
                                           sp.address("tz1PTp1gCGTUVKJ4YZ6mQBRpfovR5m6TmTee")))
