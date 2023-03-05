def main(con, address):
    sql = f'DELETE FROM pools WHERE address="{address}";'
    print(sql)
    with con:
        con.execute(sql)