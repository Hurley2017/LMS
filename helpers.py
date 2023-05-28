import hashlib
import secrets
import random
import string


def MD5_HexDigest(Feed):
    return hashlib.md5(Feed.encode()).hexdigest()

def sessionGenerator(num):
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
                  for i in range(num))
