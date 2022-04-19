import hashlib

def dhash(msg : str) -> str:
    h1 = hashlib.sha256(str.encode(msg)).hexdigest()
    return hashlib.sha256(str.encode(h1)).hexdigest()
if __name__ == '__main__':
    msg = input()
    print(dhash(msg))