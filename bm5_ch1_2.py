class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plus(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
        self.data = point(x,y)
        return (self.x, self.y)

    def minus(self, x, y):
        self.x = self.x - x
        self.y = self.y - y
        self.data = point(x,y)
        return (self.x, self.y)

    def coords(self):
        return (self.x, self.y)

data = point(0,0)
while True:
    print('На данный момент вы находитесь на точке: ', data.coords()[0],':',data.coords()[1], '. Введите координаты x и y для перемещения: ')
    x = int(input('Введите координату x: '))
    y = int(input('Введите координату y: '))
    info = input('Вы желате прибавить эти координаты к основным или отнять? ')
    if info.lower() == 'прибавить':
        print(f'Вы оказались на точке: {data.plus(x, y)}')
    elif info.lower() == 'отнять':
        print(f'Вы оказались на точке: {data.minus(x, y)}')





