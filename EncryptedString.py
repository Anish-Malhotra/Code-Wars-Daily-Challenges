#For building the encrypted string:
#Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
#Do this n times!

#Examples:

#"This is a test!", 1 -> "hsi  etTi sats!"
#"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
#"This is a test", 1 ->"hsi  et"

#Assume n>0, strings are not empty

def encrypt(text, n):
	newText = text
	while n>0:
		encrypted_text = newText[1::2]
		encrypted_text = encrypted_text+newText[0::2]
		newText = encrypted_text
		n = n - 1
	return encrypted_text

def decrypt(encrypted_text, n):
	newText = encrypted_text;
	while n > 0:
		i = 0
		decrypted_text = ""
		while i < (len(newText)/2):
			decrypted_text += newText[(len(newText)/2)+i]
			decrypted_text += newText[i]
			i += 1
		if(len(newText)%2 == 1):
			decrypted_text += newText[-1]
		newText = decrypted_text
		n = n - 1
	return decrypted_text

print encrypt("This is a test", 1)
print encrypt("This is a test!", 2)
print decrypt("hsi  etTi sats!",1)
print decrypt("s eT ashi tist!", 2)
print encrypt("This kata is very interesting!", 1)
print decrypt("hskt svr neetn!Ti aai eyitrsig", 1)