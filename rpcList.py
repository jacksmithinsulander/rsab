import apiKeys

rpcList = {
    'ethereum': {
        'link': f"https://mainnet.infura.io/v3/{apiKeys.infura}",
        'short': "eth",
        'extra': "ether"
    },
    'polygon': {
        'link': "https://polygon-bor.publicnode.com",
        'short': "polygon",
        'extra': "polygon"
    }
}
