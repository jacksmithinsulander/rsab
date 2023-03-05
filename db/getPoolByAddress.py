def main(con, address):
    sql = f"SELECT * FROM pools WHERE address='{address}';"
    with con:
        data = con.execute(sql)
    return data.fetchone()