import re

# 关键字列表
key_list = ["auto", "break", "case", "char", "const", "continue", "default", "do",
            "double", "else", "enum", "extern", "float", "for", "goto", "if",
            "int", "long", "register", "return", "short", "signed", "sizeof", "static",
            "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"
            ]


# 读入文件
def read_file(file_path):
    # 读入文件在同一目录下可以直接写文件名
    with open(file_path, 'r', encoding='UTF-8') as f:
        text = f.read()
    return text


# 去除文本干扰成分（注释、字符串）
def clean_data(text):
    # 匹配所有注释
    pattern_notes = r'(//.*)|(/\*[\s\S]*?\*/)|(/\*[\s\S]*)'
    # 匹配单引号字符串
    pattern_str1 = r'(\'[\s\S]*?\')|(\'[\s\S]*)'
    # 匹配双引号字符串
    pattern_str2 = r'(\"[\s\S]*?\")|(\"[\s\S]*)'
    text = re.sub(pattern_notes, ' ', text, flags=re.MULTILINE)
    text = re.sub(pattern_str1, ' ', text, flags=re.MULTILINE)
    text = re.sub(pattern_str2, ' ', text, flags=re.MULTILINE)
    return text


def key_count(text):
    pattern_num = r'[a-zA-Z]{2,}'
    key_data = re.findall(pattern_num, text)
    num = 0
    for key in key_list:
        num += key_data.count(key)
    return key_data, num


def switch_case_count(key_data):
    case_num = []
    switch_num = 0
    temp_case = 0
    for value in key_data:
        if value == "switch":
            switch_num += 1
            if temp_case > 0:
                case_num.append(temp_case)
                temp_case = 0
        if value == "case":
            temp_case += 1
    case_num.append(temp_case)

    return switch_num, case_num


if __name__ == "__main__":
    temp_text = read_file('text.cpp')
    temp_text = clean_data(temp_text)
    temp_key, temp_num = key_count(temp_text)
    print("total num:", temp_num)
    print(temp_key)
    temp_switch_num, temp_case_num = switch_case_count(temp_key)
    print("switch num:", temp_switch_num)
    print("case num: ", end='')
    for index, temp_value in enumerate(temp_case_num):
        if index + 1 == len(temp_case_num):
            print(temp_value, end='')
        else:
            print(temp_value, end=' ')

