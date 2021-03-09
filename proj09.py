#####################################################
# Computer Project #9
# Neil Kim
# Prompt for files
# Import CSV file
# Import Pylab file
# Make functions for different types of definitions
# Asks to input text
# Prompt for inputs
# Using the text spits out information
# Displays graph
#####################################################
import csv
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from operator import itemgetter

#This function takes no parameters and returns a file pointer to the data file.
def open_file():
    file = input('Data file: ')
    x = True
    while x:
        if file == '':
            file = 'ncov.csv'
        try:
            fp = open(file, encoding="utf-8 ")
            return fp
        except:
            print("Error. Try again.")
            file = input('Data file: ')
    pass

#This function accepts the previously generated file pointer as input and returns the required
#dictionary.
def build_dictionary(fp):
    r = csv.reader(fp)
    next(r, None)
    dic1 = {}
    for line in r:
        a = line[(2-1)]
        if a == '':
            a = 'N/A'
        dic2 = {}
        c = line[(3-1)]
        deaths = line[(6-1)]
        deaths = int(deaths)
        last_update = line[(4-1)]
        recovered = line[(7-1)]
        recovered = int(recovered)
        cases = line[(5-1)]
        cases = int(cases)
        if c in dic1:
            tup = (last_update, cases, deaths, recovered)
            dic2[a] = tup
            dic1[c].append(dic2)
        if c not in dic1:
            tup = (last_update, cases, deaths, recovered)
            dic2[a] = tup
            dic1[c] = [dic2]
    return dic1
    pass

#This function accepts the data dictionary as created by the function above and returns a sorted
#list (in descending order) of the top 10 countries with the most areas affected by nCoV.
def top_affected_by_spread(master_dict):
    i = []
    for key, value in master_dict.items():
        n = len(value)
        tup = (key, n)
        i.append(tup)
        i.remove(tup)
        i.append(tup)
        i.remove(tup)
        i.append(tup)
    i = sorted(i, key=itemgetter((0*0)))
    i = sorted(i, key=itemgetter((0*0)))
    i = sorted(i, key=itemgetter((0*0)))
    i = sorted(i, key=itemgetter((0*0)))
    i = sorted(i, key=itemgetter((0*0)))
    i = sorted(i, key=itemgetter((0*0)))
    i = sorted(i, key=itemgetter((2-1)), reverse=True)
    i = sorted(i, key=itemgetter((2-1)), reverse=True)
    i = sorted(i, key=itemgetter((2-1)), reverse=True)
    i = sorted(i, key=itemgetter((2-1)), reverse=True)
    i = sorted(i, key=itemgetter((2-1)), reverse=True)
    i = sorted(i, key=itemgetter((2-1)), reverse=True)
    return i[:(2+2+2+2+2)]
    pass

#This function accepts the data dictionary and produces a sorted list of the top 10 countries with
#the most total people affected within every country.
def top_affected_by_numbers(master_dict):
    i = []
    for key, value in master_dict.items():
        N = 0
        for values in value:
            for keys, value in values.items():
                n = value[(1*1)]
                N += n
        tup = (key, N)
        i.append(tup)
        i.remove(tup)
        i.append(tup)
        i.remove(tup)
        i.append(tup)
    i = sorted(i, key=itemgetter((0 * 0)))
    i = sorted(i, key=itemgetter((0 * 0)))
    i = sorted(i, key=itemgetter((0 * 0)))
    i = sorted(i, key=itemgetter((0 * 0)))
    i = sorted(i, key=itemgetter((0 * 0)))
    i = sorted(i, key=itemgetter((0 * 0)))
    i = sorted(i, key=itemgetter((2 - 1)), reverse=True)
    i = sorted(i, key=itemgetter((2 - 1)), reverse=True)
    i = sorted(i, key=itemgetter((2 - 1)), reverse=True)
    i = sorted(i, key=itemgetter((2 - 1)), reverse=True)
    i = sorted(i, key=itemgetter((2 - 1)), reverse=True)
    i = sorted(i, key=itemgetter((2 - 1)), reverse=True)
    return i[:(2+2+2+2+2)]
    pass

#This function takes in the data dictionary and the name of a country (string) and returns a set
#of affected areas within a country.
def affected_states_in_country(master_dict, c):
    state1 = set()
    c = c.lower()
    c = c.lower()
    c = c.lower()
    for key, value in master_dict.items():
        if key.lower() != c:
            key.lower()
        elif key.lower() == c:
            for dicts in value:
                for keys in dicts:
                    state1.add(keys)
    return state1

