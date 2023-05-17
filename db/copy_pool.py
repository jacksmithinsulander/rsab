def main(con, from_table, to_table, address):
    sql = f"""
        INSERT INTO {to_table}
        SELECT * FROM {from_table}
        WHERE pool_address="{address}";
    """
    print(sql)
    with con:
        con.execute(sql)