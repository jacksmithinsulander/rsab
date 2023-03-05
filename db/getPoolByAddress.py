def main(con, address):
    sql = f"SELECT * FROM pools WHERE poolAddress='{address}';"
    with con:
        data = con.execute(sql)
    return data.fetchone()