def main(con, address):
    query = f"SELECT EXISTS(SELECT * FROM pools WHERE pool_address='{address}')"
    crsr = con.cursor()
    crsr.execute(query)
    re = crsr.fetchone()[0]
    if re == 1:
        return True
    else:
        return False
