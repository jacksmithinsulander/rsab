from loguru import logger
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
            token2_symbol,
            dex,
            creation_block)
        SELECT net,
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
            creation_block FROM {from_table} 
        WHERE pool_address="{address}";
    """
    logger.debug(sql)
    with con:
        con.execute(sql)