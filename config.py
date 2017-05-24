import private_config
import psycopg2


def connection():
    try:
        connect_str = private_config.my_connection()
        # use our connection values to establish a connection
        conn = psycopg2.connect(host=connect_str["host"],
                                user=connect_str["user"],
                                password=connect_str["passwd"],
                                dbname=connect_str["dbname"])
        conn.autocommit = True
        return conn
        cursor = conn.cursor()
        return cursor
    except Exception as e:
        print('Cannot connect')
        print(e)
