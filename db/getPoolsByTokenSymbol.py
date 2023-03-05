def main(con, symbol):
    sql = f"SELECT * FROM pools WHERE token1Symbol='{symbol}' OR token2Symbol='{symbol}';"
    with con:
        data = con.execute(sql)
    return data.fetchall()