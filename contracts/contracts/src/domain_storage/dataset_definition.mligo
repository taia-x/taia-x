type price = tez

type dataset = {
    isOwned: bool;
    owner: address;
    onSale: bool;
    price: price option;
    id: nat
}
