# very tricky. According to ASCII, dist('A','c') == dist('B','d')
# for frequently uesd words, Hi is adjacent in English word(if we ignore upper/lower case), ths same as Yz
# So I guess the first two char might be Hi, so use ord('Y') - ord('H') as encrypt distance
def decrypt(string):
    ans = ''
    for char in string:
        ans += chr(ord(char) - 17)
    return ans

if __name__ == '__main__':
    a = decrypt('Yz=1TZedBEAB1dB1CACA')
    print(a)