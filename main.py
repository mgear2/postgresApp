# pylint: disable=import-error
import sys
import psycopg2
from src.connector import Connector
from src.browser import Browser

if __name__ == "__main__":
    if len(sys.argv) > 1:
        database = sys.argv[1]
    else:
        database = "postgres"

    connector = Connector(database)
    connector.connect()
    browser = Browser(connector)
    browser.commandrunner()
    connector.disconnect()
