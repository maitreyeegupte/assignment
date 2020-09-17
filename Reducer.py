#!/usr/bin/env python
"""reducer.py"""

#from operator import itemgetter
import sys

debug=False

def outputPatentInfo(key, values):

    #
    # Our inputs are either 3070801	1963,1096,,"BE","",,1,,269,6,69,,1,,0,,,,,,,
    # or 6009554	y
    #
    #
    # So the "values" either have zero commas or multiple commas
    #


    if debug:
        print("values is ", values)
        print("cites is ", cites)
        print("info is ", info)

    try:
        if values[5] == "":
            pass
        else:
            for i in values:
                print('&s\t%s\t%s' % (key,i,values[5]))
        current_patent = None
        values = []
    except:
        pass

    

def main():
    current_patent = None
    values = []

    debug = False

    # input comes from STDIN
    for line in sys.stdin:
        line = line.rstrip('\n')

        # parse the input we got from mapper.py
        try:
            key, value = line.split('\t', 1)
        except:
            print('Improperly formatted: *', line, '*')
            # Improperly formatted, so ignore
            continue

        # convert count (currently a string) to int
        try:
            patent = int(key)
        except ValueError:
            # key was not a number, so silently
            # ignore/discard this line
            continue

        if current_patent != patent:
            if current_patent:
                outputPatentInfo(current_patent, values)
            current_patent = None
            values = []

        current_patent = patent
        values.append(value)
        
    # do not forget to output the last word if needed!
    if current_patent:
        outputPatentInfo(current_patent, values)



main()


