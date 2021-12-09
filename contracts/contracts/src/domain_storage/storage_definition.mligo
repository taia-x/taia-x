#if !FA2_TAIA_X_DEF_TOKEN
#define FA2_TAIA_X_DEF_TOKEN

#include "dataset_definition.mligo"
#include "marketplace_definition.mligo"
#include "../tzip-12/lib/fa2_operator_lib.mligo"
#include "../user_manager/user_manager_role_lib.mligo"

type marketplace_storage = {
  //  admin: address;
  sales: sale set;
  datasets: datasets;
  datasetIds: token_id set;
  nextDatasetId: token_id;
  owners: owners;
}

type ledger = (token_id, address) big_map

type nft_token_storage = {
  market : marketplace_storage;
  users: user_storage;
  ledger : ledger;
  operators : operator_storage;
  metadata: contract_metadata;
  token_metadata: token_metadata_storage;
}

#endif
