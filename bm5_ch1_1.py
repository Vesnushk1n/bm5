class StringVar:

    def __init__(self, text):
        self.data = text
    def set(self):
        new_data = input('Введите новый текст: ')
        self.data = new_data
        return new_data

    def get(self):
        data = self.data
        return data

data = StringVar("Привет, меня зовут Дима!")
while True:
    info = input('Вы желаете получить информацию или её отредактировать?')
    if info.lower() == 'получить':
        print(f'Текущее значение: {data.get()}')
    elif info.lower() == 'отредактировать':
        print(f'Установлено: {data.set()}')