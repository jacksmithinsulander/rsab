from web3 import Web3
import apiKeys
from datetime import datetime
from time import sleep


w3local = Web3(Web3.HTTPProvider("http://192.168.0.237:8545"))
w3infura = Web3(Web3.HTTPProvider(
    f"https://mainnet.infura.io/v3/{apiKeys.infura}"))

blocksPerMinute = []
lastLocal = w3local.eth.block_number
print(lastLocal)

while True:
    localBlock = w3local.eth.block_number
    infuraBlock = w3infura.eth.block_number
    increase = localBlock - lastLocal
    blocksPerMinute.append(increase)
    averageBlocksPerMinute = 0
    for i in range(0, len(blocksPerMinute)):
        averageBlocksPerMinute += blocksPerMinute[i]
    averageBlocksPerMinute /= len(blocksPerMinute)

    blocksLeft = infuraBlock - localBlock
    if (averageBlocksPerMinute > 0):
        timeLeft = blocksLeft/averageBlocksPerMinute
    else:
        timeLeft = 999999999999999999999999

    percentage = (localBlock/infuraBlock)*100
    now = datetime.now().strftime("%H:%M:%S")
    print(f"# {now} ######################################")
    print(f"Progress: {percentage}% - {localBlock}/{infuraBlock}")
    print(f"Average Blocks Per Minute: {averageBlocksPerMinute}")
    print(f"Estimate time left:")
    print(f" - Minutes: {timeLeft}")
    print(f" - Hours: {timeLeft/60}")
    print(f" - Days: {timeLeft/60/24}")
    sleep(60)
    lastLocal = localBlock
