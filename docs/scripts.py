import os
import re

def read_file_binary(file_path):
    # 读取文件为二进制数据
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    
    # 尝试使用UTF-8解码，如果失败则尝试GBK
    try:
        return raw_data.decode('utf-8')
    except UnicodeDecodeError:
        return raw_data.decode('gbk')

def remove_lines_with_string(directory, pattern):
    # 编译正则表达式模式
    compiled_pattern = re.compile(pattern)
    
    # 递归遍历目录
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # 构造文件完整路径
            file_path = os.path.join(root, filename)
            
            # 读取文件内容
            content = read_file_binary(file_path)
            
            # 按行分割内容，并删除包含指定字符串的行
            new_lines = [line for line in content.splitlines() if not compiled_pattern.search(line)]
            
            # 将新的内容写回文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write('\n'.join(new_lines))

# 使用示例
directory_to_search = '/Users/zcy/dev/vitepress/findbook/docs/posts/2024/人文社科'  # 替换为要搜索的目录
string_to_search = '（访问密码：9080）'  # 要搜索的字符串
remove_lines_with_string(directory_to_search, string_to_search)