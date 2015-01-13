def _string_hash(source):       
    if source == "":
        return 0
    else:
        x = ord(source[0]) << 7
        print x
        m = 1000003
        mask = 2 ** 64 - 1
        for c in source:
            x = ((x * m) ^ ord(c)) & mask
            print x
        x ^= len(source)
        if x == -1:
            x = -2
        print x
        return

if __name__ == '__main__':
    _string_hash('a')

