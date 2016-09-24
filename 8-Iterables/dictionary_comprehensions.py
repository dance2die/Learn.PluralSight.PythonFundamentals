import os
import glob

from pprint import pprint as pp

map = {'a': 1, 'b': 2, 'c': 3}
pp(map)

reverse_map = {val: key for key, val in map.items()}
pp(reverse_map)


file_sizes = {os.path.realpath(p): os.stat(p).st_size
              for p in glob.glob('*.py')}
pp(file_sizes)





