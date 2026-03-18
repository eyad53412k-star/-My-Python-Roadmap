def password(secret):
	if secret == "123":
		return ("Login successful")
	
	else:
		return ("login failed")

result = password(input("Enter password"))

print(result)
