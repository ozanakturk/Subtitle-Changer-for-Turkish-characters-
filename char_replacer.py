"""
This program is for replacing the unwanted characters with the wanted characters in a file.
mrep function is taken from the stackoverflow user "mcsoini"
"""
# The mapping that linkes the unwanted characters to the wanted characters
replacer = {"þ" : "ş",
            "ý" : "ı",
            "ð" : "ğ",
            "Ý" : "İ",
            "Þ" : "Ş"}

# Asks the file name and reads the lines of that file
location = input("Please write the name (with its extension) of the file: ")
print("Your file is getting ready...")
readfile = open(location, "r")
lines = readfile.readlines()

# The below function does the replacing. 
# The first argument is a string and the second one is a dictionary in dict(dict_name).
mrep = lambda s, d: s if not d else mrep(s.replace(*d.popitem()), d)

# Edits the lines
for item in lines:
    lines[lines.index(item)] = mrep(item, dict(replacer))

# Writes the edited lines to a new file and informs the user
writefile = open("NEW_" + location, "w+", encoding="UTF-8")
for item in lines:
    writefile.write(item)

print("Your file is ready!")

# Closes the files
readfile.close()
writefile.close()