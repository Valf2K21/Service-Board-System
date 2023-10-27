# import dependencies
import pandas as pd

# create a function to check duplicates inside each service state's dataframe
def internal_deduplicator(state_data):
    # if-statement to check if submitted dataframe is not empty
    if not state_data.empty:
        # for-loop to loop through all unique conents of submitted dataframe's plate_no column
        for plate in state_data['plate_no'].unique():
            # create a new dataframe containing rows of detected duplicates of the current plate
            plate_duplicates = state_data[state_data['plate_no'] == plate]

            # if-statement to check if there are detected duplicates of currently-iterated plate
            if len(plate_duplicates) > 1:
                # store the highest jobreq_no value of the current plate in a variable
                highest_jobreq_no = plate_duplicates['jobreq_no'].max()

                # for-loop to loop through all rows of plate_duplicates using iterrows() function
                for index, row in plate_duplicates.iterrows():
                    # if-statement to check if currently-iterated jobreq_no is not equal to highest_jobreq_no
                    if row['jobreq_no'] != highest_jobreq_no:
                        # drop currently-iterated row
                        state_data = state_data.drop(index)

    # return deduplicated dataframe result
    return state_data