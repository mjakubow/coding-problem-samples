#
# Problem: Given a list of strings on the command line, print all unique values in the list.
#
# Difficulty: 1
#
# Follow-up questions:
#   - What is the complexity of your solution (in O-notation)?
#   - What are some methods you can use to make this as efficient as possible?
#   - What are some space-time trade-offs for performance?
#   - What if the list contains only integers in a known short range?
#

import sys

if len(sys.argv) < 2:
  print(f'Usage: {sys.argv[0]} [item list]')
  sys.exit(0)

unique_args = {}

for arg in sys.argv[1:]:
  if arg not in unique_args:
    unique_args[arg] = 1

print (*unique_args.keys(), sep=',')

for arg in unique_args.keys():
  print(arg, end=" ")
