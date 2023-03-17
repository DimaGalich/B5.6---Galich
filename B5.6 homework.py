# ПОЛЕ
#Функция отвечающая за отображение игрового поля.
def show_field(f):
    num ='  0 1 2' #Задать значение переменной Num которая будет выводиться перед каждым ходом.
    print(num)
    for row,i in zip(f,num.split()):
        print (f"{i} {' '.join(str(j) for j in row)}")  #Настройка внешнего вида поля ниже строки num.
# _______________________________________________________________________

# ОПРОС ИГРОКА
# Функция отвечающая за ввод данных игроком, и проверка на корректность введенных данных
def users_input(f,user):
    while True:
        # Запрос ввода данных
        place=input(f"Ходит {user} .Введите координаты по горизонтали и вертикали:").split()
        if len(place)!=2: #Если введённое количество символов не равно двум, то вывести 'Введите две координаты'
            print('Введите две координаты')
            continue
        #Проверка наличия цифр в ведённых данных игроком с помощью .isdigit, если не цифры, то вывести 'Введите числа'
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        #Проверка на колличество символов с помощью 0<=x<3 0<=y<3
        x, y = map(int, place)
        if not(x>=0 and x<3 and y>=0 and  y<3):
            print('Вышли из диапазона')
            continue
        #Проверка занята клетка или нет с помощью "неравенства '-'"
        if f[x][y]!='-':
            print('Клетка занята')
            continue
        break
    return x,y
# # ОПРОС ИГРОКА ВАРИАНТ №2
# def users_input(f):
# 	while True:
# 		place=input('Введите координаты : ').split()
# 		if len(place)!=2:
# 			print('Введите две координаты')
# 			continue
# 		if not(place[0].isdigit() and place[1].isdigit()):
# 			print('Введите числа')
# 			continue
# 		# x, y= map(int,place)
# 		# if not(x>=0 and x<3 and y>=0 and y<3:
# 		# 	print('Вышли из диапазона')
# 		# 	continue
# 		if f[x][y]!='-':
# 			print('Клетка занята')
# 			continue
# 		break
# 	return x,y
# # users_input(field)
# ________________________________________________________________

# ВЫЙГРЫШНЫЕ КОМБИНАЦИИ

def win_position(f,user):
    f_list=[]
    # print(f) #Убрал лишнее отображение перед каждым ходом ['-', '-', '-']
    for l in f:
        f_list+=l
    # print(f_list) #Убрал лишнее отображение перед каждым ходом '-', '-', '-',
    positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #Список выигрышных комбинаций
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p)))==3:
            return True
    return False

# # ВЫЙГРЫШНЫЕ КОМБИНАЦИИ ВАРИАНТ №2
# def win_v1(f, user):
# 	def check_line(a1,a2,a3,user):
# 	    if a1==user and a2==user and a3==user:
# 		    return True
# 	for n in range(3):
# 		if check_line(f[n][0], f[n][1], f[n][2], user) or \
# 		check_line(f[0][n], f[1][n], f[2][n], user) or \
# 			(f[0][0], f[1][1], f[2][2], user) or \
# 		(f[2][0], f[1][1], f[0][2], user):
# 			return True
# 	return False
# ___________________________________________________________________________________

# УСЛОВИЯ ПОБЕДЫ, РАУНДЫ, НИЧЬЯ

def start(field):

    count=0 #Счетчик ходов
    while True:
        show_field(field)
        if count%2==0: #Четный или нечетный ход, если четный то ходит "х", если нечетный то ходлит "о"
            user='x'
        else:
            user = 'o'
        if count<9:
            x, y = users_input(field,user)
            field[x][y] = user

        elif count==9: #Если раунд дошел до девятого, то объявляется ничья.
            print ('Ничья')
            break
        if win_position(field,user):
            print(f"Выйграл {user}")
            break
        count+=1 #Каждый ход счетчик ходов увеличивает на один.

# # УСЛОВИЯ ПОБЕДЫ, РАУНДЫ, НИЧЬЯ ВАРИАНТ №2
# count=0
# while True:
# 	if count%2==0:
# 		user='x'
# 	else:
# 		user='0'
# 	# show_field(field)
# 	# x,y=users_input(field)
# 	# field[x][y]=user
# 	if count==9:
# 		print('Ничья')
# 	# if win_v1(field,user):
# 		print(f"Выйграл {user}")
# 		show_field(field)
# 		break
# 	count+=1
#


field = [['-'] * 3 for _ in range(3)]
# field=[['-','-','-'],['-','-','-'],['-','-','-']]

start(field)
