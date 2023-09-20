import nltk
from nltk.tag import pos_tag

# 打开并读取过滤后的文件
with open('filtered_tokens.txt', 'r', encoding='utf-8') as file:
    tokens = file.read().splitlines()

# 进行词性标注
tagged_tokens = pos_tag(tokens)

# 将标注后的tokens写入新文件
with open('tagged_tokens.txt', 'w', encoding='utf-8') as file:
    for token, tag in tagged_tokens:
        file.write(token + '\t' + tag + '\n')