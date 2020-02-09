import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def dict_creator(file):
    """
    Creates a Dictionary containing all the values with the first value as the
    key
    """
    large_lst = []
    final_dict = {}
    f = open(file, 'r')
    for i in f.readlines():
        stats = i.split(',')
        large_lst.append(stats)
    for i in large_lst:
        i[-1] = i[-1][:-1]
        final_dict[i[0]] = i[1:]
    return final_dict


def list_creator(file):
    """
    Creates a list which contains each row as a seperate list
    """
    lst = []
    f = open(file, 'r')
    for i in f.readlines():
        stats = i.split(',')
        lst.append(stats)
    return lst


def male_columns(lst):
    males = []
    male_indexes = []
    for i in lst[:48]:
        if 'male' in i.lower() and 'female' not in i.lower():
            males.append(i)
    for i in males:
        male_indexes.append(lst.index(i))
    print(males)
    return male_indexes


def female_columns(lst):
    females = []
    female_indexes = []
    for i in lst[:48]:
        if 'female' in i.lower():
            females.append(i)
    for i in females:
        female_indexes.append(lst.index(i))
    print(females)
    return female_indexes


def males_per_row():
    male_totals = []
    for i in range(len(population_lst)):
        male_totals.append(population_lst[i][4:26])
    return male_totals


def females_per_row():
    female_totals = []
    for i in range(len(population_lst)):
        female_totals.append(population_lst[i][26:48])
    return female_totals


def total_females_per_row():
    female_totals = []
    for i in females_per_row()[1:]:
        ints = []
        for j in i:
            if j == '...':
                ints.append(0)
            else:
                ints.append(int(j))
        female_totals.append(sum(ints))
    return female_totals


def total_males_per_row():
    male_totals = []
    for i in males_per_row()[1:]:
        ints = []
        for j in i:
            if j == '...':
                ints.append(0)
            elif j[-1] == '"':
                ints.append(int(j[:-1]))
            else:
                ints.append(int(j))
        male_totals.append(sum(ints))
    return male_totals


def unique_housing_places():
    initial, unique = [], []
    for i in housing_lst:
        initial.append(i[2])
    for j in initial:
        if j not in unique:
            unique.append(j)
    return unique


def population_per_area():
    dict = {}
    for i in unique_housing_places():
        pop_list = []
        for j in housing_lst[1:]:
            if i == j[2]:
                if j[3][0] == '"':
                    pop_list.append(int(j[3][1:]))
                else:
                    pop_list.append(int(j[3]))
        dict[i] = sum(pop_list)
    return dict
    

housing_dict = dict_creator("SD1970_housing.csv")
population_dict = dict_creator("SD1970_population.csv")
housing_lst = list_creator("SD1970_housing.csv")
population_lst = list_creator("SD1970_population.csv")
housing_pd = pd.read_csv('SD1970_housing.csv', thousands=',')
population_pd = pd.read_csv('SD1970_population.csv', thousands=',')
population_with_totals = population_pd
population_with_totals.insert(155, 'Total Male Persons', total_males_per_row())
population_with_totals.insert(156, 'Total Female Persons', total_females_per_row())
population_pd = pd.read_csv('SD1970_population.csv', thousands=',')

