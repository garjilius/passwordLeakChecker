import urllib3
import hashlib


print("This tool allows you to check if your password was leaked\nWrite your password", end = ':')
password = input()

sha_1 = hashlib.sha1()
sha_1.update(password.encode("utf-8"))
password_hash = sha_1.hexdigest().upper()
parthash = password_hash[:5] #part of the password hash to pass the website

http = urllib3.PoolManager()
response = http.request('GET', "https://api.pwnedpasswords.com/range/"+parthash)
hashstring = response.data.decode('utf-8')
hashes = hashstring.splitlines()
#print("Got a list of {} hashes".format(len(hashes)))

for hash in hashes:
    fullhash = parthash + hash
    temphash = fullhash.split(":")
    fullhash = temphash[0]
    if fullhash == password_hash:
        ntimes = temphash[1]
        print("Your password was leaked {} times,you better change it!".format(ntimes))
        exit(0)

print("Congrats! Your password was not leaked") #Lo raggiunge solo se la password non è stata trovata nel for