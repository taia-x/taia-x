#if !MAIN
#define MAIN

#include "interface.ligo"
#include "role.ligo"
#include "dataset.ligo"

type action is
    Mint of string
  | MakeCertifier 
  | MakeProvider 
  | MakeConsumer
  | RemoveRole 


function main (const action: action; var store: store): return is
  block {
    skip
  } with case action of
    | Mint (p) -> mint(p, store)
    | MakeCertifier -> makeCertifier(store)
    | MakeProvider -> makeProvider(store)
    | MakeConsumer -> makeConsumer(store)
    | RemoveRole -> removeRole(store)
  end;

#endif
