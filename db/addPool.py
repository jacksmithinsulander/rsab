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
        query = 'INSERT INTO pools (net, netShort, netExtra, poolMainContract, poolAddress, timeCreated,token1Address,token1Symbol,token2Address,token2Symbol) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        data = [net, netShort, netExtra, poolMainContract, poolAddress, timeCreated, str(token1Address),
                token1Symbol, str(token2Address), token2Symbol]
        # con.executemany(sql, data
        con.cursor().execute(query, data)
        con.commit()
        print(f"      Saved pool for: {token1Symbol} - {token2Symbol}")
    except Exception as ErrorMsg:
        print(f"      Pool {poolAddress} already added probably")
        print(ErrorMsg)
