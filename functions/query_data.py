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
    c.execute('SELECT jobreq_no, plate_no, sticker_no, appoint FROM tb_jobreq WHERE jobreq_no NOT IN (SELECT jobreq_no FROM tb_jobest) AND jobcont = 1 AND jobreq_stat = 0 AND jobreq_date >= DATEADD(day, -7, GETDATE()) ORDER BY jobreq_date DESC;')
    counter_data = c.fetchall()

    c.execute('SELECT jr.jobreq_no, jr.plate_no, jr.sticker_no, jr.appoint FROM tb_jobreq jr INNER JOIN (SELECT plate_no, MAX(transact_date) AS latest_date FROM tb_jobest GROUP BY plate_no) je ON jr.plate_no = je.plate_no WHERE jr.jobreq_no IN (SELECT jobreq_no FROM tb_jobest) AND jr.jobcont = 1 AND jr.jobreq_stat = 0 AND jr.jobreq_date >= DATEADD(day, -7, GETDATE()) ORDER BY je.latest_date DESC;')
    progress_data = c.fetchall()

    c.execute('SELECT jr.jobreq_no, jr.plate_no, jr.sticker_no, jr.appoint FROM tb_jobreq jr INNER JOIN (SELECT user_id, MAX(time) AS latest_date FROM tb_jobreq_technician GROUP BY userid) jrtech ON jr.user_id = jrtech.user_id WHERE jr.jobreq_no IN (SELECT jobreq_no FROM tb_jobest) AND jr.jobreq_no IN (SELECT jobreq_no FROM tb_repair WHERE jobreq_no = repair_no) AND jr.jobcont = 1 AND jr.jobreq_stat = 1 AND jr.jobreq_date >= DATEADD(day, -7, GETDATE()) ORDER BY jrtech.latest_date DESC;')
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