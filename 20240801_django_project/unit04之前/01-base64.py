import base64

str1 = base64.b64encode('AID'.encode())
print(str1)

str2 = base64.b64decode('QUlE')

print(str2)

str3 = base64.b64encode(b'AB?')
print(str3)


str4 = base64.urlsafe_b64encode(b'AB?')
print(str4)
aaa=base64.urlsafe_b64decode(str4)
print(aaa)

