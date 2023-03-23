swaps = {
    'ethereum': {
        'uniswap3': [{"inputs": [], "stateMutability":"nonpayable", "type":"constructor"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "uint24", "name": "fee", "type": "uint24"}, {"indexed": True, "internalType": "int24", "name": "tickSpacing", "type": "int24"}], "name": "FeeAmountEnabled", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "oldOwner", "type": "address"}, {"indexed": True, "internalType": "address", "name": "newOwner", "type": "address"}], "name": "OwnerChanged", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "token0", "type": "address"}, {"indexed": True, "internalType": "address", "name": "token1", "type": "address"}, {"indexed": True, "internalType": "uint24", "name": "fee", "type": "uint24"}, {"indexed": False, "internalType": "int24", "name": "tickSpacing", "type": "int24"}, {"indexed": False, "internalType": "address", "name": "pool", "type": "address"}], "name": "PoolCreated", "type": "event"}, {"inputs": [{"internalType": "address", "name": "tokenA", "type": "address"}, {"internalType": "address", "name": "tokenB", "type": "address"}, {"internalType": "uint24", "name": "fee", "type": "uint24"}], "name": "createPool", "outputs": [{"internalType": "address", "name": "pool", "type": "address"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint24", "name": "fee", "type": "uint24"}, {"internalType": "int24", "name": "tickSpacing", "type": "int24"}], "name": "enableFeeAmount", "outputs": [], "stateMutability":"nonpayable", "type":"function"}, {"inputs": [{"internalType": "uint24", "name": "", "type": "uint24"}], "name": "feeAmountTickSpacing", "outputs": [{"internalType": "int24", "name": "", "type": "int24"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "", "type": "address"}, {"internalType": "address", "name": "", "type": "address"}, {"internalType": "uint24", "name": "", "type": "uint24"}], "name": "getPool", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name":"owner", "outputs":[{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name":"parameters", "outputs":[{"internalType": "address", "name": "factory", "type": "address"}, {"internalType": "address", "name": "token0", "type": "address"}, {"internalType": "address", "name": "token1", "type": "address"}, {"internalType": "uint24", "name": "fee", "type": "uint24"}, {"internalType": "int24", "name": "tickSpacing", "type": "int24"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_owner", "type": "address"}], "name": "setOwner", "outputs": [], "stateMutability":"nonpayable", "type":"function"}],
        'sushiv2': [{"inputs": [{"internalType": "address", "name": "_feeToSetter", "type": "address"}], "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "token0", "type": "address"}, {"indexed": True, "internalType": "address", "name": "token1", "type": "address"}, {"indexed": False, "internalType": "address", "name": "pair", "type": "address"}, {"indexed": False, "internalType": "uint256", "name": "", "type": "uint256"}], "name": "PairCreated", "type": "event"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "allPairs", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name":"allPairsLength", "outputs":[{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "tokenA", "type": "address"}, {"internalType": "address", "name": "tokenB", "type": "address"}], "name": "createPair", "outputs": [{"internalType": "address", "name": "pair", "type": "address"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name":"feeTo", "outputs":[{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name":"feeToSetter", "outputs":[{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "", "type": "address"}, {"internalType": "address", "name": "", "type": "address"}], "name": "getPair", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name":"migrator", "outputs":[{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name":"pairCodeHash", "outputs":[{"internalType": "bytes32", "name": "", "type": "bytes32"}], "stateMutability": "pure", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_feeTo", "type": "address"}], "name": "setFeeTo", "outputs": [], "stateMutability":"nonpayable", "type":"function"}, {"inputs": [{"internalType": "address", "name": "_feeToSetter", "type": "address"}], "name": "setFeeToSetter", "outputs": [], "stateMutability":"nonpayable", "type":"function"}, {"inputs": [{"internalType": "address", "name": "_migrator", "type": "address"}], "name": "setMigrator", "outputs": [], "stateMutability":"nonpayable", "type":"function"}],
        'apeswap': [{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"token0","type":"address"},{"indexed":True,"internalType":"address","name":"token1","type":"address"},{"indexed":False,"internalType":"address","name":"pair","type":"address"},{"indexed":False,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":True,"inputs":[],"name":"INIT_CODE_PAIR_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"}],
        'kyberswap': [{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"contract IERC20","name":"token0","type":"address"},{"indexed":True,"internalType":"contract IERC20","name":"token1","type":"address"},{"indexed":False,"internalType":"address","name":"pool","type":"address"},{"indexed":False,"internalType":"uint32","name":"ampBps","type":"uint32"},{"indexed":False,"internalType":"uint256","name":"totalPool","type":"uint256"}],"name":"PoolCreated","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"feeTo","type":"address"},{"indexed":False,"internalType":"uint16","name":"governmentFeeBps","type":"uint16"}],"name":"SetFeeConfiguration","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"feeToSetter","type":"address"}],"name":"SetFeeToSetter","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPools","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allPoolsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"tokenA","type":"address"},{"internalType":"contract IERC20","name":"tokenB","type":"address"},{"internalType":"uint32","name":"ampBps","type":"uint32"}],"name":"createPool","outputs":[{"internalType":"address","name":"pool","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getFeeConfiguration","outputs":[{"internalType":"address","name":"_feeTo","type":"address"},{"internalType":"uint16","name":"_governmentFeeBps","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token0","type":"address"},{"internalType":"contract IERC20","name":"token1","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getPoolAtIndex","outputs":[{"internalType":"address","name":"pool","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token0","type":"address"},{"internalType":"contract IERC20","name":"token1","type":"address"}],"name":"getPools","outputs":[{"internalType":"address[]","name":"_tokenPools","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token0","type":"address"},{"internalType":"contract IERC20","name":"token1","type":"address"}],"name":"getPoolsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"","type":"address"},{"internalType":"contract IERC20","name":"","type":"address"}],"name":"getUnamplifiedPool","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token0","type":"address"},{"internalType":"contract IERC20","name":"token1","type":"address"},{"internalType":"address","name":"pool","type":"address"}],"name":"isPool","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_feeTo","type":"address"},{"internalType":"uint16","name":"_governmentFeeBps","type":"uint16"}],"name":"setFeeConfiguration","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"stateMutability":"nonpayable","type":"function"}]
    },
    'polygon': {
        'quickswapv3': [{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"token0","type":"address"},{"indexed":True,"internalType":"address","name":"token1","type":"address"},{"indexed":False,"internalType":"address","name":"pair","type":"address"},{"indexed":False,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":True,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"}],
        'uniswap3': [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint24","name":"fee","type":"uint24"},{"indexed":True,"internalType":"int24","name":"tickSpacing","type":"int24"}],"name":"FeeAmountEnabled","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"oldOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"token0","type":"address"},{"indexed":True,"internalType":"address","name":"token1","type":"address"},{"indexed":True,"internalType":"uint24","name":"fee","type":"uint24"},{"indexed":False,"internalType":"int24","name":"tickSpacing","type":"int24"},{"indexed":False,"internalType":"address","name":"pool","type":"address"}],"name":"PoolCreated","type":"event"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"}],"name":"createPool","outputs":[{"internalType":"address","name":"pool","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"int24","name":"tickSpacing","type":"int24"}],"name":"enableFeeAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint24","name":"","type":"uint24"}],"name":"feeAmountTickSpacing","outputs":[{"internalType":"int24","name":"","type":"int24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint24","name":"","type":"uint24"}],"name":"getPool","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"parameters","outputs":[{"internalType":"address","name":"factory","type":"address"},{"internalType":"address","name":"token0","type":"address"},{"internalType":"address","name":"token1","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"int24","name":"tickSpacing","type":"int24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"setOwner","outputs":[],"stateMutability":"nonpayable","type":"function"}],
        'sushiv2': [{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"token0","type":"address"},{"indexed":True,"internalType":"address","name":"token1","type":"address"},{"indexed":False,"internalType":"address","name":"pair","type":"address"},{"indexed":False,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"migrator","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pairCodeHash","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_migrator","type":"address"}],"name":"setMigrator","outputs":[],"stateMutability":"nonpayable","type":"function"}],
        'apeswap': [{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"token0","type":"address"},{"indexed":True,"internalType":"address","name":"token1","type":"address"},{"indexed":False,"internalType":"address","name":"pair","type":"address"},{"indexed":False,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":True,"inputs":[],"name":"INIT_CODE_PAIR_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"}],
        'kyberswap': [{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"contract IERC20","name":"token0","type":"address"},{"indexed":True,"internalType":"contract IERC20","name":"token1","type":"address"},{"indexed":False,"internalType":"address","name":"pool","type":"address"},{"indexed":False,"internalType":"uint32","name":"ampBps","type":"uint32"},{"indexed":False,"internalType":"uint256","name":"totalPool","type":"uint256"}],"name":"PoolCreated","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"feeTo","type":"address"},{"indexed":False,"internalType":"uint16","name":"governmentFeeBps","type":"uint16"}],"name":"SetFeeConfiguration","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"feeToSetter","type":"address"}],"name":"SetFeeToSetter","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPools","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allPoolsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"tokenA","type":"address"},{"internalType":"contract IERC20","name":"tokenB","type":"address"},{"internalType":"uint32","name":"ampBps","type":"uint32"}],"name":"createPool","outputs":[{"internalType":"address","name":"pool","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getFeeConfiguration","outputs":[{"internalType":"address","name":"_feeTo","type":"address"},{"internalType":"uint16","name":"_governmentFeeBps","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token0","type":"address"},{"internalType":"contract IERC20","name":"token1","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getPoolAtIndex","outputs":[{"internalType":"address","name":"pool","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token0","type":"address"},{"internalType":"contract IERC20","name":"token1","type":"address"}],"name":"getPools","outputs":[{"internalType":"address[]","name":"_tokenPools","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token0","type":"address"},{"internalType":"contract IERC20","name":"token1","type":"address"}],"name":"getPoolsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"","type":"address"},{"internalType":"contract IERC20","name":"","type":"address"}],"name":"getUnamplifiedPool","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token0","type":"address"},{"internalType":"contract IERC20","name":"token1","type":"address"},{"internalType":"address","name":"pool","type":"address"}],"name":"isPool","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_feeTo","type":"address"},{"internalType":"uint16","name":"_governmentFeeBps","type":"uint16"}],"name":"setFeeConfiguration","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"stateMutability":"nonpayable","type":"function"}]
    },
    'arbitrum': {
        'uniswap3': [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint24","name":"fee","type":"uint24"},{"indexed":True,"internalType":"int24","name":"tickSpacing","type":"int24"}],"name":"FeeAmountEnabled","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"oldOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"token0","type":"address"},{"indexed":True,"internalType":"address","name":"token1","type":"address"},{"indexed":True,"internalType":"uint24","name":"fee","type":"uint24"},{"indexed":False,"internalType":"int24","name":"tickSpacing","type":"int24"},{"indexed":False,"internalType":"address","name":"pool","type":"address"}],"name":"PoolCreated","type":"event"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"}],"name":"createPool","outputs":[{"internalType":"address","name":"pool","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"int24","name":"tickSpacing","type":"int24"}],"name":"enableFeeAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint24","name":"","type":"uint24"}],"name":"feeAmountTickSpacing","outputs":[{"internalType":"int24","name":"","type":"int24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint24","name":"","type":"uint24"}],"name":"getPool","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"parameters","outputs":[{"internalType":"address","name":"factory","type":"address"},{"internalType":"address","name":"token0","type":"address"},{"internalType":"address","name":"token1","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"int24","name":"tickSpacing","type":"int24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"setOwner","outputs":[],"stateMutability":"nonpayable","type":"function"}],
        'sushiv2' : [{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"token0","type":"address"},{"indexed":True,"internalType":"address","name":"token1","type":"address"},{"indexed":False,"internalType":"address","name":"pair","type":"address"},{"indexed":False,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"migrator","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pairCodeHash","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_migrator","type":"address"}],"name":"setMigrator","outputs":[],"stateMutability":"nonpayable","type":"function"}],
        'kyberswap' : [{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint24","name":"feeUnits","type":"uint24"}],"name":"DisableFeeOption","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint24","name":"feeUnits","type":"uint24"}],"name":"EnableFeeOption","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"contract IERC20","name":"token0","type":"address"},{"indexed":True,"internalType":"contract IERC20","name":"token1","type":"address"},{"indexed":False,"internalType":"address","name":"pool","type":"address"},{"indexed":False,"internalType":"uint32","name":"ampBps","type":"uint32"},{"indexed":False,"internalType":"uint24","name":"feeUnits","type":"uint24"},{"indexed":False,"internalType":"uint256","name":"totalPool","type":"uint256"}],"name":"PoolCreated","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"feeTo","type":"address"},{"indexed":False,"internalType":"uint24","name":"governmentFeeUnits","type":"uint24"}],"name":"SetFeeConfiguration","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"feeToSetter","type":"address"}],"name":"SetFeeToSetter","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPools","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allPoolsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"tokenA","type":"address"},{"internalType":"contract IERC20","name":"tokenB","type":"address"},{"internalType":"uint32","name":"ampBps","type":"uint32"},{"internalType":"uint24","name":"feeUnits","type":"uint24"}],"name":"createPool","outputs":[{"internalType":"address","name":"pool","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint24","name":"_feeUnits","type":"uint24"}],"name":"disableFeeOption","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint24","name":"_feeUnits","type":"uint24"}],"name":"enableFeeOption","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint24","name":"","type":"uint24"}],"name":"feeOptions","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getFeeConfiguration","outputs":[{"internalType":"address","name":"_feeTo","type":"address"},{"internalType":"uint24","name":"_governmentFeeUnits","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token0","type":"address"},{"internalType":"contract IERC20","name":"token1","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getPoolAtIndex","outputs":[{"internalType":"address","name":"pool","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token0","type":"address"},{"internalType":"contract IERC20","name":"token1","type":"address"}],"name":"getPools","outputs":[{"internalType":"address[]","name":"_tokenPools","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token0","type":"address"},{"internalType":"contract IERC20","name":"token1","type":"address"}],"name":"getPoolsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"","type":"address"},{"internalType":"contract IERC20","name":"","type":"address"}],"name":"getUnamplifiedPool","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token0","type":"address"},{"internalType":"contract IERC20","name":"token1","type":"address"},{"internalType":"address","name":"pool","type":"address"}],"name":"isPool","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_feeTo","type":"address"},{"internalType":"uint24","name":"_governmentFeeUnits","type":"uint24"}],"name":"setFeeConfiguration","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"stateMutability":"nonpayable","type":"function"}]
    }
}
erc20 = [{"inputs": [], "name":"name", "outputs":[{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {
    "inputs": [], "name":"symbol", "outputs":[{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}]
