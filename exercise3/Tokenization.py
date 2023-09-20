import nltk
from nltk.tokenize import word_tokenize

# 打开并读取文件
with open('Moby-Dick.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 进行分词处理
tokens = word_tokenize(text)

# 将分词后的tokens写入新文件
with open('tokenized_text.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(tokens))