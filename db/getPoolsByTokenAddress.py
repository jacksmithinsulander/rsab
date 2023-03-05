def main(con, address):
    sql = f"SELECT * FROM pools WHERE token1Address='{address}' OR token2Address='{address}';"
    with con:
        data = con.execute(sql)
    return data.fetchall()