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