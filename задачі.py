from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.config import Config
from time import sleep
from kivy.graphics import Color


Config.set('graphics', 'resizable',  '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '500')


class calculator(App):

	def qest1(self, qes):

		try:
			self.wisible.remove_widget(self.answer)
		except:
			pass

		self.answer = BoxLayout(orientation = 'horizontal', padding = 3)
		put_cord = AnchorLayout(anchor_x='left', anchor_y='top')
		put = BoxLayout(orientation = 'vertical', padding = 3, size_hint = [1, .28])

		self.a = TextInput(hint_text = 'ведіть перше число проміжку')
		put.add_widget(self.a)
		self.b = TextInput(hint_text = 'ведіть бруге число проміжку')
		put.add_widget(self.b)
		self.label = Label(text = 'відповідь')
		put.add_widget(self.label)

		put.add_widget(Label(text = '\n\n\n\n\n\nпрограпа рахує кількість простих чисел\n'\
									'на заданому проміжку які є поліндромами\n'\
									'(читаються одинаково і в право і вліво)'))

		put_cord.add_widget(put)
		self.answer.add_widget(put_cord)
		
		def clcul(bat):
			try:
				aa = int(self.a.text)
				bb = int(self.b.text)
			except:
				self.a.text = ''
				self.b.text = ''
			else:
				if aa <= 2 and bb >= 2:
					k = [2]
				else:
					k = []
				for i in range(aa, bb+1):
					for j in range(2, int(i/2)+2):
						if i % j == 0:
							break
						else:
							if j == int(i/2)+1:

								i=str(i)
								if i == i[::-1] :
									k.append(i)
				self.label.text = str(len(k))


		button_cord = AnchorLayout(anchor_x='center', anchor_y='top')
		button_cord.add_widget(Button(text = 'обчислити',
									  size_hint = [1, .21],
									  on_press = clcul))
		
		self.answer.add_widget(button_cord)
		self.wisible.add_widget(self.answer)


	def qest2(self, qes):
		try:
			self.wisible.remove_widget(self.answer)
		except:
			pass

		def calc(bat):
			try:
				a = int(self.a.text)
			except:
				self.a.text = ''
				self.b.text = ''

			else:
				def remove_str(string, char):
					a = []
					for i in string:
						a.append(i)
					a.remove(char)
					string_answer = ''
					for i in a :
						string_answer += i
					return string_answer

				a = str(a)  #флгоритм переберючий усі елементи в будь-якуй комбінації
				kk = 0
				lack = False
				for t in range(1,len(a)+1):
					for i in a:
						k = kk + int(i)
						k_else = 0
						for j in remove_str(a,i):
							k_else += int(j)
						if k == k_else:
							lack = True
					kk += k
					a = remove_str(a,i)
				if lack == True:
					self.b.text = 'число щасливе'
				else:
					self.b.text = 'число нещасливе'
		
		self.answer = BoxLayout(orientation = 'vertical', padding = 3)
		put_cord = AnchorLayout(anchor_x='left', anchor_y='top', size_hint = [1, .09])

		put = BoxLayout(orientation = 'horizontal', padding = 3)
		self.a = TextInput(hint_text = 'ведіть число')
		put.add_widget(self.a)

		put.add_widget(Button(text = 'обчислити',
							  on_press = calc))

		put_cord.add_widget(put)
		self.answer.add_widget(put_cord)

		autput_cord = AnchorLayout(anchor_x='left', anchor_y='top', size_hint = [.5, .09])
		self.b = Label(text = '')
		autput_cord.add_widget(self.b)
		self.answer.add_widget(autput_cord)


		qest_see = AnchorLayout(anchor_x='left', anchor_y='top')
		qest_see.add_widget(Label(text = 'число щасливе якщо сума будь-яких його чисел\n'\
										 'рівна сумі тих що залишились',
										  size_hint = [.56, 1]))
		self.answer.add_widget(qest_see)

		self.wisible.add_widget(self.answer)


	def qest3(self, qes):
		try:
			self.wisible.remove_widget(self.answer)
		except:
			pass

		def calc(bat):

			def prime4k1(nam):
				'''Return True if mam is prime and 4k+1'''
				corect = False
				if (nam - 1) %4 == 0:
					corect = True
				prime = True
				for i in range(2,nam):
					if nam % i == 0:
						prime = False
						break
				if (corect and prime):
					return True
				else:
					return False

			try:
				a = int(self.a.text)
			except:
				self.a.text = ''
			else:
				if prime4k1(a) == False:
					self.a.text = ''
					self.b.text = '{0}  - не просте число виду: 4k + 1'.format(a)
				else:
					#основна частина з виконаннням, без провірки даних
					for i in range(1,a):
						for j in range(1,a):
							if i**2 + j**2 == a:
								self.b.text = '{0} = {1}² + {2}²'.format(a, i, j)
								self.a.text = ''



		self.answer = BoxLayout(orientation = 'vertical', padding = 3)
		put_cord = AnchorLayout(anchor_x='left', anchor_y='top', size_hint = [1, .09])

		put = BoxLayout(orientation = 'horizontal', padding = 3)
		self.a = TextInput(hint_text = 'ведіть число')
		put.add_widget(self.a)

		put.add_widget(Button(text = 'обчислити',
							  on_press = calc))

		put_cord.add_widget(put)
		self.answer.add_widget(put_cord)

		autput_cord = AnchorLayout(anchor_x='left', anchor_y='top', size_hint = [.5, .09])
		self.b = Label(text = '')
		autput_cord.add_widget(self.b)
		self.answer.add_widget(autput_cord)


		qest_see = AnchorLayout(anchor_x='left', anchor_y='top')
		qest_see.add_widget(Label(text = 'просте число виду 4k+1 завжди мож\n'\
										 'подати у вигляді суми двох квадратів',
										  size_hint = [.46, 1]))
		self.answer.add_widget(qest_see)

		self.wisible.add_widget(self.answer)
		#²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²


	def qest4(self, qes):
		try:
			self.wisible.remove_widget(self.answer)
		except:
			pass

		def sqer_bild(bat):
			try:
				nam = int(self.naminput.text)
			except:
				self.naminput.text = ''
			else:
				

				a = [[0] * (nam) for i in range(nam)]
				tab = 1
				stop = 0
				tras = 'right'
				i = 0
				j = 0
				cheker = True

				while cheker:

					if (nam % 2 == 1 and i + 1 == int(nam / 2) and j + 1 == (nam / 2)):
						a[i][j] = tab
						cheker = False
						print('end')

					if stop >= int(nam / 2) + 1:
						cheker = False

					if tras == 'right':
						if i < nam - stop:
							a[i][j] = tab
							a[nam-1-i][nam-1-j] = tab
							tab += 1
							i += 1
						else:
							i -= 1
							j +=1
							tras = 'duwn'
							stop += 1

					if tras == 'duwn':
						if j < nam - stop:
							a[i][j] = tab
							a[nam-1-i][nam-1-j] = tab
							tab += 1
							j += 1
						else:
							j -= 1
							i -= 1
							tras = 'left'

					if tras == 'left':
						if i > stop - 1:
							a[i][j] = tab
							a[nam-1-i][nam-1-j] = tab
							tab += 1
							i -= 1
						else:
							i += 1
							j -= 1
							tras = 'top'
							stop += 1

					if tras == 'top':
						if j > stop - 1:
							a[i][j] = tab
							a[nam-1-i][nam-1-j] = tab
							tab += 1
							j -= 1
						else:
							j += 1
							i += 1
							tras = 'right'


			try:
				self.autput_cord.remove_widget(self.sqer)
			except:
				pass
			if nam < 21:
				self.sqer = GridLayout(cols = nam, size_hint = [nam /20, nam /20])
			else:
				self.sqer = GridLayout(cols = nam)
			self.autput_cord.add_widget(self.sqer)
			for change1 in range(0, nam):
				for change2 in range(0, nam):
					self.sqer.add_widget(Label(text = '{}'.format(a[change2][change1])))

		self.answer =  BoxLayout(orientation = 'vertical', padding = 3)

		put = BoxLayout(orientation = 'horizontal', padding = 3, size_hint= [1,.08])
		self.naminput = TextInput(hint_text = 'ведіть розмір квадрата')
		put.add_widget(self.naminput)
		put.add_widget(Button(text = 'обчислити', on_press = sqer_bild))


		sqer_cord = GridLayout(size_hint = [.8, .8])
		self.autput_cord = AnchorLayout(anchor_x = 'center', anchor_y = 'center')

		self.answer.add_widget(put)
		self.answer.add_widget(self.autput_cord)


		self.wisible.add_widget(self.answer)


	def build(self):
		self.wisible = BoxLayout(orientation = 'horizontal', padding = 3)
		qests = BoxLayout(
							orientation = 'vertical',
							padding = 3,
							size_hint = [.25, 1]
						  )

		qests.add_widget(Button(text='дзеркально прості\nчисла на проміжку',
								on_press = self.qest1))

		qests.add_widget(Button(text='щасливі\nчисла',
								on_press = self.qest2))

		qests.add_widget(Button(text='розклад на суму\nквадратів чисел',
								on_press = self.qest3))

		qests.add_widget(Button(text='спіраль\nчисел',
								on_press = self.qest4))

		qests.add_widget(Button(text='задача 5'))

		self.wisible.add_widget(qests)

		return self.wisible

calculator().run()
