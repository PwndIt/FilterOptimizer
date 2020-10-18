# Rough and Dirty Python Script to Convert a list of words to UPPER, lower, and Title Case in the worst way possible.
directory = input("File to Process Directory: ")
file = open(directory)
line = file.read().replace("\n", " ")
file.close()
capital = line.upper()
Lowercase = line.lower()
title = line.title()
together = capital + " " + Lowercase + " " + title
exportFile = input("Name of File to export to: ")
f = open(exportFile, "w")
f.write(together)
f.close()
