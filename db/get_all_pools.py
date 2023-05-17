def main(con, table):
    sql = f"SELECT * FROM {table};"
    pool_array = []
    with con:
        data = con.execute(sql)
        for row in data:
            pool_array.append(row)
    return pool_array