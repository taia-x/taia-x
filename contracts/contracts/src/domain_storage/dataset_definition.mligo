type price = tez

type dataset = {
    isOwned: bool;
    owner: address;
    price: price option;
    id: nat;
}