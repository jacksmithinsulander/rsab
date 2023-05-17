def main(con, table, address):
    sql = f"SELECT * FROM {table} WHERE token1_address='{address}' OR token2_address='{address}';"
    with con:
        data = con.execute(sql)
    return data.fetchall()