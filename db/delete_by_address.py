def main(con, table, address):
    sql = f'DELETE FROM {table} WHERE pool_address="{address}";'
    print(sql)
    with con:
        con.execute(sql)