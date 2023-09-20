import time
import nltk
from nltk.tag import pos_tag
import matplotlib.pyplot as plt
from collections import Counter

# 打开并读取标注后的文件
with open('tagged_tokens.txt', 'r', encoding='utf-8') as file:
    tagged_tokens = file.read().splitlines()

# 提取词性标记
tags = [tagged_token.split('\t')[1] for tagged_token in tagged_tokens]

# 统计标记出现次数
tag_counts = Counter(tags)

# 获取出现次数最多的5个标记及其出现次数
pos_labels = tag_counts.keys()
frequencies = tag_counts.values()

# 绘制条形图
plt.bar(pos_labels, frequencies)
plt.xlabel('POS')
plt.ylabel('Frequency')
plt.title('POS Frequency Distribution')
plt.xticks(rotation=90)

# 展示图表
# plt.show()

# 将图表保存到文件
plt.savefig('pos_frequency_chart.jpg', bbox_inches='tight')