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

# Part 3
# functions will find the population per some parameter.
# input list output float
# functino will take the population of the county and multiply it by the percent of people that fit the value parameter
# this will then return the total population as a float for that parameter.

def population_by_education(lst:list[CountyDemographics], value:str)-> float:
    total = 0
    for county in lst:
        if value in county.education:
            total = total + (county.population.get('2014 Population') * county.education.get(value)/100)

    return float(total)

def population_by_ethnicity(lst: list[CountyDemographics], value: str) -> float:
    total = 0
    for county in lst:
        if value in county.ethnicities:
            total = total + (county.population.get('2014 Population') * county.ethnicities.get(value) / 100)

    return float(total)

def population_below_poverty_level(lst: list[CountyDemographics]) -> float:
    total = 0
    for county in lst:
        total = total + (county.population.get('2014 Population') * county.income.get('Persons Below Poverty Level') / 100)

    return float(total)