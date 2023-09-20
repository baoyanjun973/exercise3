import nltk
from nltk.tag import pos_tag
from collections import Counter

# 从tag.txt文件中读取词性数据
with open('tagged_tokens.txt', 'r', encoding='utf-8') as file:
    tagged_tokens = [line.strip().split('\t') for line in file]

# 创建一个字典来记录词性及其出现次数
pos_counts = {}
for _, tag in tagged_tokens:
    if tag in pos_counts:
        pos_counts[tag] += 1
    else:
        pos_counts[tag] = 1

# 按照词性出现次数进行排序
sorted_pos_counts = sorted(pos_counts.items(), key=lambda x: x[1], reverse=True)

# 打印前五个最频繁的词性
print("五个最频繁的词性：")
for tag, count in sorted_pos_counts[:5]:
    print(f"{tag}: {count}次")
