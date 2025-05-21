#!/usr/bin/env python3

# Author: Ivan Concon
# Author ID: 137013231
# Date Created: 2025/05/20

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
