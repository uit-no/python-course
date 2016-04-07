#!/usr/bin/env python3

import os

tot_bytes = 0
lst = os.listdir()

for f in lst:
    stat = os.stat(f)
    tot_bytes += stat.st_size

result = "The directory contains {0} files for a total of {1} bytes".format(len(lst), tot_bytes)

print(result)





