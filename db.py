import psycopg2
from urllib.parse import urlparse

from db_credentials import DB_URI


def setup_connection():
    """
    Setup the connection for the database
    :return:
    """
    result = urlparse(DB_URI)

    username = result.username
    password = result.password
    database = result.path[1:]
    hostname = result.hostname
    connection = psycopg2.connect(
        database=database,
        user=username,
        password=password,
        host=hostname
    )

    return connection


def create_table(cur, table_name):
    """
    Create a table with a primary key and add it to the database
    :param cur:
    :param table_name:
    :return:
    """
    cur.execute('CREATE TABLE IF NOT EXISTS {0} ("id" SERIAL PRIMARY KEY)'.format(table_name))


def add_col(cur, table, col_name):
    """
    add a col to a certain table by a name.
    :param cur:
    :param table:
    :param col_name:
    :return:
    """
    pass


def add_row(cur, table):
    """
    add a row to a certain table.
    :param cur:
    :param table:
    :return:
    """
    pass