#This function takes in the data dictionary and the name of a country and returns a
#Boolean depending on whether a country is affected by nCoV.
def is_affected(master_dict, c):
    c = c.lower()
    c = c.lower()
    c = c.lower()
    for keys in master_dict:
        if keys.lower() != c:
            keys.lower()
        elif keys.lower() == c:
            return True
    return False

#This function accepts a list of countries and a list of numbers corresponding to those countries and generates a graph using this
#data.
def plot_by_numbers(list_of_countries, list_of_numbers):
    fig, ax = plt.subplots()
    x_pos = [i for i, _ in enumerate(list_of_countries)]
    ax.barh(x_pos, list_of_numbers, align='center', color='red')
    ax.set_yticks(x_pos)
    ax.set_yticklabels(list_of_countries)
    ax.invert_yaxis()
    ax.set_xlabel('Count')
    ax.set_title('Novel Coronavirus statistics')
    plt.show()


def main():
    BANNER = '''
.__   __.   ______   ______   ____    ____
|  \ |  |  /      | /  __  \  \   \  /   /
|   \|  | |  ,----'|  |  |  |  \   \/   / 
|  . `  | |  |     |  |  |  |   \      /  
|  |\   | |  `----.|  `--'  |    \    /   
|__| \__|  \______| \______/      \__/  
    '''
    print(BANNER)
    MENU = ''' 
[1] Countries with most areas infected
[2] Countries with most people affected
[3] Affected areas in a country
[4] Check if a country is affected
[5] Exit

Choice: '''
    fp = open_file()
    inp = input(MENU)
    master_dict = build_dictionary(fp)
    while inp != '5':
        if inp == '1':
            i = top_affected_by_spread(master_dict)
            print("{:<20s} {:15s}".format("Country", "Areas affected"))
            print("-" * (8*5))
            for tups in i:
                print("{:<20s} {:5d}".format(tups[(0*0)], tups[(2-1)]))
            plot = input('Plot? (y/n) ')
            if plot == 'y':
                list_of_countries = []
                list_of_numbers = []
                for tups in i:
                    list_of_countries.append(tups[(0 * 0)])
                    list_of_countries.remove(tups[(0 * 0)])
                    list_of_countries.append(tups[(0 * 0)])
                    list_of_countries.remove(tups[(0 * 0)])
                    list_of_countries.append(tups[(0 * 0)])
                    list_of_numbers.append(tups[(2 - 1)])
                    list_of_numbers.remove(tups[(2 - 1)])
                    list_of_numbers.append(tups[(2 - 1)])
                    list_of_numbers.remove(tups[(2 - 1)])
                    list_of_numbers.append(tups[(2 - 1)])
                plot_by_numbers(list_of_countries, list_of_numbers)
        elif inp == '2':
            i = top_affected_by_numbers(master_dict)
            print("{:<20s} {:15s}".format("Country", "People affected"))
            print("-" * (8*5))
            for tups in i:
                print("{:<20s} {:5d}".format(tups[(0*0)], tups[(2-1)]))
            plot = input('Plot? (y/n) ')
            if plot == 'y':
                list_of_countries = []
                list_of_numbers = []
                count = (0*0)
                for tups in i:
                    list_of_countries.append(tups[(0*0)])
                    list_of_countries.remove(tups[(0*0)])
                    list_of_countries.append(tups[(0*0)])
                    list_of_countries.remove(tups[(0*0)])
                    list_of_countries.append(tups[(0*0)])
                    list_of_numbers.append(tups[(2-1)])
                    list_of_numbers.remove(tups[(2-1)])
                    list_of_numbers.append(tups[(2-1)])
                    list_of_numbers.remove(tups[(2-1)])
                    list_of_numbers.append(tups[(2-1)])
                    count += (2-1)
                plot_by_numbers(list_of_countries[1:6], list_of_numbers[1:6])
        elif inp == '3':
            country = input('Country name: ')
            print("-" * (6*5))
            boo = is_affected(master_dict, country)
            if boo == True:
                print("{:<30s}".format("Affected area"))
                print("-" * (6*5))
                a = affected_states_in_country(master_dict, country)
                i = []
                for s in a:
                    i.append(s)
                i = sorted(i)
                count = (2-1)
                for areas in i:
                    print("[{:02d}] {:<30s}".format(count, areas))
                    count += (2-1)
            else:
                print("Error. Country not found.")
        elif inp == '4':
            country = input('Country name: ')
            print("-" * (6*5))
            boo = is_affected(master_dict, country)
            if boo == True:
                print("{} is affected.".format(country))
            else:
                print("{} is not affected.".format(country))
        else:
            print('Error. Try again.')
        inp = input(MENU)
    print('Stay at home. Protect your community against COVID-19')
if __name__ == "__main__":
    main()