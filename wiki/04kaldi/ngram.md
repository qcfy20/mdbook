| ngram-count参数 | 作用                                                         |
| :-------------- | ------------------------------------------------------------ |
| -text           | 指定输入训练文本路径                                         |
| -order          | 训练几阶语法模型，比如：`-order 3` 训练3-gram                |
| -limit-vocab    | 仅仅计算词典中出现的单词，后面需要参数`-vocab`指定字典。<br>字典中没有出现的单词在训练文本中出现，则会被认为是未知词汇（unknown word），<br/>这些未知词汇会被认为是参数`-map-unk`所指定的词汇 |
| -vocab          | 指定词典文件                                                 |
| -unk            | 如果指定该选项，语言模型中保留未知词汇的语言模型；<br>如果不指定那么语言模型跟unknow word相关的计数不会被保存 |
| -map-unk        | 指定将未知词汇映射成哪个词汇，一般使用特殊字符“<unk>”表示未知词汇 |
| -kndiscount     | 使用Kneser-Ney计数方法，只要是跟平滑相关                     |
| -interpolate    | 插值预测，主要是解决语言模型数据稀疏性问题                   |
| -lm             | 指定输入语言模型位置                                         |

