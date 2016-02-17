
# coding: utf-8

# In[2]:

import unicodecsv

with open('lahman-csv_2015-01-24/batting.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    batting = list(reader)

batting[0]


# In[3]:

from datetime import datetime as dt

def parse_maybe_int(i):
    if i == '':
        return None
    else: 
        return int(i)
    
def parse_date(i):
    if date == '':
        return None
    else: 
        return dt.strptime(data, '%Y-%m-%d')
    


# In[4]:

for bat in batting:
    bat['G'] = parse_maybe_int(bat['G'])
    bat['AB'] = parse_maybe_int(bat['AB'])
    bat['R'] = parse_maybe_int(bat['R'])
    bat['H'] = parse_maybe_int(bat['H'])
    bat['2B'] = parse_maybe_int(bat['2B'])
    bat['3B'] = parse_maybe_int(bat['3B'])
    bat['HR'] = parse_maybe_int(bat['HR'])
    bat['RBI'] = parse_maybe_int(bat['RBI'])
    bat['SB'] = parse_maybe_int(bat['SB'])
    bat['CS'] = parse_maybe_int(bat['CS'])
    bat['BB'] = parse_maybe_int(bat['BB'])
    bat['SO'] = parse_maybe_int(bat['SO'])
    bat['IBB'] = parse_maybe_int(bat['IBB'])
    bat['HBP'] = parse_maybe_int(bat['HBP'])
    bat['SH'] = parse_maybe_int(bat['SH'])
    bat['SF'] = parse_maybe_int(bat['SF'])
    bat['GIDP'] = parse_maybe_int(bat['GIDP'])

batting[0]
    


# In[5]:

#method to sum certain "columns" chosen in a key_list in a dictionary list (get sums of runs, etc..)

def sum_columns(key_list, dictionary_list):
    batting_totals_dictionary = {}
    for key in key_list:
        total_sum = 0
        for i in dictionary_list:
            if i[key] is not None: 
                total_sum += i[key] 
        batting_totals_dictionary[key] = total_sum
    return batting_totals_dictionary


#method to get the averages of the totals in a dictionary  

def divide_dictionary(num_dict, divisor):
    for key, value in num_dict.items():
        num_dict[key] = value / divisor
    return num_dict
    
    
        


# In[6]:

##column = 'RBI'
##print sum(row[column] for row in batting)

#type(batting[0]['RBI']) is int



#print batting[0]['RBI'] + batting[1]['RBI']

key_list = ['RBI', 'R', 'H', 'HR']
total_sums = sum_columns(key_list, batting) 

print total_sums

length = len(batting)

print length

averages = divide_dictionary(total_sums, length)

print averages

#print col_totals


# In[15]:

#Print Total Runs by Team ID

from collections import defaultdict

d = defaultdict(int)

for item in batting:
      d[item['teamID']] += item.get('R', 0) or 0

#d = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
#d = sorted(d, key=d.get, reverse=True)        
        
for team, r_sum in d.items():
    print team, r_sum


# In[28]:

#Print Total Runs By Year

from collections import defaultdict

new_dict = defaultdict(int)

for item in batting:
      new_dict[item['yearID']] += item.get('R', 0) or 0        
        

for year, r_sum in sorted(new_dict.iterkeys()): 
    print year, r_sum
        
#for year, r_sum in new_dict.items():
#    print year, r_sum
    
#print sorted(new_dict.items())


# In[17]:

#Average runs per team

import numpy as np

total_runs_by_team = d.values()

np.mean(total_runs_by_team) 


# In[20]:

#Average runs per year

import numpy as np

total_runs_by_year = new_dict.values()

print np.mean(total_runs_by_year) 
print np.std(total_runs_by_year)
print np.min(total_runs_by_year)
print np.max(total_runs_by_year)


# In[ ]:



