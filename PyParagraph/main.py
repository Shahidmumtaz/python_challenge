# Import text file
import os
import re

PyParagraph = ["paragraph_1.txt", "paragraph_2.txt"]

# Save output file path
for PyParagraph in PyParagraph:

	outputpath = os.path.join("Resources", PyParagraph)
	with open(outputpath, "r") as text:

		lines = text.read()
		sentences = re.split(r"(?<!w\w.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", lines)
		words = re.split(r"", lines)
		lettercount = 0
	for word in words:
		lettercount = lettercount + len(word)

	

	lines = []

	outputcsv = open(outputpath, "w")
	lines.append("Paragraph Analysis")
	lines.append("---------------------")
	lines.append("Approximate_word_count:" +str(len(words)))
	lines.append("Approximate_sentence_count:" +str(len(sentences)))
	lines.append("Avg_letter_count:" +str(round(lettercount/len(words), 2)))
	lines.append("Avg_sentence_length:" +str(round(len(words)/len(sentences), 2)))

	for line in lines:
		print(line)


