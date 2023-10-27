# import dependencies
import pandas as pd

# create a function to check duplicates outside each service state's dataframe
def external_deduplicator(state_data, external_data1, external_data2):
    # create a function inside this function that is the actual external deduplicator
    def execute_deduplicator(state_data, external_data):
        # for-loop to loop through all unique conents of submitted dataframe's plate_no column
        for plate in state_data['plate_no'].unique():
            # create two new dataframes containing rows of detected duplicates of the current plate on state_data and external_data
            plate_duplicates1 = state_data[state_data['plate_no'] == plate]
            plate_duplicates2 = external_data[external_data['plate_no'] == plate]

            # if-statement to check if there are detected duplicates of currently-iterated plate
            if len(plate_duplicates1) + len(plate_duplicates2) > 1:
                # store the highest jobreq_no value of the current plate in a variable
                highest_jobreq_no = max(plate_duplicates1['jobreq_no'].max(), plate_duplicates2['jobreq_no'].max())

                # for-loop to loop through all rows of plate_duplicates1 using iterrows() function
                for index, row in plate_duplicates1.iterrows():
                    # if-statement to check if currently-iterated jobreq_no is not equal to highest_jobreq_no
                    if row['jobreq_no'] != highest_jobreq_no:
                        # drop currently-iterated row
                        state_data = state_data.drop(index)
        # return deduplicated dataframe result
        return state_data

    # if-statement to check if submitted dataframe is not empty
    if not state_data.empty:
        # if-statement to check if submitted external dataframe 1 is not empty
        if not external_data1.empty:
            state_data = execute_deduplicator(state_data, external_data1)
        
        # if-statement to check if submitted external dataframe 2 is not empty
        if not external_data2.empty:
            state_data = execute_deduplicator(state_data, external_data2)
    
    # return deduplicated dataframe result
    return state_data