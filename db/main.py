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

con = sqlite3.connect("db/foundPools.db")

with con:
    con.execute("""
        CREATE TABLE if not exists pools(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            net TEXT,
            poolContract TEXT,
            poolAddress TEXT UNIQUE,
            timeCreated INTEGER,
            token1Address TEXT,
            token1Symbol TEXT,
            token2Address TEXT,
            token2Symbol TEXT
        );
    """)

def addPool(net,
            poolContract,
            poolAddress,
            timeCreated,
            token1Address,
            token1Symbol,
            token2Address,
            token2Symbol):
    db.addPool.main(con, net,
            poolContract,
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