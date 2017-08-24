
import psycopg2

from db_credentials import DB_NAME, DB_USER, DB_HOST, DB_PASS

connection_str = "dbname='{0} user='{1}' host='{2}' password='{3}'"

try:
    conn = psycopg2.connect(connection_str.format(DB_NAME,
                                                  DB_USER,
                                                  DB_HOST,
                                                  DB_PASS))

except:
    print ("I am unable to connect to the database")
