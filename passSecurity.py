import ssl
import urllib3
import hashlib

print("This tool allows you to check if your password was leaked")

sha_1 = hashlib.sha1()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager(cert_reqs=ssl.CERT_NONE)

def checkLeak(password):
    sha_1.update(password.encode("utf-8"))
    password_hash = sha_1.hexdigest().upper()
    parthash = password_hash[:5]  # part of the password hash to pass the website
    response = http.request('GET', "https://api.pwnedpasswords.com/range/" + parthash)
    hashstring = response.data.decode('utf-8')
    hashes = hashstring.splitlines()
    leaked = False
    ntimes = 0
    for hash in hashes:
        fullhash = parthash + hash
        temphash = fullhash.split(":")
        fullhash = temphash[0]
        if fullhash == password_hash:
            ntimes = temphash[1]
            leaked = True
    return leaked, ntimes

while True:
    print("Write your password", end = ':')
    password = input()
    leaked, ntimes = checkLeak(password)
    if leaked:
        print("Your password was leaked {} times. Better change it!".format(ntimes))
    print("Want to check another password? (y/n)", end = ':')
    check = input()
    if check.lower() != 'y':
        print("Bye!")
        exit(0)