import re

#检查str是否以连续的字母开头+连续的数字结束
def check_string(input_string):
    pattern = r'^[a-zA-Z]+[0-9]*(\.[0-9]+)?$'
    if re.match(pattern, input_string):
        return True
    else:
        return False
#去掉字符串中的字母
def remove_letters(input_string):
    pattern = r'[a-zA-Z]+'
    return re.sub(pattern, '', input_string)
#判断字符串是否有小数点 
def process_string(input_string):
    parts = input_string.split('.')
    if len(parts) > 1:
        second_part = parts[1]
        if len(second_part) > 2:
            second_part = second_part[:2]
        elif len(second_part) < 2:
            second_part += '0' * (2 - len(second_part))
        return parts[0]+"."+second_part
    else:
        return input_string+'.00'

state=True
while state:
    str=input("请输入一个前面是字母，后边是数字的字符串");
    print(str)
    if check_string(str):
        print("您的输入符合规范")
        #去掉字符串中的字母
        num=re.sub(r'[a-zA-Z]', '', str)
        re_num=process_string(num)
        print(re_num)
        state=False
    else:
        print("您的输入有误，请重新输入")
        state=True