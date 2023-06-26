#import api_keys

rpc_list = {
    'ethereum': {
        'links': [f"https://endpoints.omniatech.io/v1/eth/mainnet/public"],
        'short': "eth",
        'extra': "ether"
    },  
    'polygon': {
        'links': ["https://polygon-bor.publicnode.com", "https://polygon.blockpi.network/v1/rpc/public", "https://rpc.ankr.com/polygon"],
        # "https://polygon.llamarpc.com",
        'short': "polygon",
        'extra': "polygon"
    },
    'arbitrum': {
        'links': ["https://arbitrum.blockpi.network/v1/rpc/public", "https://endpoints.omniatech.io/v1/arbitrum/one/public"],
        'short': "arbitrum",
        'extra': "arbitrum"
    }
}
