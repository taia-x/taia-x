import pytest

from .ipfs import IPFSClient


class TestIPFSClient:

    def test_wrong_port_number(self):
        with pytest.raises(AssertionError):
            IPFSClient('127.0.0.1', 0)

    def test_ipv4_address(self):
        addr, port, protocol = '127.0.0.1', 5001, 'ip4'
        client = IPFSClient(addr, port)
        assert client.protocol == protocol
        assert client.port_number == port
        assert client.connection_str == f'/{protocol}/{addr}/tcp/{port}/http'

    def test_ipv6_address(self):
        addr, port, protocol = '::1', 6789, 'ip6'
        client = IPFSClient(addr, port)
        assert client.protocol == protocol
        assert client.port_number == port
        assert client.connection_str == f'/{protocol}/{addr}/tcp/{port}/http'

    def test_dns_address(self):
        addr, port, protocol = 'ipfs', 3456, 'dns4'
        client = IPFSClient(addr, port)
        assert client.protocol == protocol
        assert client.port_number == port
        assert client.connection_str == f'/{protocol}/{addr}/tcp/{port}/http'