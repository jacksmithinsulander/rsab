def translator(input_chain):
    translations = {
        "eth": "1",
        "op": "10",
        "cronos": "25",
        "bsc": "56",
        "okc": "66",
        "gnosis": "100",
        "heco": "128",
        "matic": "137",
        "ftm": "250",
        "kcc": "321",
        "zkera": "324",
        "arb": "42161",
        "avax": "43114",
        "one": "1666600000",
        "trx": "tron"
    }

    if input_chain in translations:
        return translations[input_chain]
    else:
        return "Translation not found."
