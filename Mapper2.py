"#!/usr/bin/env python"
"""mapper.py"""

import sys

debug = False
for line in sys.stdin:
    line = line.rstrip('\n')
    # split the line into CSV fields
    try:
        words = line.split(",")
    except:
        #

        # Can't split, so invalid line
        #
        continue
    try:
        if len(words) == 3:
        
            print('%s\t%s\t%s' % (words[1],words[2],words[0]))
        else:
        
            print('%s\t%s\t%s' % (words[1],words[2],""))

    except:
        print("No output")
    

    else:
        try:
            print('%s\t%s' % (words[0], ','.join(words[1:])))
        except Exception as e:
            
                # improperly formed citation number
            print("Exception ", e);
            pass
