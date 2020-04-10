## 安装anaconda, 创建py环境

conda命令

```
conda --version
conda env list # 查看目前已创建的py环境
activate <env_name> # 激活环境
conda deactivate # exit
conda update conda # base环境下更新
```

conda替换为国内源

```shell
显示chuannels信息
$ conda config --show channels
删除默认的channel，并增加国内清华的conda源
$ conda config --remove channels defaults
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
$ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
$ conda config --set show_channel_urls yes
```
## 安装vscode

### extension

- code runer : 代码运行

  >运行: `ctrl + alt + N`
  >
  >直接终端运行(两种方法如下): 
  >> `CTRL + , `打开setting->Extensions->Run code->Run inTerminal
  >>
  >>```json
  >> "code-runner.runInTerminal": true //code runner直接打开终端运行
  >> ```

- tabnine : 代码自动补全

### 快捷键shortcuts

|                |                  |
| -------------- | ---------------- |
| ctrl+w         | 关闭页面         |
| ctrl+,(逗号)   | 打开设置         |
| ctrl+`(左上角) | 打开终端         |
| ctrl+shift+G   | 打开代码管理工具 |

