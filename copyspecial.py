
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# Copyright 2010 Google Inc.

'''
IMPORT REQUIRED MODULES
'''

'''
Write functions and modify main() to call them
+++your code here+++
'''

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir] dir [dir ...]")
    sys.exit(1)

  # todir is either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  ''' +++your code here+++
   Call your functions'''
  
if __name__ == "__main__":
  main()
