import sqlite3
import db.add_pool
import db.check_if_saved
import db.copy_pool
import db.count_pools
import db.delete_by_address
import db.edit_pool
import db.get_all_pools
import db.get_by_address
import db.get_by_token_address
import db.get_by_token_symbol
import db.print_all_pools

# Real data
con = sqlite3.connect("db/pools.db")

# # Mock data
# con = sqlite3.connect("mockdata/found_pools.db")
# conPassedFA = sqlite3.connect("mockdata/passedFa.db")

_net = 1
_net_short = 2
_net_extra = 3
_pool_main_contract = 4
_pool_address = 5
_time_created = 6
_token1_address = 7
_token1_symbol = 8
_token2_address = 9
_token2_symbol = 10
_dex = 11
_creation_block = 12

with con:
    con.execute("""
        CREATE TABLE if not exists pools_found(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            net TEXT,
            net_short TEXT,
            net_extra TEXT,
            pool_main_contract TEXT,
            pool_address TEXT UNIQUE,
            time_created INTEGER,
            token1_address TEXT,
            token1_symbol TEXT,
            token2_address TEXT,
            token2_symbol TEXT,
            dex TEXT,
            creation_block INTEGER
        );
    """)
    con.execute("""
        CREATE TABLE if not exists pools_passed_fa(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            net TEXT,
            net_short TEXT,
            net_extra TEXT,
            pool_main_contract TEXT,
            pool_address TEXT UNIQUE,
            time_created INTEGER,
            token1_address TEXT,
            token1_symbol TEXT,
            token2_address TEXT,
            token2_symbol TEXT,
            dex TEXT,
            creation_block INTEGER,
            passed_fa1 INTEGER,
            passed_fa2 INTEGER,
            passed_fa3 INTEGER
        );
    """)

# with conPassedFA:
#     conPassedFA.execute("""
#         CREATE TABLE if not exists pools(
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             net TEXT,
#             net_short TEXT,
#             net_extra TEXT,
#             pool_main_contract TEXT,
#             pool_address TEXT UNIQUE,
#             time_created INTEGER,
#             token1_address TEXT,
#             token1_symbol TEXT,
#             token2_address TEXT,
#             token2_symbol TEXT
#         );
#     """)


def add_pool(table,
            net,
            net_short,
            net_extra,
            pool_main_contract,
            pool_address,
            time_created,
            token1_address,
            token1_symbol,
            token2_address,
            token2_symbol,
            dex,
            creation_block):
    db.add_pool.main(con, table, net,
                    net_short,
                    net_extra,
                    pool_main_contract,
                    pool_address,
                    time_created,
                    token1_address,
                    token1_symbol,
                    token2_address,
                    token2_symbol,
                    dex,
                    creation_block)

def check_if_saved(table, address):
    return db.check_if_saved.main(con, table, address)

def copy_pool(from_table, to_table, address):
    db.copy_pool.main(con, from_table, to_table, address)

def count_pools(table):
    return db.count_pools.main(con, table)

def delete_by_address(table, address):
    db.delete_by_address.main(con, table, address)

def edit_pool(table, address, column, new_value):
    db.edit_pool.main(con, table, address, column, new_value)

def get_all_pools(table):
    return db.get_all_pools.main(con, table)

def get_by_address(table, address):
    return db.get_by_address.main(con, table, address)

def get_by_token_address(table, address):
    return db.get_by_token_address.main(con, table, address)

def get_by_token_symbol(table, symbol):
    return db.get_by_token_symbol.main(con, table, symbol)

def print_all_pools(table):
    db.print_all_pools.main(con, table)


# def addPoolToPassedFA(net,
#                       net_short,
#                       net_extra,
#                       pool_main_contract,
#                       pool_address,
#                       time_created,
#                       token1_address,
#                       token1_symbol,
#                       token2_address,
#                       token2_symbol):
#     db.add_pool.main(conPassedFA, net,
#                     net_short,
#                     net_extra,
#                     pool_main_contract,
#                     pool_address,
#                     time_created,
#                     token1_address,
#                     token1_symbol,
#                     token2_address,
#                     token2_symbol)
