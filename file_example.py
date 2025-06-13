import string


def count_occurences(file_name, word):
	count = 0
	lower_word = word.lower()
	stream = open(file_name)
	line = stream.readline()
	while line != '':
		line = line.translate(str.maketrans('', '', string.punctuation))
		line_list = line.split()
		for line_word in line_list:
			if line_word.lower() == lower_word:
				count += 1
		line = stream.readline()
	return count


print(count_occurences('first_text_file.txt', 'bit'))
