- 为什么加窗

  语音信号一般在10ms到30ms之间，我们可以把它看作是平稳的。（一般20ms）

- 为什么汉明窗（不是矩形窗）

  因为之后我们会对汉明窗中的数据进行FFT，它假设一个窗内的信号是代表一个周期的信号。加上汉明窗后，数据形状就有点周期的感觉了。

- 为什么移动窗函数有重叠

  因为加上汉明窗，只有中间的数据体现出来了，两边的数据信息丢失了，所以等会移窗的时候，只会移1/3或1/2窗，这样被前一帧或二帧丢失的数据又重新得到了体现。（一般移动帧10ms）
