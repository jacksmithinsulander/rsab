def main(con, table):
    sql = f"SELECT COUNT(*) FROM {table}"
    value = con.execute(sql).fetchone()[0]
    return value