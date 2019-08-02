import re
ID_num = str(input('Please input ID_num: '))

#檢查ID_num[0]是否為英文字母，且不分大小寫
str_partten1 = re.compile(r'([a-z])', re.I)
ID_partten1 = str_partten1.match(ID_num[0])
#檢查ID_num[2:9]是否出現數字以外的字元
str_partten2 = re.compile(r'([^0-9])')
ID_partten2 = str_partten2.findall(ID_num[2:10])
#檢查ID_num的字元是否為10個
if(len(ID_num) != 10):
    print('False')
#檢查ID_num[0]是否為英文字母
elif(ID_partten1 == None):
    print('False')
#檢查ID_num[1]是否有非1 or 2以外的字元
elif(ID_num[1] != '1' and ID_num[1] != '2'):
    print('False')
#檢查ID_num[2:9]是否出現數字以外的字元
elif(ID_partten2 != []):
    print('False')
#輸出該ID
else:
    print(ID_num + ' is True')