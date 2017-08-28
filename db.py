import psycopg2
from urllib.parse import urlparse

from settings.db_credentials import DB_URI


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


def add_row(cur, table, db_dict):
    """
    add a row to a certain table.
    :param cur: connection's cursor.
    :param table: table's name.
    :param db_dict: a pair of (field: key).
    """

    # extract data
    fields = '(' + ", ".join(db_dict.keys()) + ')'
    values = str(tuple(db_dict.values()))[:-2] + ')'

    # execute query
    insert_query = "INSERT INTO {t_name} {fields} VALUES {values};"
    insert_query = insert_query.format(
        t_name=table,
        fields=fields,
        values=values
    )

    cur.execute(insert_query)


def get_random_row(cur, table):
    """This function returns a random row in the table."""

    query = "SELECT quote FROM {table} ORDER BY RANDOM() LIMIT 1".format(table)
    cur.execute(query)

    row = cur.fetchone()[0]
    if row:
        return row
