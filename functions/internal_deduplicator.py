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

# create a function to check duplicates inside each service state's dataframe
def internal_deduplicator(state_data):
    # if-statement to check if submitted dataframe is not empty
    if not state_data.empty:
        # for-loop to loop through all unique conents of submitted dataframe's sticker_no column
        for sticker in state_data['sticker_no'].unique():
            # create a new dataframe containing rows of detected duplicates of the current sticker
            sticker_duplicates = state_data[state_data['sticker_no'] == sticker]

            # if-statement to check if there are detected duplicates of currently-iterated sticker
            if len(sticker_duplicates) > 1:
                # store the highest jobreq_no value of the current sticker in a variable
                highest_jobreq_no = sticker_duplicates['jobreq_no'].max()

                # for-loop to loop through all rows of sticker_duplicates using iterrows() function
                for index, row in sticker_duplicates.iterrows():
                    # if-statement to check if currently-iterated jobreq_no is not equal to highest_jobreq_no
                    if row['jobreq_no'] != highest_jobreq_no:
                        # drop currently-iterated row
                        state_data = state_data.drop(index)

    # return deduplicated dataframe result
    return state_data