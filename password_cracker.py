# IMPORT LIBRARIES
import hashlib
import itertools
import string
import time


# STARTER CODE FOR SHA-1 WITH SALTS
# WORKS
def convert_text_to_sha1(text):
    digest = hashlib.sha1(
        text.encode()
    ).hexdigest()
#    print("digest: ", digest)
    return digest


def crack_sha1_hash(hash,use_salts=False):
    start_time = time.time()
    user_sha1 = hash
    cleaned_user_sha1 = user_sha1.strip().lower()
    print(cleaned_user_sha1)

    
    with open('./top-10000-passwords.txt') as f:
        for line in f:
            password = line.strip()

            if use_salts == True:
                with open('./known-salts.txt') as salty:
                    for line in salty:
                        testsalt = line.strip()
                        password = password + testsalt

            converted_sha1 = convert_text_to_sha1(password)
            if cleaned_user_sha1 == converted_sha1:
                print(f"Password Found: {password}")
                print(round(time.time() - start_time, 2), 'secs')
                return password

    return "PASSWORD NOT IN DATABASE"
    


"""
# STARTER CODE FOR SHA-1 WITHOUT SALTS
# WORKS
def convert_text_to_sha1(text):
    digest = hashlib.sha1(
        text.encode()
    ).hexdigest()
    print("digest: ", digest)
    return digest


def crack_sha1_hash(hash):
    start_time = time.time()
    user_sha1 = hash
    cleaned_user_sha1 = user_sha1.strip().lower()
    print(cleaned_user_sha1)

    
    with open('./top-10000-passwords.txt') as f:
        for line in f:
            password = line.strip()
            converted_sha1 = convert_text_to_sha1(password)
            if cleaned_user_sha1 == converted_sha1:
                print(f"Password Found: {password}")
                print(round(time.time() - start_time, 2), 'secs')
                return

    print("Could Not Find the Password")
    
"""





"""
    with open('top-10000-passwords.txt', 'r') as passwords:
        data = passwords.read().splitlines()
        converted_sha1 = convert_text_to_sha1(data)
"""




# TEST FOR UNHASHED COMMON PASSWORDS
"""
def guess_common_passwords(hash):
    
    with open('top-10000-passwords.txt', 'r') as passwords:
        data = passwords.read().splitlines()

    for i, match in enumerate(data):
        if match == hash:
            return f'The password is {match} (Attempt #{i})'

    return 0
    # hash = 'apple123'

def brute_force(hash, min_length=4, max_length=10):
    chars = string.ascii_lowercase + string.digits 
# + string.punctuation
    attempts = 0
    for password_length in range(min_length, max_length):
        for guess in itertools.product(chars, repeat=password_length):
            attempts +=1
            guess = "".join(guess)
            if guess == hash:
               return f'The password is {guess} (Attempt #{attempts})'
            print(guess, attempts)



def get_password(hash):
    common = guess_common_passwords(hash)
    return brute_force(hash) if common  == 0 else common

hash = 'appl4'
"""

hash1 = "fbbe7e952d1050bfb09dfdb71d4c2ff2b3d845d2"
'A36E1F2D2C1309E9F4CD2D6D2EF75D01DD4FD21C'
#'A36E1F2D2C1309E9F4CD2D6D2EF75D01DD4FD21C'
#'B1B3773A05C0ED0176787A4F1574FF0075F7521E'
#'7C4A8D09CA3762AF61E59520943DC26494F8941B'



# print(get_password(hash))

#print(crack_sha1_hash(hash1))




#print(guess_common_passwords(hash))
#print(brute_force(hash))



