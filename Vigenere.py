#-*-coding:utf-8-*-

# Vigenere
# by Kisna 21.5.20

# 加密模块
def VigenereEncrypto(input, key):
    ptLen = len(input)
    keyLen = len(key)

    quotient = ptLen // keyLen    
    remainder = ptLen % keyLen    
    out = ""

    for i in range(0, quotient):
        for j in range (0, keyLen):
            c = int((ord(input[i*keyLen + j]) - ord('a') + ord(key[j]) - ord('a'))%26 + ord('a'))
            #global output
            out += chr(c)

    for i in range(0, remainder):
        c =  int((ord(input[quotient*keyLen + i]) - ord('a') + ord(key[i]) - ord('a'))%26 + ord('a'))
        #global output
        out += chr(c)

    return out


# 解密模块
def VigenereDecrypto(output, key):
    ptLen = len(output)
    keyLen = len(key)

    quotient = ptLen // keyLen
    remainder = ptLen % keyLen
    inp = ""

    for i in range(0, quotient):
        for j in range(0, keyLen):
            c = int((ord(output[i*keyLen + j]) - ord('a') + 26 - (ord(key[j]) - ord('a'))%26 + ord('a')))
            #global input
            inp += chr(c)

    for i in range(0, remainder):
        c = int((ord(output[quotient*keyLen + i]) - ord('a') + 26 - (ord(key[i]) - ord('a'))%26 + ord('a')))
        #global input
        inp += chr(c)

    return inp

# 统计频率
def getLetterList(c_text):
    char_list = list(c_text)  # 转化为列表，每个字母为一个元素

    # 统计加密字符串中各个字母的出现次数
    tempSet = set(char_list)  # 化为集合去重

    # 保存为字典，key:字母，value:出现次数
    tempDict = {}
    for i in tempSet:
        tempDict[i] = char_list.count(i)

    # 列表排序, 以元组形式
    dict_sorted = sorted(tempDict.items(), key=lambda x: x[1], reverse=True)
    # print(dict_sorted)


    frequency_list = []
    print("字符", "出现次数", "频率")
    for i in dict_sorted:
        print(i[0], "\t", i[1], "\t", i[1] / len(c_text))
        frequency_list.append(i[0])     # 按照出现频率写入到列表

    return frequency_list

# Main
print("Vigenere Encrypto")
plainText = input("请输入明文: ")
key = input("请输入密钥: ")
CipherText = VigenereEncrypto(plainText, key)
print("密文为: " + CipherText)

print("Vigenere Decrypto")
cipherText = input("请输入密文: ")
key = input("请输入密钥: ")
PlainTextt = 'WithoutyouIdbeasoulwithoutapurposeWithoutyouIdbeanemotionwithoutaheartimafacewithoutexpressionAheartwithnobeatWithoutyoubymysideImjustaflamewithouttheheat'# VigenereDecrypto(cipherText, key)
print("明文为: " + PlainTextt)

 # 频率统计
print("明文频率统计： ")
getLetterList(plainText)
print("密文频率统计： ")
getLetterList(cipherText)