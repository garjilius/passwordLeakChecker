# passwordLeakChecker
Uses the pwnedpassword.com api to check if a password has ever been leaked

Note that your password is not sent to the server, and neither is a full hash.
In fact, only the fist 5 characters of the SHA-1 hash of your password will be sent.
The server will then return a list of hashes that begin with those 5 characters.
If there are matches, a full match will be checked locally. 
