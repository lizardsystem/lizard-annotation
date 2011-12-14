#!/usr/bin/python
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.

import sys

# Should be used after mongoexport
if '--export' in sys.argv:

    print '%s  # Header added by mongo-dumpdata' % sys.argv[2]
    for line in sys.stdin:
        sys.stdout.write(line)
