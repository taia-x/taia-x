#if !DATASET
#define DATASET

#include "interface.ligo"

function mint(const hash : string; var store : store) : return is
  block {
    const newToken : token = record[hash = hash];
    const newDataset : big_map(address, token) = Big_map.update(Tezos.sender, Some(newToken), store.datasets);
  } with ((nil : list (operation)), store with record [datasets = newDataset;]);

#endif