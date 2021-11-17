import ipfshttpclient

from ipaddress import ip_address, ip_interface, IPv4Address, IPv6Address

from.config import IPFS_ADDRESS, IPFS_PORT


class IPFSClient:

    def __init__(self, address: str, port_number: int):
        
        assertion_error = f'port number must be 1 <= port number <= 65535 porvided: {port_number}'
        assert 1 <= port_number <= 65535, assertion_error
        self.port_number: int = port_number
        
        # decide whether given address uses ip4, ip6 or dns4 protocol
        try:
            ip_addr: IPv4Address | IPv6Address = ip_address(address)
            self.protocol = f'ip{ip_addr.version}'
        except ValueError:
            self.protocol = 'dns4'

        self.address = address
        self.connection_str: str = f'/{self.protocol}/{self.address}/tcp/{self.port_number}/http'

    def save_json(self, payload: dict) -> str:
        if self.connection_str:
            with ipfshttpclient.connect(self.connection_str) as client:
                return client.add_json(payload)
                

ipfs_client = IPFSClient(IPFS_ADDRESS, IPFS_PORT)
