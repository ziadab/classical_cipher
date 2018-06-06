import os

while True:
	try:
		os.system('pip3 install pycipher')
		os.system('pip install pycipher')
		break
	except Exception as e:
		print("Something go wrong sorry,I will Try again")