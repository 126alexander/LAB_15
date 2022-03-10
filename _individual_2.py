#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

text = ""

if len(sys.argv) <= 1:
    print("Error: No file arguments found.")
    exit()

for filename in sys.argv:
    if sys.argv[0] == filename:
        continue

    try:
        with open(filename, "r" , encoding="utf-8") as a:
            buf = a.read()
            text = text + buf + " "
    except:
        pass

print(text)
