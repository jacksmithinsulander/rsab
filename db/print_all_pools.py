def main(con, table):
    sql = f"SELECT * FROM {table};"
    with con:
        data = con.execute(sql)
        for row in data:
            print(row)