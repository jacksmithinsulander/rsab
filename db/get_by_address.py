def main(con, table, address):
    sql = f"SELECT * FROM {table} WHERE pool_address='{address}';"
    with con:
        data = con.execute(sql)
    return data.fetchone()