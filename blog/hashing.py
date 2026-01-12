from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

class Hash():
    def bcrypt_password(password: str):
        hashed_password = password_hash.hash(password)
        return hashed_password 
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
