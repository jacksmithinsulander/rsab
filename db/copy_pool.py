def main(con, from_table, to_table, address):
    sql = f"""
        INSERT INTO {to_table} ( net,
            net_short,
            net_extra,
            pool_main_contract,
            pool_address,
            time_created,
            token1_address,
            token1_symbol,
            token2_address,
            token2_symbol)
        SELECT net,
            net_short,
            net_extra,
            pool_main_contract,
            pool_address,
            time_created,
            token1_address,
            token1_symbol,
            token2_address,
            token2_symbol FROM {from_table} 
        WHERE pool_address="{address}";
    """
    # print(sql)
    with con:
        con.execute(sql)