#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

debug=False

def outputPatentInfo(key, values,citations):

    #
    # Our inputs are either 3070801	1963,1096,,"BE","",,1,,269,6,69,,1,,0,,,,,,,
    # or 6009554	y
    #
    #
    # So the "values" either have zero commas or multiple commas
    #
    cites = [ pat for pat in values if pat.count(',') == 0 ]
    info = [ pat for pat in values if  pat.count(',') > 2 ]

##    if debug:
##        print("values is ", values)
##        print("cites is ", cites)
##        print("info is ", info)
    if key != None and values != None:
        cites = [ pat for pat in values if pat.count(',') == 0 ]
        info = [ pat for pat in values if  pat.count(',') > 2 ]
        try:
            if len(info) == 0:  
                print("%s\tbad missing patent info " % (key))
            else:
                try:
                    
                        cites_official = int( info[0].split(',')[5] )
                        cite_number = int( info[0].split(',')[11] )
                except ValueError as e:
                    cites_official = 0
                if citations != None:
                    if len(citations) == cite_number:
                        for i in citations:
                            print("%s\t%s\t%s" % (key,i,cites_official))
            #if len(cites) == cites_official:
             #   print("%s\tok" % (key))
#
# It would be nice to use the counters in this example but it
# causes the Java process to run out of heap space
#
#                sys.stderr.write("reporter:counter:PatentReducer,REDUCE_GOOD,1")
                else:
                    print("%s\tbad cites got %s expected %d " % (key, len(cites), cites_official))
#                sys.stderr.write("reporter:counter:PatentReducer,REDUCE_BAD,1")
        except ValueError as e:
            #
            # Something wrong in number format
            #
            pass
##    except Exception as e:
##        print("Something died", e)

    

def main():
    current_patent = None
    values = []
    citations = []

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

        if len(value) > 1:
            values = value.split(',')
            current_patent = patent
        else:
            current_patent = patent
            citations = citations.append(value)
        

        if current_patent:
            outputPatentInfo(current_patent,values,citations)
        else:
            current_patent = patent
            values = value.split(',')
            outputPatentInfo(current_patent,values,citations)


        
    # do not forget to output the last word if needed!
    if current_patent:
        outputPatentInfo(current_patent, values,citations)



main()
