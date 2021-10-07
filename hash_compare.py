import hashlib

def main():
    password = input('Type your password: ')
    hashed_password = convert_to_hash(password)
    print('The md5 hash of your password is:', hashed_password)
    hash_to_compare = input('Type a hash to compare: ')
    result = hash_compare(hashed_password, hash_to_compare)

    if result: print('Passwords match.')
    else: print('The passwords do not match.')
        
def convert_to_hash(password):
    password = hashlib.md5(password.encode('utf8')).hexdigest()
    return password
        
def hash_compare(hashed_password, hash_to_compare):
    if hashed_password == hash_to_compare: return True
    else: return False

if __name__ == '__main__':
    main()
