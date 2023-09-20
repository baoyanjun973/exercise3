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
pos_labels, frequencies = zip(*tag_counts.most_common(5))

# 绘制条形图
plt.figure(figsize=(10, 6))  # 设置图表大小
plt.bar(pos_labels, frequencies, color='skyblue')  # 设置颜色
plt.xlabel('POS Tags')
plt.ylabel('Frequency')
plt.title('Top 5 POS Tags Frequency Distribution')
plt.xticks(rotation=45)  # 旋转标签以避免重叠

# 添加数据标签
for i, v in enumerate(frequencies):
    plt.text(i, v + 10, str(v), ha='center', va='bottom')

# 保存图表到文件
plt.savefig('pos_frequency_chart.png', bbox_inches='tight', dpi=300)

# 显示图表
plt.show()
