from modules.onchain import abi
from modules.onchain.rpc_list import rpc_list
from modules.onchain.swap_list import swap_list
from modules.balancer.balancer_main import Balancer
import db.main as db
from web3 import Web3
from time import sleep
from datetime import datetime
import json
from web3.middleware import geth_poa_middleware


class Scanner:
    def __init__(self):
        with open('conf.json', "r") as file:
            self.conf = json.load(file)
        print(f"Loaded with config:\n{self.conf}")

        # self.balancer = 0
        self.last_blocks = {
            'ethereum': 0,
            'polygon': 0,
            'arbitrum': 0
        }
        self.balancer = Balancer()

        for net in rpc_list:
            # self.rpc_link = rpc_list[net]['links'][0]
            self.w3 = self.balancer.w3(net) #Web3(Web3.HTTPProvider(self.rpc_link))
            self.last_blocks[net] = self.w3.eth.block_number - 500

    def start(self):
        while True:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"# {now} ######################################")
            for net in rpc_list:
                # rpc_link = rpc_list[net]['links'][self.balancer %
                #                                   len(rpc_list[net]['links'])]
                w3 = self.balancer.w3(net)#Web3(Web3.HTTPProvider(rpc_link))
                if (net == 'polygon'):
                    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
                current_block = w3.eth.block_number
                # fromBlock = lastBlock - 50
                print(
                    f"  # Checking {net} # Blocks {self.last_blocks[net]}-{current_block}")
                # print(f"  # Using {rpc_link}")
                # print(f"Connection to {net}: {w3.isConnected()}")
                for swap in swap_list[net]:
                    print(
                        f"    # Checking for pools by {swap}")
                    contract = w3.eth.contract(address=Web3.to_checksum_address(
                        swap_list[net][swap]['address']), abi=abi.swaps[net][swap])

                    exec(
                        f"self.get_pools = contract.events.{swap_list[net][swap]['event_name']}.get_logs")
                    latest_pools = self.get_pools(
                        fromBlock=self.last_blocks[net])

                    for pool in latest_pools:
                        pool_address = pool['args'][swap_list[net][swap]
                                                    ['pool_address']]
                        if (db.check_if_saved("pools_found", pool_address)):
                            print(f'      Already saved {pool_address}')
                        else:
                            token1_address = pool['args']['token0']
                            token1 = w3.eth.contract(
                                token1_address, abi=abi.erc20)
                            token1_symbol = token1.functions.symbol().call()

                            token2_address = pool['args']['token1']
                            token2 = w3.eth.contract(
                                token2_address, abi=abi.erc20)
                            token2_symbol = token2.functions.symbol().call()

                            unixTime = w3.eth.get_block(
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
                                       token2_symbol)
                self.last_blocks[net] = current_block
            print(f"Currently {db.count_pools('pools_found')} pools saved")
            print(f"Sleeping 30 seconds before next check")
            sleep(30)
            print("###########################################")
            # self.balancer += 1
