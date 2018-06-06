from pycipher import Rot13
print("""
  _____       _  __ ____  
 |  __ \     | |/_ |___ \ 
 | |__) |___ | |_| | __) |
 |  _  // _ \| __| ||__ < 
 | | \ \ (_) | |_| |___) |
 |_|  \_\___/ \__|_|____/ 
                             
                ~by Ziad Abouelfarah~
                                    
1-encrypt  \n2-decrtpt	""")
choise = input('Choise: ')
if  choise == 1 or choise == '1':
	plaintext = str(input("Your Secret Text : "))
	words = plaintext.split(" ")
	i = 0
	for i in range(len(words)):
		cipher = Rot13().encipher(words[i])
		cipher = cipher.lower()
		print(cipher, sep=' ',end=" ")
else:
	cipher = str(input("Your Text : "))
	words = cipher.split(" ")
	i = 0
	for i in range(len(words)):
		plaintext = Rot13().decipher(words[i])
		plaintext = plaintext.lower()
		print(plaintext, sep=' ', end=" ")

print(" ")