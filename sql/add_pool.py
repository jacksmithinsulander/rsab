def main(con, net,
         net_short,
         net_extra,
         pool_main_contract,
         pool_address,
         time_created,
         token1_address,
         token1_symbol,
         token2_address,
         token2_symbol):
    try:
        query = 'INSERT INTO pools (net, net_short, net_extra, pool_main_contract, pool_address, time_created,token1_address,token1_symbol,token2_address,token2_symbol) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
        data = [net, net_short, net_extra, pool_main_contract, pool_address, time_created, str(token1_address),
                token1_symbol, str(token2_address), token2_symbol]
        # con.executemany(sql, data
        con.cursor().execute(query, data)
        con.commit()
        print(f"      Saved pool for: {token1_symbol} - {token2_symbol}")
    except Exception as error_msg:
        print(f"      Pool {pool_address} already added probably")
        print(error_msg)
