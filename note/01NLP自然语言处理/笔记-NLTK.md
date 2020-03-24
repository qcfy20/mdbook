```python
# NLTK第一章
from nltk.book import *

# 搜索文本中单词出现的位置
# text1.concordance("<query>")

# 根据上下文, 搜索词性或词义相近的词
# text1.similar("<query>")

# 研究两个及以上词的上下文(可以判断词性是否相近)
# text1.common_contexts(["A", "B"])

# 根据单词在文本中的位置生成离散图(需要numpy,matplotlib模块)
# text4.dispersion_plot(["citizens","democracy","freedom","duties","China"])

# 根据源文本随机生成文本
# text3.generate()

# 计算文本长度,包括词和标识符
word = len(text3)
# 统计所有出现的词汇和标识符,正序排序
sorted(set(text3))
```

![1584001856376](assets/1584001856376.png)

### 自然语言理解

词义消歧

指代消解,语义角色标注

NLG自动语言生成

机器翻译

