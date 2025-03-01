import data
from data import CountyDemographics
from build_data import get_data



# Part 1
# Function will return the total population as a number.
# Input: the full data list, Output: an int
# Function will take all the county demographics objects from the full data from 2014 and add up all the values from population.

def population_total(lst:list[CountyDemographics]) -> int:
    total = 0
    for county in lst:
        total = total + county.population.get('2014 Population')

    return total

# Part 2
# Function will filter the full data by state.
# Input the full data list of counties and a string. output: a list of county demographic objects.
# function will take all the counties that are from the same inputted county string and return them as a list of county demographic objects.

def filter_by_state(lst:list[CountyDemographics], state:str) -> list[CountyDemographics]:
    final_list = []
    for county in lst:
        if county.state == state:
            final_list.append(county)
        else:
            continue
    return final_list


