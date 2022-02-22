# -*- coding: utf-8 -*-

"""
Created on Sat Jul 17 16:09:52 2021
"""

# Your name: Susan Cheng
# Your student id: 43830881
# Your email: schengg@umich.edu
# List who you have worked with on this project:

import io
from multiprocessing.sharedctypes import Value
import sys
import csv
import unittest


# Question 1
def load_csv(file):
    '''
    Reads in the csv, removes the header (first row) and
    stores the data in the following nested dictionary format:
    {'region': {'ethnicity': count...}...}

    Parameters
    ----------
    file: string
        the file to read

    Returns
    -------
    data_dict: dict
        a nested dictionary
    '''
    data_dict = {}

    with open(file, 'r') as csv_file:

        data = csv.DictReader(csv_file, delimiter = ",")

        for row in data:
            data_dict[row["Region"]] = {}
            for key in row.keys():
                if key != "Region":
                    data_dict[row["Region"]][key] = int(row[key])
    
    return (data_dict)


# Question 2
def get_perc(data_dict):
    '''
    Calculate the percentage of each demographic using this
    formula: (demographic / total people) * 100

    Parameters
    ----------
    data_dict: dict
        Either AP or Census data

    Returns
    -------
    pct_dict: dict
        the dictionary that represents the data in terms of percentage share
        for each demographic for each region in the data set
    '''
    pct_dict = {}

    for region in data_dict.keys():
        pct_dict[region] = {}
        for i in data_dict[region].keys():
            if i != "Region Totals":
                pct_dict[region][i] = round(int(data_dict[region][i]) / int(data_dict[region]["Region Totals"]) * 100, 2)
            
    return (pct_dict)


# Question 3
# (census_data) - (ap_data)
def get_diff(ap_data, census_data):
    '''
    Takes the absolute value, rounded to 2 deicmal places,
    of the difference between each demographic's percentage
    value in census_data from ap_data

    Parameters
    ----------
    ap_data: dict
        AP data
    census_data: dict
        Census data

    Returns
    -------
    pct_dif_dict: dict
        the dictionary of the percent differences
    '''
    pct_dif_dict = {}

    for region in census_data.keys():
        pct_dif_dict[region] = {}
        for demo in census_data[region].keys():
            if demo != "NO RESPONSE" and demo != "Region Totals":
                value = census_data[region][demo] - ap_data[region][demo]
                pct_dif_dict[region][demo] = abs(round(value, 2))

    return(pct_dif_dict)


# Question 4
def write_csv(data_dict, file_name):
    '''
    Writes the data to csv, adding the header as
    the first row

    Parameters
    ----------
    data_dict: dict
        dictionary with percent differences (pct_dif_dict)

    file_name: str
        the name of the file to write

    Returns
    -------
    None. (Doesn't return anything)
    '''

    with open(file_name, "w", newline="") as fileout:
        
        header = ["Region"] + list(data_dict["midwest"].keys())

        line = header[0]
        for i in range(len(header)):
            if i > 0:
                line += "," + header[i]
        line += "\n"
        fileout.write(line)
        
    
        for region in data_dict.keys():
            line = region
            for demo in data_dict[region].keys():
                line += "," + str(data_dict[region][demo])
            line += "\n"
            fileout.write(line)


def max_min_mutate(data_dict, col_list):
    # Do not change the code in this function
    # edit this code
    '''
    Mutates the data to simplify sorting

    Parameters
    ----------
    data_dict : dict
        dictionary of data passed in. In this case, it's the
    col_list : list
        list of columns to mutate to.

    Returns
    -------
    demo_vals: dict
    '''
    # Do not change the code in this function
    demo_vals = {}
    for demo in col_list:
        demo_vals.setdefault(demo, {})
        for region in data_dict:
            demo_vals[demo].setdefault(region, data_dict[region][demo])
    return demo_vals


# Question 5
def min_max(data_dict):
    '''
    Finds the max and min regions and vals for each demographic,
    filling a dictionary in the following format:
    {"max": {"demographic": {"region": value...}...} "min": {demographic: {"region": value}...}...}

    Parameters
    ----------
    data_dict: dict
        the data_dictionary you're passing in. In this case, the mutated dict

    Returns
    -------
    min_max: dict
        a triple nested dict with the this basic format
        {"max":{demographic:{"region":value}}}
    '''
    min_max = {}

def nat_perc(data_dict, col_list):
    '''
    EXTRA CREDIT
    Uses either AP or Census data dictionaries
    to sum demographic values, calculating
    national demographic percentages from regional
    demographic percentages

    Parameters
    ----------
    data_dict: dict
        Either AP or Census data
    col_list: list
        list of the columns to loop through. helps filter out region totals cols

    Returns
    -------
    data_dict_totals: dict
        dictionary of the national demographic percentages

    '''
    data_dict = {}

