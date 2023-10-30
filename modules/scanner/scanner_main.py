from modules.onchain import abi
from modules.onchain.rpc_list import rpc_list
from modules.onchain.swap_list import swap_list
from web3_balancer import Web3_balancer
import db.main as db
from web3 import Web3
from time import sleep
from datetime import datetime
import json
from web3.middleware import geth_poa_middleware
from loguru import logger

tor_toggle_placeholder = True


class Scanner:
    def __init__(self):
        logger.debug("init started")
        with open('conf.json', "r") as file:
            self.conf = json.load(file)
        logger.info(f"Loaded with config:\n{self.conf}")

        logger.debug(self.conf['chains'])
        self.last_blocks = {}
        for chain in self.conf['chains']:
            self.last_blocks[chain] = 0

        self.w3 = Web3_balancer(rpc_list, tor=tor_toggle_placeholder)

        logger.debug('Setting up start blocks for each chain')
        for net in self.conf['chains']:
            logger.debug(f"Checking last block for {net}")
            # self.w3 = self.balancer.w3(net)
            self.w3.net = net
            self.last_blocks[net] = self.w3.eth.block_number() - 500
            logger.debug(
                f"Last block for {net} is set to {self.last_blocks[net]}")

    def start(self):
        while True:
            now = datetime.now().strftime("%H:%M:%S")
            for net in self.conf['chains']:
                self.w3.net = net
                logger.debug(f"w3.is_connected = {self.w3.is_connected()}")
                # w3 = self.balancer.w3(net)
                current_block = self.w3.eth.block_number()
                block_amount = current_block - self.last_blocks[net]
                logger.info(
                    f"Checking {net} # Blocks {self.last_blocks[net]}-{current_block} ({block_amount})")
                for swap in swap_list[net]:
                    logger.info(
                        f"Checking for pools on {swap}")
                    contract = self.w3.eth.contract(address=Web3.to_checksum_address(
                        swap_list[net][swap]['address']), abi=abi.swaps[net][swap])
                    exec(
                        f"self.get_pools = contract.events.{swap_list[net][swap]['event_name']}.get_logs")
                    latest_pools = self.get_pools(
                        fromBlock=self.last_blocks[net])

                    for pool in latest_pools:
                        pool_address = pool['args'][swap_list[net][swap]
                                                    ['pool_address']]
                        if (db.check_if_saved("pools_found", pool_address)):
                            logger.info(
                                f'Already saved {pool_address} ({pool["args"]["token0"]}-{pool["args"]["token1"]})')
                        else:
                            token1_address = pool['args']['token0']
                            token1 = self.w3.eth.contract(
                                token1_address, abi=abi.erc20)
                            token1_symbol = token1.functions.symbol().call()

                            token2_address = pool['args']['token1']
                            token2 = self.w3.eth.contract(
                                token2_address, abi=abi.erc20)
                            token2_symbol = token2.functions.symbol().call()
                            creation_block = pool['blockNumber']

                            unixTime = self.w3.eth.get_block(
                                pool['blockNumber']).timestamp
                            db.add_pool("pools_found", net,
                                        rpc_list[net]['short'],
                                        rpc_list[net]['extra'],
                                        swap_list[net][swap]['address'],
                                        pool_address,
                                        unixTime,
                                        token1_address,
                                        token1_symbol,
                                        token2_address,
                                        token2_symbol,
                                        swap,
                                        creation_block)
                self.last_blocks[net] = current_block
            logger.info(
                f"Currently {db.count_pools('pools_found')} pools saved")
            logger.info(f"Sleeping 30 seconds before next check")
            sleep(30)
