#if !FA2_TAIA_X_DEF_TOKEN
#define FA2_TAIA_X_DEF_TOKEN

#include "dataset_definition.mligo"
#include "marketplace_definition.mligo"
#include "user_definition.mligo"
#include "cert_definition.mligo"

#include "../tzip-12/lib/fa2_operator_lib.mligo"

type marketplace_storage = {
  datasets: datasets;
  datasetIds: token_id set;
  nextDatasetId: token_id;
  owners: owners;
}

type ledger = (token_id, address) big_map

type taia_x_storage = {
  market : marketplace_storage;
  certificates: cert_storage; 
  users: user_storage;
  ledger : ledger;
  operators : operator_storage;
  token_metadata: token_metadata_storage;
}

#endif
