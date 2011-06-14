#!/usr/bin/env python

# Original version by Keith McCammon available from http://mccammon.org/keith/code/
# Parsing argv and checking for existing files by Mario Aeby, eMeidi.com, 2011

import sys
import re
import os.path

if len(sys.argv) < 2:
	sys.exit('Usage: %s <source> [<destination>]' % sys.argv[0])

INFILE = sys.argv[1]

# If a second argument is provided, use this as the destination filename
if len(sys.argv) > 2:
	OUTFILE = sys.argv[2]
else:
	OUTFILE = re.sub('\.ics$','',INFILE) + '.gcal.ics'

if not os.path.isfile(INFILE):
	sys.exit('Error: File "' + INFILE + '" not found')
	
if os.path.isfile(OUTFILE):
	sys.exit('Error: File "' + OUTFILE + '" already exists')

sys.stdout.write('Converting "' + INFILE + '" to "' + OUTFILE + '"' + "\n");

DEBUG = 1   # 0:Silent, 1:Info, 2:Verbose
TAGS = [
        ('BEGIN:VALARM', 'END:VALARM'),
        ('BEGIN:VTODO', 'END:VTODO')
       ]

def dbg(level, s, debug=DEBUG):
    if debug == 0:
        return
    elif level <= debug:
        sys.stdout.write(s)

def main():
    f = open(INFILE, 'r')
    infile = f.readlines()
    f.close()
    dbg(1, "Read %d lines from %s\n" % (len(infile), INFILE))

    outfile = []
    for t in TAGS:
        START = t[0]
        END = t[1]
        dbg(1, "Begin processing tag set: (%s, %s)\n" % (START, END))
        
        # If there's already data in outfile, assume that we need to continue
        # processing that data, with additional tag sets.
        if len(outfile) > 0:
            data = outfile[:]
            outfile = []
        else:
            data = infile

        # Remove lines that either match or are between START and END tags.
        WITHIN = False
        for i in data:    
            if not WITHIN and START not in i and END not in i:
                outfile.append(i)
            elif START in i:
                dbg(2, "Entering stanza: %s\n" % START)
                WITHIN = True
            elif WITHIN:
                if END in i:
                    dbg(2, "Exiting stanza: %s\n" % END)
                    WITHIN = False
                else:
                    dbg(2, "--> within stanza\n")

        dbg(1, "End processing tag set: (%s, %s)\n" % (START, END))

    dbg(1, "Removed %d lines.  Writing..." % (len(infile) - len(outfile)))

    f = open(OUTFILE, 'w')
    for i in outfile:
        f.write(i)
    f.close()
    dbg(1, "done!\n")

if __name__ == '__main__':
    
    main()
