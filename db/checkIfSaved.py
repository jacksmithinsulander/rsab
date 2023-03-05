def main(con, address):
    sql = f"""
    SELECT count(1) FROM pools WHERE poolAddress='{address}';
    """
    with con:
        r = con.execute(sql).fetchone()
    for re in r:
        if re == 1:
            return True
        else:
            return False