def nat_diff(data_dict1, data_dict2):
    '''
    EXTRA CREDIT
    Calculates the difference between AP and Census
    data on a national scale

    Parameters
    ----------
    data_dict1: dict
        Either national AP or national Census data
    data_dict2: dict
        Either national AP or national Census data

    Returns
    nat_diff: dict
        the dictionary consisting of the demographic difference on natl. level
    '''
    nat_diff = {}

def main():
    # read in the data

    # compute demographic percentages

    # computing the difference between test taker and state demographics

    # outputing the csv
    write_csv(pct_dif_dict, "HW5V1.csv")

    # creating a list from the keys of inner dict
    col_list = list(pct_dif_dict["west"].keys())

    # mutating the data
    mutated = max_min_mutate(pct_dif_dict, col_list)

    # calculating the max and mins
    min_max(mutated)

    # extra credit
    # providing a list of col vals to cycle through
    col_list = census_data["west"].keys()

    # computing the national percentages
    ap_nat_perc = nat_perc(ap_data, col_list)
    census_nat_perc = nat_perc(census_data, col_list)

    # computing the difference between them
    dif = nat_diff(ap_nat_perc, census_nat_perc)
    print("Difference between AP Comp Sci A and national demographics:\n", dif)

main()

# unit testing
# Don't touch anything below here
# create 4 tests
class HWTest(unittest.TestCase):

    def setUp(self):
        # surpressing output on unit testing
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        # setting up the data we'll need here
        # basically, redoing all the stuff we did in the main function
        self.ap_data = load_csv("region_ap_data.csv")
        self.census_data = load_csv("region_census_data.csv")

        self.ap_pct = get_perc(self.ap_data)
        self.census_pct = get_perc(self.census_data)

        self.pct_dif_dict = get_diff(self.ap_pct, self.census_pct)

        self.col_list = list(self.pct_dif_dict["midwest"].keys())

        self.mutated = max_min_mutate(self.pct_dif_dict, self.col_list)

        self.max_min_val = min_max(self.mutated)

        # extra credit
        # providing a list of col vals to cycle through
        self.col_list = self.census_data["midwest"].keys()

        # computing the national percentages
        self.ap_nat_pct = nat_perc(self.ap_data, self.col_list)
        self.census_nat_pct = nat_perc(self.census_data, self.col_list)

        self.dif = nat_diff(self.ap_nat_pct, self.census_nat_pct)

    # testing the csv reading func is working properly
    def test_load_csv(self):
         test = load_csv("region_ap_data.csv")

         self.assertEqual(test["west"]["ASIAN"], 7477)

    # testing the get_perc function
    def test_get_perc(self):
        self.assertEqual(get_perc({"region":{"demo":5,"Region Totals":10}}),
                         {"region":{"demo": 50.0}})

    # second test on the get_perc function
    # fails because my value is wrong (doh!)
    def test2_get_perc(self):
        self.assertEqual(
            self.ap_pct["midwest"]['AMERICAN INDIAN/ALASKA NATIVE'],
            0.29)

    # testing the get_diff function
    def test_get_diff(self):
        self.assertEqual(
            get_diff({"region":{"demo":50.0}},{"region":{"demo":50.0}}),
            {'region': {'demo': 0.0}}
            )

    # second test on the get_diff function
    # needs a valid value though brah
    def test2_get_diff(self):
        self.assertEqual(
            self.pct_dif_dict["west"]["AMERICAN INDIAN/ALASKA NATIVE"],
            1.51)

    # testing the max_min function
    def test_min_max(self):
        self.assertEqual(
            min_max({"demo":{"a":1,"b":2,"c":3,"d":4,"e":5}})
            ,
            {'max': {'demo': {'e': 5, 'd': 4, 'c': 3, 'b': 2, 'a': 1}},
             'min': {'demo': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}}}
            )

    # second test on the max_min function
    def test2_min_max(self):
        self.assertEqual(
            self.max_min_val["max"]["BLACK"]["west"],
            3.47)

    # testing the nat_pct extra credit function
    def test_nat_perc(self):
       self.assertEqual(
       nat_perc({"region":{"demo":5,"Region Totals":10}},["demo", "Region Totals"]),
       {"demo":50.0, "Region Totals":10})

    # second test for the nat_pct extra credit function
    def test2_nat_perc(self):
        self.assertEqual(
            self.ap_nat_pct["AMERICAN INDIAN/ALASKA NATIVE"],
            0.3)

    # testing the nat_dif extra credit function
    def test_nat_diff(self):
        self.assertEqual(
            nat_diff({"demo":0.53, "Region Totals": 1},{"demo":0.5, "Region Totals": 1}),
            {"demo":0.03}
            )

    # second test for the nat_diff extra credit function
    def test2_nat_diff(self):
        self.assertEqual(
            self.dif["ASIAN"],
            28.2)

if __name__ == '__main__':
    unittest.main(verbosity=2)