type name = string
type description = string option
type price = tez

type dataset = {
    name: name;
    description: description;
    isOwned: bool;
    owner: address;
    onSale: bool;
    price: price option;
    id: nat
}
