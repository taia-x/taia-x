#if !DATASET
#define DATASET

#include "interface.mligo"

let mint (new_token, store : token * store) : return = 
    let datasets : (address, token) big_map = Big_map.update Tezos.sender (Some new_token) store.datasets in
    ([] : operation list), { store with datasets = datasets; }  
  
#endif