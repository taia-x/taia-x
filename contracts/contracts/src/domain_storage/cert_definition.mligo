type cert_state = Pending | Certified | Rejected

type cert = {
    dataset_id: token_id; 
    issuer: address option; // certifier: optional because must be set after certify
    root_hash: bytes;
    state: cert_state;
}

type cert_storage = (token_id, cert) big_map // dataset -> cert

type cert_params = {
    dataset_id: token_id; 
    root_hash: bytes;
}

type update_cert_param =
[@layout:comb]
  | Certify of cert_params
  | Reject of cert_params