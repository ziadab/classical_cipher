from pycipher import Atbash
print("""

          _   _               _     
     /\  | | | |             | |    
    /  \ | |_| |__   __ _ ___| |__  
   / /\ \| __| '_ \ / _` / __| '_ \ 
  / ____ \ |_| |_) | (_| \__ \ | | |
 /_/    \_\__|_.__/ \__,_|___/_| |_|
                    
                    ~by Ziad Abouelfarah~
                                    
1-encrypt  \n2-decrtpt	""")
choise = input('Choise: ')
if  choise == 1 or choise == '1':
	plaintext = str(input("Your Secret Text : "))
	words = plaintext.split(" ")
	i = 0
	for i in range(len(words)):
		cipher = Atbash().encipher(words[i])
		cipher = cipher.lower()
		print(cipher, sep=' ',end=" ")
else:
	cipher = str(input("Your Text : "))
	words = cipher.split(" ")
	i = 0
	for i in range(len(words)):
		plaintext = Atbash().decipher(words[i])
		plaintext = plaintext.lower()
		print(plaintext, sep=' ', end=" ")

print(" ")