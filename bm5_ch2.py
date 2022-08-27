import json
class Citatka:
	def __init__(self, title, text, author):
		self.title = title
		self.text = text
		self.author = author
		open(f'Phrase.json', 'w').write(json.dumps(self.__dict__))
while(True):
	title = input('Title: ')
	text = input('Text: ')
	author = input('Author: ')
	Citatka(title, text, author)
	print('Done!')