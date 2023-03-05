def main(con):
    sql = "SELECT COUNT(*) FROM pools"
    value = con.execute(sql).fetchone()[0]
    return value