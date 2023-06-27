def token_parser(token):
	cases = {
		"polygon": ["matic", "matic", "polygon"],
		"ethereum": ["eth", "ether", "ethereum"],
		"arbitrum": ["arb", "arb", "arbitrum"]
	}
	result = cases.get(token, "Unrecognised token!")
	return result
	

