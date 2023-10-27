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