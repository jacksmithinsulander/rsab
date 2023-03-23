import apiKeys

rpcList = {
    'ethereum': {
        'links': [f"https://mainnet.infura.io/v3/{apiKeys.infura}"],
        'short': "eth",
        'extra': "ether"
    },  # "https://polygon.llamarpc.com",
    'polygon': {
        'links': ["https://polygon-bor.publicnode.com", "https://polygon.blockpi.network/v1/rpc/public", "https://rpc.ankr.com/polygon"],
        'short': "polygon",
        'extra': "polygon"
    },
    'arbitrum': {
        'links': ["https://arbitrum.blockpi.network/v1/rpc/public", "https://endpoints.omniatech.io/v1/arbitrum/one/public"],
        'short': "arbitrum",
        'extra': "arbitrum"
    }
}
