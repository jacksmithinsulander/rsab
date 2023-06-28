def token_parser(token):
	cases = {
		"polygon": ["matic", "matic", "polygon"],
		"ethereum": ["eth", "ether", "ethereum"],
		"arbitrum": ["arb", "arb", "arbitrum"],
		"optimism": ["op", "op", "optimism"],
		"fantom": ["ftm", "ftm", "fantom"],
		"avalanche": ["avax", "avax", "avalanche"],
		"metis": ["metis", "andromeda", "metis"],
		"harmony": ["one", "one", "harmony"],
		"pulsechain": ["pls", "pulse", "pulsechain"]
	}
	result = cases.get(token, "Unrecognised token!")
	return result
	

