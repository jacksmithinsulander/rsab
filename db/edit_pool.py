def main(con, table, address, column, new_value):
    try:
        sql = f'UPDATE {table} SET {column} = {new_value} WHERE pool_address="{address}";'
        with con:
            con.execute(sql)
        print(f"# Edited {column} on {table}-{address} to {new_value}")
    except Exception as error_msg:
        print(error_msg)
