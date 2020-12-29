########### ИМПОРТ БИБЛИОТЕК ###########
from os import system
from math import tan
########### ИМПОРТ БИБЛИОТЕК ###########



########### КЛАСС ДЛЯ СОБСТВЕННЫХ ИСКЛЮЧЕНИЙ ###########
class MyError(Exception):
	def __init__(self, msg): self.msg = msg
########### КЛАСС ДЛЯ СОБСТВЕННЫХ ИСКЛЮЧЕНИЙ ###########



########### ФУНКЦИИ ###########
clear = lambda: system('cls')

# Функция катангенса
ctg = lambda x: 1 / tan(x)

# Функция исходной функции уравнения
func = lambda x: ctg(x) - x / 2
# func = lambda x: pow(x, 3) - 3 * sin(x)

# Функция приема чисел от пользователя
def user_input(symbol):
	clear()
	while True:
		try:
			var = float(input(f'Введите {symbol}: '))
			if var < 0:
				clear()
				raise MyError(f'{symbol} не может быть отрицательным')			
			break
		except ValueError:
			clear()
			print('Неверно указан тип')
		except MyError as mr:
			print(mr)
	return var

# Функция решения
def decision(e, a, b):
	# Точки интервала
	sp, mp, ep = a, (a + b) / 2, b
	# Значения функций для точек
	sf, mf, ef, x = func(sp), func(mp), func(ep), 0

	while True:
		xp, a1 = x, (mf - sf) / (mp - sp)
		a2 = (1 / (ep - mp)) * ((ef - sf) / (ep - sp) - (mf - sf) / (mp - sp))
		x = 0.5 * (sp + mp - (a1 / a2))
		fx = func(x)
		if (sp < x < mp < ep):
			if fx >= mf: sp, sf = x, func(sp)				
			else: ep, mp, mf, ef = mp, x, func(mp), func(ep)
		elif (sp < mp < x < ep):
			if (fx >= mf): ep, ef = x, func(ep)				
			else: sp, mp, sf, mf = mp, x, func(sp), func(mp)
		if abs(xp - x) <= e: break
	return round(x, 5), round(fx, 5)

# Главная функция
def main():
	clear()
	# Погрешность, и интервал	
	e, a, b = user_input('e'), user_input('a'), user_input('b')	
	# Получаем значения x и y
	x, y = decision(e, a, b)
	print(f'x = {x}\ny = {y}')
########### ФУНКЦИИ ###########

main()