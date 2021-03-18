"""
Here I wrote a utility function that finds min and max of n numbers with 3n/2 compares.
"""

def efficent_minmax_finder(array):
    bigger_list = []
    smaller_list = []
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            bigger_list.append(array[i+1])
            smaller_list.append(array[i])
        else:
            bigger_list.append(array[i])
            smaller_list.append(array[i+1])
    min_item = smaller_list[0]
    for item in smaller_list:
        if item<min_item:
            min_item = item
    max_item = bigger_list[0]
    for item in bigger_list:
        if item>max_item:
            max_item = item
    return min_item, max_item