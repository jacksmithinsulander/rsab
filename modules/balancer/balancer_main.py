
from web3 import Web3
from web3.middleware import geth_poa_middleware
from modules.onchain.rpc_list import rpc_list
from time import sleep
from loguru import logger
from modules.balancer.http_connector import get_tor_session


class Balancer():
    def __init__(self):
        logger.debug('init started')
        self.balancer = {}
        for network in rpc_list:
            self.balancer[network] = 0

    def w3(self, network):
        self.balancer[network] += 1
        self.balancer[network] = self.balancer[network] % len(
            rpc_list[network]['links'])
        session = get_tor_session()
        w3 = Web3(Web3.HTTPProvider(
            rpc_list[network]['links'][self.balancer[network]], session=session))
        if (network == "matic" or network == "bnb"):
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        if (w3.is_connected()):
            logger.debug(
                f"Returning W3 on {rpc_list[network]['links'][self.balancer[network]]}")
            return w3
        else:
            logger.debug(
                f"Unable to connect to {rpc_list[network]['links'][self.balancer[network]]}")
            sleep(0.5)
            return self.w3(network)
