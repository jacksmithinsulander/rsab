def main(con, table, address):
    sql = f"""
    SELECT count(1) FROM {table} WHERE pool_address='{address}';
    """
    with con:
        r = con.execute(sql).fetchone()
    for re in r:
        if re == 1:
            return True
        else:
            return False