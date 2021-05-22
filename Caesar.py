# -*-coding:utf-8-*-

# Caesar's 
# by Kisna 21.5.20

# 加密模块
def plain_to_shadow():
    # print("请输入明文：")
    # plaincode = input()
    print("输出密文为：")
    for p in plaincode:
        if ord("a") <= ord(p) <= ord("z"):
            print((chr(ord("a") + (ord(p) - ord("a") + 3) % 26)),end = '')
        else:
            print(p,end = '')
    print()


# 加密模块
def shadow_to_plain():
    # print("请输入密文：")
    # shadowcode = input()
    print("输出明文为：")
    for q in shadowcode:
        if ord("a") <= ord(q) <= ord("z"):
            print((chr(ord("a") + (ord(q) - ord("a") - 3) % 26)),end = '')
        else:
            print(q,end = '')
    print()


# 统计频率
def getLetterList(c_text):
    char_list = list(c_text)  # 转化为列表，每个字母为一个元素

    # 统计加密字符串中各个字母的出现次数
    #  Q X Z
    tempSet = set(char_list)  # 抓转为集合去重

    # 保存为字典，key:字母，value:出现次数
    tempDict = {}
    for i in tempSet:
        tempDict[i] = char_list.count(i)

    # 列表排序, 以元组形式
    dict_sorted = sorted(tempDict.items(), key=lambda x: x[1], reverse=True)
    # print(dict_sorted)


    frequency_list = []
    print("字母", "出现次数", "频率")
    for i in dict_sorted:
        print(i[0], "\t", i[1], "\t", i[1] / len(c_text))
        frequency_list.append(i[0])     # 按照出现频率写入到列表

    return frequency_list


# Main
print("请输入明文：")
plaincode = input()
plain_to_shadow()

print("请输入密文：")
shadowcode = input()
shadow_to_plain()

print("明文频率统计：")
getLetterList(plaincode)
print("密文频率统计：")
getLetterList(shadowcode)