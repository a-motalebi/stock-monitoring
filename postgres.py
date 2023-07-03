import psycopg2


def connection():
    conn = psycopg2.connect(
        host="db", port="5432", database="hermes", user="ali", password="ali"
    )
    conn.autocommit = True

    cur = conn.cursor()

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS total_index(
        time TIMESTAMPTZ,
        index FLOAT
    )"""
    )
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS funds_index(
        time TIMESTAMPTZ,
        index FLOAT
    )"""
    )
    return cur
