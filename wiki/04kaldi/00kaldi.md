Kaldi的目标和==HTK==(是?)类似，它需要提供现代和灵活的代码，使用C++实现，容易修改和扩展。它包括如下重要特性：

- 代码级别集成==WFST==([介绍-李](<http://fancyerii.github.io/wfst/wfst/>))
  - Kaldi是把OpenFST作为一个库编译进来。(而不是脚本的方式集成)。
- 广泛的线性代数支持
  - Kaldi包括封装了标准BLAS和LAPACK库的[矩阵库](http://kaldi-asr.org/doc/matrix.html)。
- 可扩展的设计
  - 如果可能的话，我们提供的算法会尽量的通用。比如，我们的decoder是基于模板，模板的对象根据(frame, fst-input-symbol)来计算score。这就意味着decoder可以很容易的用神经网络梯度GMM模型。
- 完整的recipe
  - 对于很多常见语音数据集(主要是LDC的数据，当然也有一些其它开源数据集)都提供完整的recipe，从而可以完整的复现整个过程。