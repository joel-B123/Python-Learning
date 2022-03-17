###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:
from typing import List, Any

from ps1_partition import get_partitions
from time import process_time
import re
import operator
from collections import OrderedDict
#================================
# Part A: Transporting Space Cows
#================================


# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # open the file
    #   use 'open' function
    # create a list with each line of the file being an item of the list
    #   eliminate newline symbol from file line import
    #       define the "list" with 'map' function
    #       remove symbol from each line using 'lambda' function and 're.sub' function
    # create dictionary using list of lines
    #   split each item of list at the comma
    #       define the "dictionary" with 'map' function
    #       split each item of the "list" using 'lambda' function and 'split' function
    # update the dictionary by converting numerical string(dict.value) with corresponding integer
    #   update the "dictionary" using 'update' function
    # return resulting "dictionary"
    cows = open(filename, "r")
    lines = list(map(lambda x: re.sub("\n", "", x), cows))
    result = dict(map(lambda tup: tup.split(","), lines))
    (result.update((k, int(result.get(k))) for k in result))
    sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    return OrderedDict(sorted_result)


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # create helper function for list creation
    #   helper function use 'dict' and 'var'(max_weight) as parameters
    #   iterate through the 'dict', the largest value to the smallest value
    #   add cows in order of heaviest to lightest, keeping under the weight limit
    # create empty 'list' for main return
    #   create loop for running helper function to create 'lists'
    #   add each complete 'list' from helper function to a 'list' of all 'lists'
    #   remove items of each 'list' from copy of 'dict'
    #       use a 'for' loop to iterate through each item in current 'list'
    # return 'list' of all 'lists'

    def weigh_in(cargo, max_weight):
        """
        helper function to loop through 'dict' and produce a list of which cows can be transported on each shipment
        without going over the weight limit.
        parameters;
        cargo: dictionary of cows and weights
        max-weight: integer, representing total weight allowed in each list being returned
        :return: list of cows being shipped
        """
        transport_list = []
        cow_weights = []
        for key in cargo.keys():
            current_weight = cargo.get(key)
            ship_weight = sum(cow_weights)
            if current_weight <= (max_weight - ship_weight):
                transport_list.append(key)
                cow_weights.append(cargo.get(key))
            if ship_weight == max_weight:
                break
        return transport_list

    shipments = []
    cows2 = cows.copy()
    while len(cows2) > 0:
        shipment = weigh_in(cows2, limit)
        shipments.append(shipment)
        for i in shipment:
            cows2.pop(i)
    return shipments


# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    # define function for comparing weight
    def weigh(a_list: list, max_weight: int):
        """
        iterates through list adding together value of each position and comparing it to the max_weight allowed.

        param: max_weight(integer) representing the max a ship can handle

        param: a_list(list) of integers

        return: True if total weight of 'a_list' is equal to or less than max weight. Returns False otherwise.
        """
        # iterate through 'list' passed in
        #   use 'for' loop
        # add integers in 'list' together(integer) and compare to 'max_weight'(integer)
        # if the total of 'list'(integer) is larger than 'max_weight'(integer) then return False
        #   otherwise return True
        for i in a_list:
            if sum(i) > max_weight:
                return False
        return True

    # define function for finding the key associated with value from dictionary
    def get_key(number: int, my_dict: dict):
        """
        compares dictionary values with list of values to return the key associated with the value.

        param my_dict: copy of original dictionary

        param number: integer from list passed in

        return: a key(string) from dictionary
        """
        # loop through dictionary
        # compare value passed in against values in dictionary
        # if a match is found, return key
        for key, val in my_dict.items():
            if val == number:
                return key

    # create deep copy of 'dict'
    # create list of values from 'dict'
    # get list of permutations using 'get_partitions' function
    # create empty 'list'
    #   'list is for compiling the 'lists' that meet the requirements
    # loop through item of 'list' of 'lists'
    #   use 'for' loop
    #   add 'lists' that meet requirements to new 'list' of 'lists'
    # find 'list' that has the minimum number of 'lists' and create a 'list' of 'lists'
    # create empty 'list' of 'lists'
    # loop though each 'list' in 'list' of 'lists'
    #   use 'for' loop
    #   create empty single 'list'
    #   loop through 'integers' in 'list'
    #       use 'for' loop
    #       assign variable to return from "get_key" function
    #       add variable key to 'list'
    #       remove variable key from copy of dictionary
    #   add 'list' of keys to final 'list' of 'lists'
    # return final 'list' of 'lists'
    cows2 = cows.copy()
    l_values = list(cows.values())
    l_partitions = list(get_partitions(l_values))
    res = []
    for item in l_partitions:
        res.append(item) if weigh(item, limit) else False
    [result] = [min(res, key=len)]
    fin_result = []
    for shipment in result:
        transport_list = []
        for value in shipment:
            x = get_key(value, cows2)
            transport_list.append(x)
            cows2.pop(x)
        fin_result.append(transport_list)
    return fin_result


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # start process time
    # print return from function 'greedy_cow_transport'
    # stop process time
    # print total time to complete 'function' in seconds
    #   difference between stop time minus start time
    # start process time
    # print return from function 'brute_force_cow_transport'
    # stop process time
    # print total process time
    #   difference between stop time minus start time
    t1_start = process_time()
    print(greedy_cow_transport(load_cows("ps1_cow_data.txt"), 10))
    t1_stop = process_time()
    print("Time elapsed for 'greedy_cow_transport' is", (t1_stop - t1_start), "seconds")
    t1_start = process_time()
    print(brute_force_cow_transport(load_cows("ps1_cow_data.txt"), 10))
    t1_stop = process_time()
    print("Time elapsed for 'brute_force_cow_transport' is", (t1_stop - t1_start), "seconds")
    # repeat lines 195 - 204 on different text file
    t1_start = process_time()
    print(greedy_cow_transport(load_cows("ps1_cow_data_2.txt"), 10))
    t1_stop = process_time()
    print("Time elapsed for 'greedy_cow_transport' is", (t1_stop - t1_start), "seconds")
    t1_start = process_time()
    print(brute_force_cow_transport(load_cows("ps1_cow_data_2.txt"), 10))
    t1_stop = process_time()
    print("Time elapsed for 'brute_force_cow_transport' is", (t1_stop - t1_start), "seconds")


compare_cow_transport_algorithms()
