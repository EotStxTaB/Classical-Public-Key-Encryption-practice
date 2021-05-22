#-*-coding:utf-8-*-

# Playfair
# by Kisna 21.5.20

'''
tips:1、若明文字母数量为奇数，在明文末尾添加一个'Z'     
     2、'I'与'J'同
'''

letter_list = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'
T_letter = ['','','','','']
 
# 根据密钥建立密码表
def Create_Matrix(key):
  key = Remove_Duplicates(key)  
  key = key.replace(' ','') # 去除密钥中的空格
  
  for ch in letter_list:  # 根据密钥获取新组合的字母表
    if ch not in key:
      key += ch
  
  j = 0
  for i in range(len(key)): # 将新的字母表里的字母逐个填入密码表中，组成5*5的矩阵
    T_letter[j] += key[i]     # j用来定位字母表的行
    if 0 == (i + 1) % 5:
      j += 1
 
# 移除字符串重复的字母
def Remove_Duplicates(key):
  key = key.upper() # 转成大写字母组成的字符串
  keyy = ''
  for ch in key:
    if ch == 'I':
      ch = 'J'
    if ch in keyy:
      continue
    else:
      keyy += ch
  return keyy
 
# 获取字符在密码表中的位置
def Get_MatrixIndex(ch):
  for i in range(len(T_letter)):
    for j in range(len(T_letter)):
      if ch == T_letter[i][j]:
        return i,j     # i为行，j为列
 
# 加密模块
def Encrypt(plaintext, T_letter):
  ciphertext = ''
  
  if len(plaintext)%2 != 0:  # 如果新的明文长度为奇数，在其末尾添上'Z'
    plaintext += 'Z'
  
  i = 0
  while i < len(plaintext): # 对明文进行遍历
    if True == plaintext[i].isalpha():  # 如果是明文是字母的话，
      j = i+1                           # 则开始对该字母之后的明文进行遍历，
      while j < len(plaintext):         # 直到遍历到字母，进行加密
        if True == plaintext[j].isalpha():
          if 'I' == plaintext[i].upper():             #
            x = Get_MatrixIndex('J')                  #
          else:                                     #
            x = Get_MatrixIndex(plaintext[i].upper()) # 对字符在密码表中的坐标
          if 'I' == plaintext[j].upper():             # 进行定位,同时将'I'作为
              y = Get_MatrixIndex('J')                # 'J'来处理
          else:                                     #
            y = Get_MatrixIndex(plaintext[j].upper()) #
          
          if x[0] == y[0]:    # 如果在同一行
            ciphertext += T_letter[x[0]][(x[1]+1) % 5] + T_letter[y[0]][(y[1]+1) % 5]
          elif x[1] == y[1]:  # 如果在同一列
            ciphertext += T_letter[(x[1]+1) % 5][x[0]] + T_letter[(y[1]+1) % 5 ][y[0]]
          else:             # 如果不同行不同列
            ciphertext += T_letter[x[0]][y[1]] + T_letter[y[0]][x[1]]
          break;  # 每组明文对加密完成后，结束本次对明文的遍历
        j += 1
      i = j+1  # 每次对明文的遍历是从加密过后的明文的后一个明文开始的,结束本次循环
      continue
    else:
      ciphertext += plaintext[i]  # 如果明文不是字母，直接加到密文上
    i += 1
    
  return ciphertext
 
# 解密模块
def Decrypt(ciphertext, T_letter):
  plaintext = ''
  if len(ciphertext) % 2 != 0:  # 如果新的密文长度为奇数，在其末尾添上'Z'
    ciphertext += 'Z'
  
  i = 0
  while i < len(ciphertext): # 对密文进行遍历
    if True == ciphertext[i].isalpha():  # 如果是密文是字母的话，
      j = i + 1                            # 则开始对该字母之后的密文进行遍历，
      while j < len(ciphertext):         # 直到遍历到字母，进行解密
        if True == ciphertext[j].isalpha():
          if 'I' == ciphertext[i].upper():              
            x = Get_MatrixIndex('J')                    
          else:                                       
            x = Get_MatrixIndex(ciphertext[i].upper())  #对字符在密码表中的坐标
          if 'I' == ciphertext[j].upper():              #进行定位,同时将'I'作为
              y = Get_MatrixIndex('J')                  #'J'来处理
          else:                                       
            y = Get_MatrixIndex(ciphertext[j].upper())  
          
          if x[0] == y[0]:    # 如果在同一行
            plaintext += T_letter[x[0]][(x[1]-1) % 5] + T_letter[y[0]][(y[1]-1 )% 5]
          elif x[1] == y[1]:  # 如果在同一列
            plaintext += T_letter[(x[1]-1) % 5][x[0]] + T_letter[(y[1]-1) % 5][y[0]]
          else:             # 如果不同行不同列
            plaintext += T_letter[x[0]][y[1]] + T_letter[y[0]][x[1]]
          break;  # 每组密文对解密完成后，结束本次对密文的遍历
        j += 1
      i = j + 1  # 每次对密文的遍历是从解密过后的密文的后一个密文开始的,结束本次循环
      continue
    else:
      plaintext += ciphertext[i]  #如果密文不是字母，直接加到明文上
    i += 1
    
  return plaintext


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
if __name__ == '__main__': 
    key = input("请输入密钥生成关键词: ")
    Create_Matrix(key)  #建立密码表

    # 加密
    print('请输入明文:')
    plaintext = input()
    print("密文为:\n%s" % Encrypt(plaintext,T_letter))

    # 解密
    print('请输入密文:')
    ciphertext = input()
    print('明文为:\n%s' % Decrypt(ciphertext,T_letter))

    # 频率统计
    print("明文频率统计： ")
    getLetterList(plaintext)
    print("密文频率统计： ")
    getLetterList(ciphertext)