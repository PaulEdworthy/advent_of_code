import hashlib

secret = 'iwrupvqb'
salt = 6


def solve(key, zeros):
    n = 1
    prefix = zeros * '0'

    while True:
        s = key + str(n)
        h = hashlib.md5(s.encode()).hexdigest()[:zeros]
        if h == prefix:
            return n
        n += 1


print(solve(secret, salt))
