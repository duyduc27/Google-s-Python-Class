import sys
import re

"""
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
"""

def extract_name(filename):
  names = [] #initial list contains year, name, rank
  f = open(filename, 'rU')
  text = f.read()
  year_match = re.search(r'Popularity in (\d\d\d\d)', text)
  if not year_match:
    # can't find year
    sys.stderr.write('Couldn\'t find the year!\n')
    sys.exit(1)
  names.append(year_match.group(1))

  tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
  # return tuple with format (rank, male name, female name)
  name_and_rank = {} # initial dic
  for tuple_rank in tuples:
    (rank, boyname, girlname) = tuple_rank #unpack tuple
    # Since boys and girls have chance to get the same name
    if boyname not in name_and_rank:
      name_and_rank[boyname] = rank
    if girlname not in name_and_rank:
      name_and_rank[girlname] = rank
  # sorted the dictionary by key
  sorted_key = sorted(name_and_rank.keys()) # list of names was sorted
  for name in sorted_key:
    names.append("{} {}".format(name, name_and_rank[name]))

  return names

def main():
  args = sys.argv[1:] # omit the [0] element

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for filename in args:
    names = extract_name(filename)

    text = '\n'.join(names)

    if summary:
      output = open(filename + ".txt", "w")
      output.write(text + '\n')
      output.close()
    else:
      print(text)

if __name__ == "__main__":
  main()

  