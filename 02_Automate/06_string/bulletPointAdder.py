#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip

text = pyperclip.paste()  #將複製的文本貼上

lines = text.split('\n') # Separate lines and add stars.

for i in range(len(lines)): 		# loop through all indexes for "lines" list
	lines[i] = '* ' + lines[i] 	# add star to each string in "lines" list
	
text = '\n'.join(lines)

pyperclip.copy(text)

print(text)