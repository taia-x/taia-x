const { MichelsonMap } = require("@taquito/taquito");
const { char2Bytes } = require("@taquito/utils");

const web3 = require("web3");

module.exports = async (Tezos) => {
  const empty_datasets = new MichelsonMap();
  const empty_dataset_ids = [];
  const empty_owners = new MichelsonMap();

  const market = {
    datasets: empty_datasets,
    datasetIds: empty_dataset_ids,
    nextDatasetId: 1,
    owners: empty_owners,
  };

  const empty_certs = new MichelsonMap();
  const metadata = new MichelsonMap();
  const token_metadata = new MichelsonMap();
  const empty_ledger = new MichelsonMap();
  const empty_operators = new MichelsonMap();
  const users = new MichelsonMap();

  // Set deployment account address as the only certifier
  users.set(
    {
      0: "tz1ggvpTMyxX5QVYqbpLVmNGCsgDpDyUMawq", // addresss of jon
      1: { certifier: {} }, // role
    },
    [["unit"]]
  );

  return {
    market: market,
    users: users,
    certificates: empty_certs,
    ledger: empty_ledger,
    operators: empty_operators,
    token_metadata: token_metadata,
  };
};
