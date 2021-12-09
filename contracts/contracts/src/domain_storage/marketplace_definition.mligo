type sale = {
    token_id: token_id;
    price: price;
}

type datasets = (nat, dataset) big_map

type owners = (address, token_id set) big_map