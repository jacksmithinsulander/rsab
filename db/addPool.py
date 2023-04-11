def main(con, net,
         netShort,
         netExtra,
         poolMainContract,
         poolAddress,
         timeCreated,
         token1Address,
         token1Symbol,
         token2Address,
         token2Symbol):
    try:
        sql = 'INSERT INTO pools (net, netShort, netExtra, poolMainContract, poolAddress, timeCreated,token1Address,token1Symbol,token2Address,token2Symbol) values(?,?,?,?,?,?,?,?,?,?);'
        data = [(net, netShort, netExtra, poolMainContract, poolAddress, timeCreated, str(token1Address),
                 token1Symbol, str(token2Address), token2Symbol)]
        with con:
            con.executemany(sql, data)
        print(f"      # Saved pool for: {token1Symbol} - {token2Symbol}")
    except Exception as ErrorMsg:
        print(f"Pool {poolAddress} already added probably")
        print(ErrorMsg)
