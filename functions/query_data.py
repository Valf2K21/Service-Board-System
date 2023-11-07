'''
    The Service Board System is a web application for monitoring vehicle maintenance status according to three states: counter, in progress, and completed.
    Copyright (C) 2023 Valfrid Galinato
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

# import dependencies
import psycopg2
import pandas as pd

# import user-created dependencies
from .config import config

# create a function to gather and prepare data for further processing
def query_data():
    # call config() function and store server parameters in a variable
    params = config()

    # use psycopg2.connect() function to connect to PostgreSQL server
    # note: ** means we want to extract the values of the returned dictionary stored in params variable
    conn = psycopg2.connect(**params)

    # use conn.cursor() function to create a cursor for SQL command execution
    c = conn.cursor()

    # use created cursor to query and fetch data for each service state
    c.execute('SELECT jobreq_no, plate_no, sticker_no, appoint FROM tb_jobreq WHERE jobreq_no NOT IN (SELECT jobreq_no FROM tb_jobest) AND jobcont = 1 AND jobreq_stat = 0 ORDER BY jobreq_date DESC;')
    counter_data = c.fetchall()

    c.execute('SELECT jr.jobreq_no, jr.plate_no, jr.sticker_no, jr.appoint FROM tb_jobreq jr INNER JOIN (SELECT sticker_no, MAX(transact_date) AS latest_date FROM tb_jobest GROUP BY sticker_no) je ON jr.sticker_no = je.sticker_no WHERE jr.jobreq_no IN (SELECT jobreq_no FROM tb_jobest) AND jr.jobcont = 1 AND jr.jobreq_stat = 0 ORDER BY je.latest_date DESC;')
    progress_data = c.fetchall()

    c.execute('SELECT jr.jobreq_no, jr.plate_no, jr.sticker_no, jr.appoint FROM tb_jobreq jr INNER JOIN (SELECT user_id, MAX(time) AS latest_date FROM tb_jobreq_technician GROUP BY user_id) jrtech ON jr.user_id = jrtech.user_id WHERE jr.jobreq_no IN (SELECT jobreq_no FROM tb_jobest) AND jr.jobreq_no IN (SELECT jobreq_no FROM tb_repair WHERE jobreq_no = repair_no) AND jr.jobcont = 1 AND jr.jobreq_stat = 1 ORDER BY jrtech.latest_date DESC;')
    completed_data = c.fetchall()

    # use pd.dataframe() function to store fetched data of each service state in their respective dataframes
    counter_df = pd.DataFrame(counter_data, columns = ['jobreq_no', 'plate_no', 'sticker_no', 'appoint'])
    progress_df = pd.DataFrame(progress_data, columns = ['jobreq_no', 'plate_no', 'sticker_no', 'appoint'])
    completed_df = pd.DataFrame(completed_data, columns = ['jobreq_no', 'plate_no', 'sticker_no', 'appoint'])

    # close cursor and connect objects after the process
    c.close()
    conn.close()

    # return dataframed results
    return counter_df, progress_df, completed_df