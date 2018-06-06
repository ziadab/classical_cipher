from pycipher import Caesar
print("""
 _____                            
/  __ \                           
| /  \/ __ _  ___  ___  __ _ _ __ 
| |    / _` |/ _ \/ __|/ _` | '__|
| \__/\ (_| |  __/\__ \ (_| | |   
 \____/\__,_|\___||___/\__,_|_|   
                                                  
                    ~by Ziad Abouelfarah~
                                    
1-encrypt  \n2-decrtpt	""")
choise = input('Choise: ')
if  choise == 1 or choise == '1':
	plaintext = str(input("Your Secret Text : "))
	words = plaintext.split(" ")
	key = int(input("choise a key ! like:[0,1,2,3,4,..] default=1 ! : "))
	i = 0
	for i in range(len(words)):
		cipher = Caesar(key=key).encipher(words[i])
		cipher = cipher.lower()
		print(cipher, sep=' ',end=" ")
else:
	cipher = str(input("Your Text : "))
	words = cipher.split(" ")
	key = int(input("key that you encrypt with : "))
	i = 0
	for i in range(len(words)):
		plaintext = Caesar(key=key).decipher(words[i])
		plaintext = plaintext.lower()
		print(plaintext, sep=' ', end=" ")

print(" ")