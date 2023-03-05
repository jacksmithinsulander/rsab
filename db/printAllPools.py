def main(con):
    sql = "SELECT * FROM pools;"
    with con:
        data = con.execute(sql)
        for row in data:
            print(row)