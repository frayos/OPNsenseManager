import sqlite3

mydb = sqlite3.connect("rules.db", check_same_thread=False)
db = mydb.cursor()


def create_tables():
    db.execute("""CREATE TABLE  IF NOT EXISTS rules(
    id integer PRIMARY KEY,
    rname TEXT,
    uuid TEXT NOT NULL UNIQUE
    );""")

    db.execute("""CREATE TABLE IF NOT EXISTS api_info(
    id integer PRIMARY KEY,
    profile_id INTEGER,
    api_key TEXT NOT NULL,
    api_secret TEXT NOT NULL,
    url TEXT NOT NULL,
    port INTEGER,
    password BLOB,
    FOREIGN KEY (profile_id) REFERENCES profiles(id)
    );""")

    db.execute("""CREATE TABLE IF NOT EXISTS profiles(
    id integer PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
    );""")