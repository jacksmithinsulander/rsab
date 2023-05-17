import sqlite3
import db.addPool
import db.checkIfSaved
import db.countPools
import db.deleteByAddress
import db.getAllPools
import db.getPoolByAddress
import db.getPoolsByTokenAddress
import db.getPoolsByTokenSymbol
import db.printAllPools

# Real data
con = sqlite3.connect("db/foundPools.db")

# # Mock data
# con = sqlite3.connect("mockdata/foundPools.db")
# conPassedFA = sqlite3.connect("mockdata/passedFa.db")

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

with con:
    con.execute("""
        CREATE TABLE if not exists pools(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            net TEXT,
            netShort TEXT,
            netExtra TEXT,
            poolMainContract TEXT,
            poolAddress TEXT UNIQUE,
            timeCreated INTEGER,
            token1Address TEXT,
            token1Symbol TEXT,
            token2Address TEXT,
            token2Symbol TEXT
        );
    """)

# with conPassedFA:
#     conPassedFA.execute("""
#         CREATE TABLE if not exists pools(
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             net TEXT,
#             netShort TEXT,
#             netExtra TEXT,
#             poolMainContract TEXT,
#             poolAddress TEXT UNIQUE,
#             timeCreated INTEGER,
#             token1Address TEXT,
#             token1Symbol TEXT,
#             token2Address TEXT,
#             token2Symbol TEXT
#         );
#     """)


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


def addPoolToPassedFA(net,
                      netShort,
                      netExtra,
                      poolMainContract,
                      poolAddress,
                      timeCreated,
                      token1Address,
                      token1Symbol,
                      token2Address,
                      token2Symbol):
    db.addPool.main(conPassedFA, net,
                    netShort,
                    netExtra,
                    poolMainContract,
                    poolAddress,
                    timeCreated,
                    token1Address,
                    token1Symbol,
                    token2Address,
                    token2Symbol)
