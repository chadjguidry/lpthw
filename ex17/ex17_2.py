from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying {from_file} to {to_file}")

# we could do these two on one line, how?
# in_file = open(from_file)
# indata = open(from_file).read()

open(to_file, 'w').write(open(from_file).read())
# out_file.write(indata)

print("Alright, all done.")

#out_file.close()
# in_file.close()
