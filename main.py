ASCII = []
passage = [""]
password = ""
safelysent = "y"
LondonPassword = ""
londonpasswordinput = ""


print("Enter sentence to be encrypted:")
passage = input()

for character in passage:
  ASCII.append(ord(character))


password = passage[0:8] 
LondonPassword = password



print("The password for this passage is:", password)
print("The ASCII for this is:", ASCII)

if safelysent != "y":
  print("Error: Not Sent Safely")

if safelysent == "y":
 print("Data was sent Safely")
else: print("Error: Acess Denied")

print()


print("LONDON HQ")
print()
print("Enter Password:")
londonpasswordinput = input()

if londonpasswordinput == LondonPassword:
  print("The message unencrypted is:", passage)
else: print("Access Denied")





