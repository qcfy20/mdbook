## Ubuntu之kaldi编译安装

### 编译安装kaldi

系统是Linux Ubuntu 16.04。具体过程如下

1. 安装一些依赖工具与第三方库
```shell
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
sudo apt-get install bc
sudo apt-get install g++
sudo apt-get install zlib1g-dev make automake autoconf bzip2 libtool subversion
sudo apt-get install libatlas3-base
```

> - autoconf
> - automake
> - libtool
> - atlas  根据系统自动选择最优的线性代码库的库
> - wget 下载工具(好像也不需要)
> - zlib 数据压缩工具(bzip都可以)

2. 下载kaldi，终端输入(注意文件路径)

```shell
git clone https://github.com/kaldi-asr/kaldi.git
cd kaldi/tools
```

3. 用kaldi自带的脚本`check_dependencies.sh`来检测是否安装完所有必须的依赖工具

```shell
extras/check_dependencies.sh
```

根据提示安装必须的依赖。比如提示缺少mkl，需要用tools目录下自带的脚本`extras/install_mkl.sh`来安装mkl

4. 安装mkl, 如果提示权限不足在执行命令前加上`sudo`

```shell
sudo extras/install_mkl.sh
```

多次运行`check_dependencies.sh`检查依赖，得到如下提示，则说明所有依赖都安装成功。

```shell
extras/check_dependencies.sh: all OK.
```

5. 编译tools

```shell
cd kaldi/tools # 进入tools目录
make -j 2 # 多进程编译;根据cpu选择线程数,高于机器配置容易卡死
```

6. 编译src

```shell
cd kaldi/src # 进入src目录
./configure --shared
make depend -j 2
make -j 2
```

这个步骤比较花时间，编译成功后，提示如下

```
Running matrix-lib-test ... 3s... SUCCESS matrix-lib-test
Running sparse-matrix-test ... 0s... SUCCESS sparse-matrix-test
make[1]: Leaving directory '/home/rootuser/speech_2019/kaldi/src/matrix'
echo Done
Done
```

7. 运行自带的yesno例子，测试安装是否成功

```shell
cd kaldi/egs/yesno/s5 # 进入egs/yesno/s5目录
./run.sh # 运行脚本
```

### 编译安装srilm

语言模型训练需要用到srilm

1. 进入下载地址，下载`srilm-1.7.3.tar.gz`
2. 将`srilm-1.7.3.tar.gz`拷贝到`/kaldi/tools`目录下并重命名为`srilm.tar.gz`，运行安装脚本

```shell
cd kaldi/tools
mv srilm-1.7.3.tar.gz srilm.tar.gz
./install_srilm.sh
```

### 参考

- [kaldi的编译安装与报错解决方法-csdn](https://blog.csdn.net/ybdesire/article/details/90760196)