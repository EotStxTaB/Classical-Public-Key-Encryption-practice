import  math

def Encrypt(msg, key):#加密
    size = len(msg)
    result = []
    for i in range(key):
        t = i
        while t < size:
            result.append(msg[t])
            t += key
    return ''.join(result)

def Decrypt(msg, key):#解密
    numOfColums = int(math.ceil(len(msg)/float(key)))
    numOfRows = key
    sharedBox = numOfColums * numOfRows - len(msg)
    row = 0
    col = 0
    result = [''] * numOfColums
    for i in msg:
        result[col] += i
        col += 1
        if col == numOfColums or (col == numOfColums - 1 and row >= numOfRows - sharedBox):
            col = 0
            row += 1
    return ''.join(result)

        


if  __name__=="__main__":
    plaintext = input("请输入明文：")
    key = int(input("请输入密钥："))
    cipher = Encrypt(plaintext, key)
    print("密文：" + cipher) 
    print("明文：" + Decrypt(cipher, key))