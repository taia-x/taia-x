const { MichelsonMap } = require("@taquito/taquito");
const { char2Bytes } = require("@taquito/utils");

const web3 = require("web3");

module.exports = async (Tezos) => {
  const admin = await Tezos.signer.publicKeyHash();
  const empty_datasets = new MichelsonMap();
  const empty_sales = [];
  const empty_dataset_ids = [];
  const empty_owners = new MichelsonMap();
  const empty_users = new MichelsonMap();

  const market = {
    admin: admin,
    sales: empty_sales,
    datasets: empty_datasets,
    datasetIds: empty_dataset_ids,
    nextDatasetId: 0,
    owners: empty_owners,
  };

  const metadata = new MichelsonMap();
  const token_info = new MichelsonMap();
  const token_metadata = new MichelsonMap();
  const empty_ledger = new MichelsonMap();
  const empty_operators = new MichelsonMap();

  // Set TZIP-16 contract metadata, with a JSON Blob
  // metadata.set(
  //   "",
  //   char2Bytes("ipfs://QmfGSjEWPwqZnZzpYGRrFu2UcmTHSuFUz3Jb98qL4pJ321")
  // );

  // Set TZIP-16 token metadata with a JSON Blob
  // token_info.set(
  //     "", web3.utils.asciiToHex("https://ipfs.io/ipfs/QmZKJKce6Y9yyuPvatGZuqsvY3dYd6TH6qt9AsTW22xtgq").slice(2)
  // );

  // Set TZIP-12 token metadata, in the token_metadata big map
  // token_info.set(
  //     "symbol", web3.utils.asciiToHex("TLD").slice(2)
  // );
  // token_info.set(
  //     "name", web3.utils.asciiToHex("Tezosdataset").slice(2)
  // );
  // token_info.set(
  //     "decimals", web3.utils.asciiToHex("0").slice(2)
  // );
  // token_info.set(
  //     "thumbnailUri", web3.utils.asciiToHex("https://tezosdataset.io/logo512.png").slice(2)
  // );

  // token_metadata.set(
  //     1, {
  //     token_info: token_info,
  //     token_id: 1
  // }
  // );

  return {
    market: market,
    users: empty_users,
    ledger: empty_ledger,
    operators: empty_operators,
    metadata: metadata,
    token_metadata: token_metadata,
  };
};
