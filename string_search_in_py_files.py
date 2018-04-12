import os

matching_files = []
string_containing_files = []


root = raw_input("Enter the path of the root folder : ")

search = raw_input("Enter the element to search : ")

for path, subdirs, files in os.walk(root):
    for name in files:
        if name.endswith(".py"):
            matching_files.append(os.path.join(path, name))

for item in matching_files:
    with open(item, 'r') as current_file:
        if search in current_file.read():
            string_containing_files.append(item)

if len(string_containing_files) == 0:
    raw_input("No files contain the requested string.")

else:
    print "Following files contain the requested string :\n\n\n"
    for item in string_containing_files:
        print item