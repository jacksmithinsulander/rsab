
from web3 import Web3
from web3.middleware import geth_poa_middleware
from modules.onchain.rpc_list import rpc_list
from time import sleep


class Balancer():
    def __init__(self):
        # print("Created")
        self.balancer = {}
        for network in rpc_list:
            self.balancer[network] = 0
        
    def w3(self, network):
        # print("first", self.balancer[network])
        self.balancer[network] += 1
        # print("second", self.balancer[network])
        self.balancer[network] = self.balancer[network] % len(rpc_list[network]['links'])
        w3 = Web3(Web3.HTTPProvider(rpc_list[network]['links'][self.balancer[network]]))
        if (network == "polygon"):
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        # print("last", self.balancer[network])
        if (w3.is_connected()):
            print(f"RPC: {rpc_list[network]['links'][self.balancer[network]]}")
            return w3
        else:
            # print("not connected trying again")
            # print(f"balancer: {self.balancer[network]}")
            sleep(0.5)
            return self.w3(network)

        