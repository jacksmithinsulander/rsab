from loguru import logger
def main(con, table, address):
    sql = f'DELETE FROM {table} WHERE pool_address="{address}";'
    logger.debug(sql)
    with con:
        con.execute(sql)