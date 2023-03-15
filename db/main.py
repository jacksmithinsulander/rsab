import sqlite3
import mysql.connector
from mysql.connector import Error
import apiKeys
import db.addPool
import db.checkIfSaved
import db.countPools
import db.deleteByAddress
import db.getAllPools
import db.getPoolByAddress
import db.getPoolsByTokenAddress
import db.getPoolsByTokenSymbol
import db.printAllPools


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
    "192.168.0.237", apiKeys.sql_user, apiKeys.sql_pass, "wagmi")

# key for output
_net = 1
_netShort = 2
_netExtra = 3
_poolMainContract = 4
_poolAddress = 5
_timeCreated = 6
_token1Address = 7
_token1Symbol = 8
_token2Address = 9
_token2Symbol = 10

query = """
        CREATE TABLE if not exists pools(
            net TEXT,
            netShort TEXT,
            netExtra TEXT,
            poolMainContract TEXT,
            poolAddress TEXT,
            timeCreated INTEGER,
            token1Address TEXT,
            token1Symbol TEXT,
            token2Address TEXT,
            token2Symbol TEXT
        );
    """
con.cursor().execute(query)
con.commit()


def addPool(net,
            netShort,
            netExtra,
            poolMainContract,
            poolAddress,
            timeCreated,
            token1Address,
            token1Symbol,
            token2Address,
            token2Symbol):
    db.addPool.main(con, net,
                    netShort,
                    netExtra,
                    poolMainContract,
                    poolAddress,
                    timeCreated,
                    token1Address,
                    token1Symbol,
                    token2Address,
                    token2Symbol)


def getAllPools():
    return db.getAllPools.main(con)


def printAllPools():
    db.printAllPools.main(con)


def getPoolByAddress(address):
    return db.getPoolByAddress.main(con, address)


def getPoolsByTokenAddress(address):
    return db.getPoolsByTokenAddress.main(con, address)


def getPoolsByTokenSymbol(symbol):
    return db.getPoolsByTokenSymbol.main(con, symbol)


def deleteByAddress(address):
    db.deleteByAddress.main(con, address)


def countPools():
    return db.countPools.main(con)


def checkIfSaved(address):
    return db.checkIfSaved.main(con, address)
