#Steve Sabaugh
#regex.py
#data file to be included mames.txt

import re


def find_names(line):
    pattern = r"(?![A-Z][A-Z]\,)([A-Z][a-zA-Z]+)"
    result = re.findall(pattern, line)

    return result

f = open("venv/names.txt")
count = 0
for line in f.readlines():
    #print(line)
    result = find_names(line)
    if (len(result)>0):
        print(result)
        count += 1

print('name count: ', count)
