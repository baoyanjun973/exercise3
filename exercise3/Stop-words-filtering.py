import nltk
from nltk.corpus import stopwords

# 加载英文停用词列表
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# 打开并读取分词后的文件
with open('tokenized_text.txt', 'r', encoding='utf-8') as file:
    tokens = file.read().splitlines()

# 过滤停用词
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

# 将过滤后的tokens写入新文件
with open('filtered_tokens.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(filtered_tokens))