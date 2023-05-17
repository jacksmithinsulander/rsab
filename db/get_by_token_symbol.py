def main(con, table, symbol):
    sql = f"SELECT * FROM {table} WHERE token1_symbol='{symbol}' OR token2_symbol='{symbol}';"
    with con:
        data = con.execute(sql)
    return data.fetchall()