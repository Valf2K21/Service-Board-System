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
import pandas as pd

# create a function to prepare plates and set their respective colors
def plate_preparator(state_data):
    # store jobreq_no values as index in a variable
    index_column = state_data['jobreq_no']

    # create a list to store each column of the state_data dataframe into a list of list of lists
    big_list = []

    # for-loop to loop through the jobreq_no values of index_column
    for index in index_column:
        # store list version of row from state_data that matches currently-iterated index to a variable
        data_grab = state_data.loc[state_data['jobreq_no'] == index, ['plate_no', 'sticker_no', 'appoint']].values.tolist()

        # append data_grab to big_list
        big_list.append((data_grab))

    # create a list to store converted big_list's list of list of lists into list of list
    generator_data = []

    # for-loop to loop through the contents of big_list
    for small_list in big_list:
        # append current index of 0 of small_list to generator_data
        generator_data.append(small_list[0])

    # return list result
    return generator_data