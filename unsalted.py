import hashlib, bcrypt
password_file = open("formspring.txt", "r")
dictionary_file = open("english.txt", "r")

for word in dictionary_file.readlines():
	hashedSha1 = hashlib.sha1(word.encode()).hexdigest()
	hashedsha256 = hashlib.sha256(word.encode()).hexdigest()
	hashedmd5 = hashlib.md5(word.encode()).hexdigest()
	hashedbcrypt = bcrypt.hashpw(word.encode(), bcrypt.gensalt(10))
	cracked = False;
	for encryptedPass in password_file.readlines():
		if hashedSha1 == encryptedPass:
			print("Password found after sha1 encryption " + word)
			cracked = True
		elif hashedmd5 == encryptedPass:
			print("Password found after md5 encryption " + word)
			cracked = True
		elif hashedbcrypt == encryptedPass:
			print("Password found after bcrypt encryption with 10 salts" + word)
			cracked = True
		elif hashedsha256 == encryptedPass:
			print("Password found after bcrypt encryption")
			cracked = True
	if cracked == False:
		print("Couldn't crack password retrying with another word")


