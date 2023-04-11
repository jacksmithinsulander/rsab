import mysql.connector
from mysql.connector import Error
import sql.config as cfg
import sql.add_pool
import sql.count_pools
import sql.check_if_saved


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


con = create_connection(
    cfg.server, cfg.username, cfg.password, cfg.db)
print(con)

query = """
        CREATE TABLE if not exists pools(
            net TEXT,
            net_short TEXT,
            net_extra TEXT,
            pool_main_contract TEXT,
            pool_address TEXT,
            time_created INTEGER,
            token1_address TEXT,
            token1_symbol TEXT,
            token2_address TEXT,
            token2_symbol TEXT
        );
    """
con.cursor().execute(query)
con.commit()


def add_pool(net,
             net_short,
             net_extra,
             pool_main_contract,
             pool_address,
             time_created,
             token1_address,
             token1_symbol,
             token2_address,
             token2_symbol):
    sql.add_pool.main(con, net,
                      net_short,
                      net_extra,
                      pool_main_contract,
                      pool_address,
                      time_created,
                      token1_address,
                      token1_symbol,
                      token2_address,
                      token2_symbol)


def count_pools():
    return sql.count_pools.main(con)


def check_if_saved(address):
    return sql.check_if_saved.main(con, address)
