# 基础

- 安装vscode

### extension

- code runer : 代码运行

  >运行: `ctrl + alt + N`
  >
  >直接终端运行(两种方法如下): 
  >> `CTRL + , `打开setting->Extensions->Run code->Run inTerminal
  >
  >>```json
  >> "code-runner.runInTerminal": true //code runner直接打开终端运行
  >> ```

- tabnine : 代码自动补全

# 快捷键shortcuts

|                |                  |
| -------------- | ---------------- |
| ctrl+w         | 关闭页面         |
| ctrl+,(逗号)   | 打开设置         |
| ctrl+`(左上角) | 打开终端         |
| ctrl+shift+G   | 打开代码管理工具 |

# 配置开发环境

### 1. python

- 安装anaconda, 创建py环境

  > ```
  > conda --version
  > conda env list # 查看目前已创建的py环境
  > activate <env_name> # 激活环境
  > conda deactivate # exit
  > conda update conda # base环境下更新
  > ```
  >

### 2. C

### 3. Git

修改git默认编辑器为vscode, 在git bash 运行

```bash
git config --global core.editor "code --wait"
```
> vscode编辑器特色
>
> - 行数显示附近标注: 红色代表有删除行, 蓝色表示修改, 绿色表示新增 
> - ctrl+shift+G: 打开源代码管理工具,查看修改文件和文件状态
> - 左下角显示当前活动分支状态
>

