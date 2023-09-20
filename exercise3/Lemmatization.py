import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# 初始化WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# 标记WordNetLemmatizer用到的POS tag
tag_mapping = {
    'N': 'n',  # Nouns
    'V': 'v',  # Verbs
    'R': 'r',  # Adverbs
    'J': 'a'   # Adjectives
}

# 打开并读取tag标记文件
with open('tagged_tokens.txt', 'r', encoding='utf-8') as file:
    tagged_tokens = file.read().splitlines()

# 提取tokens和POS tag
tokens_pos = [(token.split('\t')[0], token.split('\t')[1]) for token in tagged_tokens]

# 得到前20个tokens
top20_tokens = [token for token, pos in tokens_pos[:20]]

# 还原tokens
lemmatized_tokens = []
for token, pos in tokens_pos[:20]:
    pos_tag = pos[0]
    if pos_tag in tag_mapping:
        pos_tag = tag_mapping[pos_tag]
    else:
        pos_tag = 'n'
    lemmatized_token = lemmatizer.lemmatize(token, pos=pos_tag)
    lemmatized_tokens.append(lemmatized_token)

# 打印tokens和lemmatized tokens
for token, lemmatized_token in zip(top20_tokens, lemmatized_tokens):
    print(f"{token} --> {lemmatized_token}")

# 将结果保存到文件中
with open('token_lemmatized_token.txt', 'w', encoding='utf-8') as file:
    for token, lemmatized_token in zip(top20_tokens, lemmatized_tokens):
        file.write(f"{token} --> {lemmatized_token}\n")