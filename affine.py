from pycipher import Affine
print("""
  ___   __  __ _            
 / _ \ / _|/ _(_)           
/ /_\ \ |_| |_ _ _ __   ___ 
|  _  |  _|  _| | '_ \ / _ \
| | | | | | | | | | | |  __/
\_| |_/_| |_| |_|_| |_|\___|
                                            
                    \033[91m~by Ziad Abouelfarah~

\033[94mThe Algorithm:
\033[97mThe 'key' for the Affine cipher consists of 2 numbers, we'll call them a and b.
The following discussion assumes the use of a 26 character alphabet (m = 26).
a should be chosen to be relatively prime to m (i.e. a should have no factors in common with m).
For example 15 and 26 have no factors in common, so 15 is an acceptable value for a, however 12 and 26 have factors in common (e.g. 2) so 12 cannot be used for a value of a.
When encrypting, we first convert all the letters to numbers ('a'=0, 'b'=1, ..., 'z'=25).
The ciphertext letter c, for any given letter p is (remember p is the number representing a letter):         

c = ap + b(mod m), 1 <= a <=m ,  1 <= b <=m

The decryption function is: 

p =  (a**−1)(c-b) (mod m)

where a**−1 is the multiplicative inverse of a in the group of integers modulo m.
To find a multiplicative inverse, we need to find a number x such that:                           

ax = 1(mod m)

If we find the number x such that the equation is true, then x is the inverse of a, and we call it a−1. 
The easiest way to solve this equation is to search each of the numbers 1 to 25, and see which one satisfies the equation.
If you want a more rigorous solution, you can use matlab to find x: 

> [g,x,d] = gcd(a,m);    % we can ignore g and d, we dont need them
> x = mod(x,m);    \033[0m                  

The Script :

1-encrypt  \n2-decrtpt	""")
choise = input('Choise: ')
if  choise == 1 or choise == '1':
	plaintext = str(input("\033[97mYour Secret Text :\033[91m "))
	words = plaintext.split(" ")
	key1 = int(input("\033[97mchoise the first key ! like:[0,1,2,3,4,..] default=1 ! :\033[91m "))
	key2 = int(input("\033[97mchoise the first key ! like:[0,1,2,3,4,..] default=1 ! :\033[91m "))
	i = 0
	for i in range(len(words)):
		cipher = Affine(a=key1,b=key2).encipher(words[i])
		cipher = cipher.lower()
		print(cipher, sep=' ',end=" ")
else:
	cipher = str(input("\033[97mYour Text : "))
	words = cipher.split(" ")
	key1 = int(input("\033[97mThe first key that you encrypt with :\033[91m "))
	key2 = int(input("\033[97mThe second key that you encrypt with :\033[91m "))
	i = 0
	for i in range(len(words)):
		plaintext = Affine(a=key1,b=key2).decipher(words[i])
		plaintext = plaintext.lower()
		print(plaintext, sep=' ', end=" ")

print("\033[0m ")