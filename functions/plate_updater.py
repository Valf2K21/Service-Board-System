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

# import user-created dependencies
from functions.query_data import query_data
from functions.internal_deduplicator import internal_deduplicator
from functions.external_deduplicator import external_deduplicator
from functions.plate_preparator import plate_preparator

# create a function to destroy and recreate currently displayed plates
def plate_updater():
    # call query_data() function and receive results into three variables
    counter_df, progress_df, completed_df = query_data()

    # call internal_deduplicator() function to remove duplicates inside each service state's dataframe
    counter_df = internal_deduplicator(counter_df)
    progress_df = internal_deduplicator(progress_df)
    completed_df = internal_deduplicator(completed_df)

    # call external_deduplicator() function to remove duplicates outside each service state's dataframe
    counter_df = external_deduplicator(counter_df, progress_df, completed_df)
    progress_df = external_deduplicator(progress_df, completed_df, counter_df)
    completed_df = external_deduplicator(completed_df, counter_df, progress_df)

    # call plate_preparator() function to turn each service state's dataframe into list of lists
    counter_plates = plate_preparator(counter_df)
    progress_plates = plate_preparator(progress_df)
    completed_plates = plate_preparator(completed_df)

    # save the list of lists results of the three service states into a jsonifiable dictionary
    all_plates = {'counter': counter_plates, 'progress': progress_plates, 'completed': completed_plates}

    # return dictioary result
    return all_plates