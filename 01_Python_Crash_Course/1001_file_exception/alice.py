title = 'Alice in Wonderland'
titles = title.split()
print(titles)
print(len(titles))

filename = '01_Python_Crash_Course\\1001_file_exception\\Alice in Wonderland.txt'
try:
    with open(filename) as fileobject:
        contents = fileobject.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)

    print("This file has " + str(num_words) + ' words.')