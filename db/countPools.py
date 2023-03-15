def main(con):
    query = "SELECT COUNT(*) FROM pools"
    crsr = con.cursor()
    crsr.execute(query)
    value = crsr.fetchone()[0]
    return value
