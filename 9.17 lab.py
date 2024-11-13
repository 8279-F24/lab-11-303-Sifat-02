contact= input().split()
search= input()

contacts={}

for entry in contact:
    name,number=entry.split(',')
    contacts[name]=number

print(contacts[search])