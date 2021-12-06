#if !MAIN
#define MAIN

#include "interface.mligo"
#include "role.mligo"
#include "dataset.mligo"


type action =
    | Mint of token
    | MakeCertifier 
    | MakeProvider 
    | MakeConsumer
    | RemoveRole 

let main (action, store : action * store) : return =
    match action with
    | Mint t -> mint(t, store)
    | MakeCertifier -> makeCertifier(store)
    | MakeProvider -> makeProvider(store)
    | MakeConsumer -> makeConsumer(store)
    | RemoveRole -> removeRole(store)

#endif
