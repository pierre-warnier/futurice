
# coding: utf-8

# In[1]:

import pandas as pd
from sklearn import metrics
import re
import StringIO

data_file = 'old_projects_dataset.csv'

# remove inconsistencies in whitespaces found in the input file
r = re.compile('\s+')
cleaned_file_as_string = '\n'.join(r.sub('', line) for line in open(data_file))

# create a DataFrame from the string read as a file
raw_data = pd.read_csv(StringIO.StringIO(cleaned_file_as_string), index_col='id')

# create the similarity matrix (not optimized for speed)
sim_mat = pd.DataFrame()

for l1 in raw_data.columns:
    for l2 in raw_data.columns:
        sim_mat.ix[l1, l2] = metrics.mutual_info_score(raw_data[l1], raw_data[l2])

# create a lookup table
def format_results(s):
    sorted_s = s.sort_values(ascending=False)
    return '\n'.join("%.7f,%s" %(score, label) for label,score in sorted_s.iteritems())

lookup_table = dict((c, format_results(sim_mat[c])) for c in sim_mat.columns)

def get_similarities(variable):
    if variable not in lookup_table:
        return "variable must be in: %s" %lookup_table.keys()
    return "mi,%s\n%s" % (variable, lookup_table[variable])
