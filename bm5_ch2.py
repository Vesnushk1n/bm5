import json
class Save:
	def save(self, title, text, author):
		result = json.dumps({'title': title, 'text': text, 'author': author})
		path = f'{author}.json'
		open(path, 'w').write(result)
		return f"Сохранено в {path}"
while(True):
	cit = Save()
	title = input('Title: ')
	text = input('Text: ')
	author = input('Author: ')
	print(cit.save(title, text, author))