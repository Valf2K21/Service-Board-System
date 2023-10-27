# import dependencies
from datetime import datetime

# define a function for date getting process
def get_time():
    # get current time in this format: Monday, 12/31/2023 23:59:59
    currentTime = datetime.now().strftime('%A, %m/%d/%Y %H:%M:%S')

    # return fetched time
    return currentTime