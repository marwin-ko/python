"""
    Author:
    Date Created:
    Date Last Modified:
    Python Version:
"""

import psycopg2
import pandas pd

# set these variables: host, database, user, password, port (if necessary)
conn = psycopg2.connect(host, database, user, password, port)
df = pd.read_sql_query(query, conn)
