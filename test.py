print(123)
if 3 > 2:
	print ('it works!')
if 5 > 2:
	print ('5is indeed greater than 2')
else:
	print ('5 is not greater then 2')
name = ' Sonja'
if name == 'Ola':
	print('Hey Ola')
elif name == 'Sonja':
	print('Hey Sonja!')
else:
	print('Hey anonymous!')
volume = 57
if volume < 20:
	print("it's kinda quiet.")
elif 20 <= volume < 40:
	print("it's nice for background music")
elif 40 <= volume < 60:
	print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
	print("Nice for parties")
elif 80 <= volume < 100:
	print("A bit loud!")
else:
	print("My ears are hurting! :(")
def hi():
	print('Hi there!')
	print('How are you?')
hi()


def hi(name):
	if name == 'Ola!':
		print('Hi Ola')
	elif name == 'Sonja':
		print('Hi Sonja!')
	else:
		print('Hi anonymous!')
hi('Sonja')
def hi(name):
	print('Hi ' + name + '!')
hi("Rachel")
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola']
for name in girls:
	hi(name)
	print('Next girl')
for i in range(1,6
	):
	print(i)



