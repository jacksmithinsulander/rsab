def main(con, 
            net,
            poolContract,
            poolAddress,
            timeCreated,
            token1Address,
            token1Symbol,
            token2Address,
            token2Symbol):
    try:
        sql = 'INSERT INTO pools (net, poolContract, poolAddress, timeCreated,token1Address,token1Symbol,token2Address,token2Symbol) values(?,?,?,?,?,?,?,?);'
        data = [(net, poolContract, poolAddress, timeCreated, str(token1Address),
                 token1Symbol, str(token2Address), token2Symbol)]
        with con:
            con.executemany(sql, data)
        print(f"Saved pool for: {token1Symbol} - {token2Symbol}")
    except Exception as ErrorMsg:
        print(f"Pool {poolAddress} already added probably")
        print(ErrorMsg)