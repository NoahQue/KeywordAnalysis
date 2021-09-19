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
        temp_text = f.read()
    return temp_text


# 去除文本干扰成分（注释、字符串）
def clean_data(temp_text):
    # 匹配所有注释
    pattern_notes = r'(//.*)|(/\*[\s\S]*?\*/)|(/\*[\s\S]*)'
    # 匹配单引号字符串
    pattern_str1 = r'(\'[\s\S]*?\')|(\'[\s\S]*)'
    # 匹配双引号字符串
    pattern_str2 = r'(\"[\s\S]*?\")|(\"[\s\S]*)'
    temp_text = re.sub(pattern_notes, ' ', temp_text, flags=re.MULTILINE)
    temp_text = re.sub(pattern_str1, ' ', temp_text, flags=re.MULTILINE)
    temp_text = re.sub(pattern_str2, ' ', temp_text, flags=re.MULTILINE)
    return temp_text


def key_count(temp_text):
    pattern_num = r'[a-zA-Z]{2,}'
    temp_data = re.findall(pattern_num, temp_text)
    temp_num = 0
    for key in key_list:
        temp_num += temp_data.count(key)
    return temp_data, temp_num


if __name__ == "__main__":
    text = read_file('text.cpp')
    text = clean_data(text)
    key_data, num = key_count(text)
    print("total num:", num)
