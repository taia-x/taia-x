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
    nextDatasetId: 0,
    owners: empty_owners,
  };

  const empty_users = new MichelsonMap();
  const empty_certs = new MichelsonMap();
  const metadata = new MichelsonMap();
  const token_metadata = new MichelsonMap();
  const empty_ledger = new MichelsonMap();
  const empty_operators = new MichelsonMap();

  return {
    market: market,
    users: empty_users,
    certificates: empty_certs,
    ledger: empty_ledger,
    operators: empty_operators,
    token_metadata: token_metadata,
  };
};
