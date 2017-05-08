import psycopg2


def connection():
    # setup connection string
    connect_str = "dbname='' user='' host='localhost' password=''"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    # return connection
    return conn
