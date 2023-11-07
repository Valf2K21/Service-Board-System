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
from datetime import datetime

# define a function for date getting process
def get_time():
    # get current time in this format: Monday, 12/31/2023 23:59:59
    current_time = datetime.now().strftime('%A, %m/%d/%Y %H:%M:%S')

    # return fetched time
    return current_time