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


    cites = [ pat for pat in values if pat.count(',') == 0 ]
    info = [ pat for pat in values if  pat.count(',') > 2 ]

    if debug:
        print("values is ", values)
        print("cites is ", cites)
        print("info is ", info)

    try:
        if len(info) == 0:
            print("%s\tbad missing patent info " % (key))
        else:
            try:
                cites_official = int( info[0].split(',')[11] )
            except ValueError as e:
                cites_official = 0

            if len(cites) == cites_official:
                for i in info:
                    print(key,i,info[11])
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



