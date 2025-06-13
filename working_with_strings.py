sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''
sample_story2 = "Once I'm awaken, I'll sacrifice your soul to the ruler of darkness."
def get_longest_word(story):
	if len(story) == 0:
		return ''
	story = story.replace(',', '').replace('.', '').replace('\n', ' ').replace('\r', ' ')
	story_list = story.split()
	longest_word = story_list[0]
	for item in story_list:
		if len(item) > len(longest_word):
			longest_word = item
	return longest_word

print(get_longest_word(sample_story2))


