import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.probability import FreqDist

# 下载VADER词典
nltk.download('vader_lexicon')

# 读取分词和去除停用词后的结果
with open('filtered_tokens.txt', 'r', encoding='utf-8') as file:
    tokens = file.read().split()

# 统计词频
freq_dist = FreqDist(tokens)

# 选择最常见的1000个词汇
top_words = freq_dist.most_common(1000)

# 构建词汇表
vocab = [word for word, _ in top_words]

# 初始化情感强度分析器
sid = SentimentIntensityAnalyzer()

# 更新情感强度分析器的词典
for word in vocab:
    scores = sid.polarity_scores(word)
    sid.lexicon[word] = scores['compound']

# 定义批次大小
batch_size = 100

# 批次情感分析
sentiment_scores = []
for i in range(0, len(tokens), batch_size):
    batch = tokens[i: i+batch_size]
    batch_scores = [sid.polarity_scores(word)['compound'] for word in batch]
    sentiment_scores.extend(batch_scores)

# 计算平均情感分数
average_sentiment_score = sum(sentiment_scores) / len(sentiment_scores)

# 判断文本的情感倾向
threshold = 0.05
overall_sentiment = 'positive' if average_sentiment_score > threshold else 'negative'

# 输出平均情感分数和情感倾向
print(f"Average Sentiment Score: {average_sentiment_score}")
print(f"Overall Sentiment: {overall_sentiment}")