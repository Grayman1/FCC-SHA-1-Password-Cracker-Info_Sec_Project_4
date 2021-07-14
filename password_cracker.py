# IMPORT LIBRARIES
import hashlib
import time
import itertools
import string


# STARTER CODE FOR SHA-1 WITH SALTS
# WORKS
def convert_text_to_sha1(text):
  digest = hashlib.sha1(
      text.encode()
  ).hexdigest()
#  print("digest: ", digest)
  return digest


# FINAL WORKNG VERSION

def crack_sha1_hash(hash, use_salts=False):
  start_time = time.time()
  user_sha1 = hash
  cleaned_user_sha1 = user_sha1.strip().lower()
#  print("cleaned user hash: ", cleaned_user_sha1, "Use Salts?:", use_salts)
  
  with open('./top-10000-passwords.txt') as f:
    pass_list = f.readlines()

  with open('./known-salts.txt') as f2:
    salt_list = f2.readlines()

  for line in pass_list:
    password = line.strip()
#    print(password)
  
    if use_salts :      
      for salty in salt_list:
        testsalt = salty.strip()
#        print(password, testsalt)
        salt_test1 = password + testsalt
        salt_test2 = testsalt + password
#        print(salt_test1, salt_test2)         
        salted_hash1 = convert_text_to_sha1(salt_test1)
        salted_hash2 = convert_text_to_sha1(salt_test2)

        if cleaned_user_sha1 == salted_hash1 or cleaned_user_sha1 == salted_hash2:
          print(f"Password Found: {password}")
          print(round(time.time() - start_time, 2), 'secs')
          return password
  #      print("No Match")
  

    else:  
      converted_sha1 = convert_text_to_sha1(password)

      if cleaned_user_sha1 == converted_sha1:
        print(f"Password Found: {password}")
        print(round(time.time() - start_time, 2), 'secs')
        return password

  return "PASSWORD NOT IN DATABASE"