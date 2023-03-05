def main(con):
    sql = "SELECT * FROM pools;"
    poolArray = []
    with con:
        data = con.execute(sql)
        for row in data:
            poolArray.append(row)
    return poolArray