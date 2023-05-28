import hashlib

def MD5_HexDigest(Feed):
    return hashlib.md5(Feed.encode()).hexdigest()

