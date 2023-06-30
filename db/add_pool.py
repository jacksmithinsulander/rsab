def main(con, table, net,
         net_short,
         net_extra,
         pool_main_contract,
         pool_address,
         time_created,
         token1_address,
         token1_symbol,
         token2_address,
         token2_symbol,
         dex,
         creation_block):
    try:
        sql = f'INSERT INTO {table} (net, net_short, net_extra, pool_main_contract, pool_address, time_created,token1_address,token1_symbol,token2_address,token2_symbol, dex, creation_block) values(?,?,?,?,?,?,?,?,?,?,?,?);'
        data = [(net, net_short, net_extra, pool_main_contract, pool_address, 
                 time_created, str(token1_address), token1_symbol, 
                 str(token2_address), token2_symbol, dex, creation_block)]
        with con:
            con.executemany(sql, data)
        print(f"      # Added {token1_symbol}-{token2_symbol} to {table}")
    except Exception as error_msg:
        print(f"Pool {pool_address} already added probably")
        print(error_msg)
