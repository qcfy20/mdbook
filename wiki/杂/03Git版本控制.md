## 术语

**git**源代码管理器/版本控制系统

**repo**: 版本库

**working** directory: 工作区

**staging** index: 暂存区

**commit**: 提交

**SHA**: commit 标识

**Branch**: 项目分支

##  emoji 指南

| emoji | emoji 代码 | commit 说明 |
| :-- | :-- | :-- |
| :art: (调色板) | `:art:` | 改进代码结构/代码格式 |
|:zap: (闪电):racehorse: (赛马)|`:zap:“:racehorse:`| 提升性能 |
| :fire: (火焰) | `:fire:` | 移除代码或文件 |
| :bug: (bug) | `:bug:` | 修复 bug |
| :ambulance: (急救车) | `:ambulance:` | 重要补丁 |
| :sparkles: (火花) | `:sparkles:` | 引入新功能 |
| :memo: (备忘录) | `:memo:` | 撰写文档 |
| :rocket: (火箭) | `:rocket:` | 部署功能 |
| :lipstick: (口红) | `:lipstick:` | 更新 UI 和样式文件 |
| :tada: (庆祝) | `:tada:` | 初次提交 |
| :white_check_mark: (白色复选框) | `:white_check_mark:` | 增加测试 |
| :lock: (锁) | `:lock:` | 修复安全问题 |
| :apple: (苹果) | `:apple:` | 修复 macOS 下的问题 |
| :penguin: (企鹅) | `:penguin:` | 修复 Linux 下的问题 |
| :checkered_flag: (旗帜) | `:checked_flag:` | 修复 Windows 下的问题 |
| :bookmark: (书签) | `:bookmark:` | 发行/版本标签 |
| :rotating_light: (警车灯) | `:rotating_light:` | 移除 linter 警告 |
| :construction: (施工) | `:construction:` | 工作进行中 |
| :green_heart: (绿心) | `:green_heart:` | 修复 CI 构建问题 |
| :arrow_down: (下降箭头) | `:arrow_down:` | 降级依赖 |
| :arrow_up: (上升箭头) | `:arrow_up:` | 升级依赖 |
| :construction_worker: (工人) | `:construction_worker:` | 添加 CI 构建系统 |
| :chart_with_upwards_trend: (上升趋势图) | `:chart_with_upwards_trend:` | 添加分析或跟踪代码 |
| :hammer: (锤子) | `:hammer:` | 重大重构 |
| :heavy_minus_sign: (减号) | `:heavy_minus_sign:` | 减少一个依赖 |
| :whale: (鲸鱼) | `:whale:` | Docker 相关工作 |
| :heavy_plus_sign: (加号) | `:heavy_plug_sign:` | 增加一个依赖 |
| :wrench: (扳手) | `:wrench:` | 修改配置文件 |
| :globe_with_meridians: (地球) | `:globe_with_meridians:` | 国际化与本地化 |
| :pencil2: (铅笔) | `:pencil2:` | 修复 typo |


## 常用命令

### 1. 配置git 

```bash
git config --list
```

安装完Git, 查看用户配置文件

> ```bash
> git config --global user.name "<full-name>" # 用户名
> git config --global user.email "<email-address>" # 用户邮箱地址
> git config --global core.editor "code --wait" # 配置编辑器vscode
> ```
>
> 连接github
>
> ```bash
> ssh-keygen -t rsa -C "l201583332@gmail.com" # 生成ssh key,本地用户文件夹下生成.ssh的文件夹
> 
> .ssh文件夹下打开.pub文件,复制文本到github setting新建SSH
>
> ssh -T git@github.com # git终端执行命令, 输入yes,测试本地和github通信配置
> ```


### 2. 创建git仓库

```bash
git init 
```
可以在当前目录下创建新的空仓库。 自动生成 `.git`隐藏目录,  它存储了所有的配置文件和目录，以及所有的 commit。 

> 补充知识:终端命令
>
> - ls -a 列出文件目录,包括隐藏文件
> - mkdir <file_name> 新建文件夹
> - cd 切换工作目录  例如 `cd ..`返回上层目录; `cd d:/`打开D盘工作目录; `cd` 返回根目录 
> - rm <文件> 删除文件
> - pwd 列出当前工作路径
> - touch <文件名> 新建文件; 然后去编辑器中修改代码

```bash
git clone [仓库url] [文件名]
```

复制仓库到本地计算机; 默认文件名为原仓库名; 如果需要push到github选择ssh格式

```bash
git status # @常用命令
```
查看仓库状态 

> ```bash
> On branch master  # master表示默认分支
> nothing to commit, working directory clean # 已跟踪文件在上次提交后都未被
> ```
>
> ```bash
> nothing to commit (create/copy files and use "git add" to track) # 尚未有任何提交
> ```

### 3. 查看仓库commit记录

 git 使用命令行分页器 less 浏览所有信息。以下是 less 的重要快捷键：
>
> - 要按行向下滚动，使用 `j` 或 `↓`
> - 要按行向上滚动，使用 `k` 或 `↑`
> - 要按页向下滚动，使用**空格键**或 `f`或Page Down 按钮
> - 要按页向下滚动，使用 `b` 或 Page Up 按钮
> - 要退出，使用 `q`或者Ctrl+c

```bash
git log
```
打印日志, *默认情况下*，该命令会显示仓库中每个 commit 的：SHA; 作者; 日期; 消息

> 命令选项
> ```bash
> git log --oneline # 单行显示 commit 的SHA的前 7 个字符;消息(包括标签,分支) @常用命令
> ```
>
> ```bash
> git log --stat # 显示被修改的文件;显示添加/删除的行数;显示一个摘要，其中包含修改/删除的总文件数和总行数
> (stat是“统计信息 statistics”的简称)
> ```
>
> ```bash
> git log -p / --patch # 显示具体修改内容更改(补丁消息)
> git log -p -w # 将显示补丁信息，但是不会突出显示仅更改了空格的行。
> git log -p fdf5493 # 查看特定commit修改信息
> ```
```bash
git show 
```
显示最近一次 commit。 包括commit的SHA;作者;日期;commit 消息(提交说明);补丁信息(具体修改内容)

> ```bash
> git show fdf5493 # 显示特定commit
> ```

### 4. 仓库添加commit

```bash
git add <文件名1> <文件名2> 
```
将新建或修改的**文件**从工作目录添加到暂存区(多个文件用空格分隔)
> ```bash
> git add .  # 表示当前目录下所有文件添加到暂存区(包括所有嵌套目录和文件) @常用命令
> 
> git rm --cached <file> # 将添加到暂存区的文件撤回
> git reset HEAD <file> # 撤回暂存区文件 @为什么有的必须用HEAD指针撤回
> ```

```bash
git commit # 常用命令
```

跳转编辑器(之前设置的vscode), 编辑并**保存**commit提交说明, `ctrl+w` 关闭vscode

> ```bash
> git commit -m "提交说明" # `-m`直接在Git Bash完成提交说明 
> ```

```bash
git push # 推送到云端github
```

提交说明

```bash
第一行是不超过50个字的提要, 分类: 提要
(然后空一行)
罗列出改动原因、主要变动、以及需要注意的问题。
(最后)
提供对应的网址（比如Bug ticket）。
```

> 规范样式
> - **feature**： 新功能
> - **fix**：错误修复
> - **docs**：文档修改
> - **style**：格式、分号缺失等，代码无变动
> - **refactor**：生产代码重构
> - **test**：测试添加、测试重构等，生产代码无变动
> - **chore**：构建任务更新、程序包管理器配置等，生产代码无变动

```bash
git diff
```

 编辑器修改并保存文件, 运行命令查看修改前后的具体内容(`git log -p`实际后台使用`git diff`命令)

```bash
touch .gitignore # 根目录新建`.gitignore`文件
```

忽略特定文件, 告诉 git 不应跟踪的文件。 

> 通配符: 
>
> - `#` - 将行标记为注释
>
> - `*` - 与 0 个或多个字符匹配
>
> - `?` - 与 1 个字符匹配
>
> - `[abc]` - 与 a、b 或 c 匹配
>
> - `**` 与嵌套目录匹配 (例a/**/c匹配目录a/c, a/b/c)
>

### 5. 标签\分支\合并

```bash
git tag
```

列出仓库所有标签

> ```bash
> git tag  <tag1> # 直接创建标签, 标签默认与最近提交的commit绑定; 同一commit可以绑定多个标签
> git tag -a <tag2> [SHA] # 跳转编辑器, 编辑说明及注释, 标签与特定commit绑定 @如何看到自己编辑的说明
> git tag -d <tag1> #删除标签
> ```
>
> ```bash
> git log # 查看日志及标签
> git log --oneline --graph --all # 显示所有分支commit
>```
> 

```bash
git branch
```

列出仓库所有分支, 着重显示**当前分支**

> ```bash
> git branch <分支名> # 创建分支 
> git branch <分支名> [SHA] # [可以省略];创建分支指向特定commit
> ```
>
> ```bash
> git checkout <分支名1> # 切换活动分支
> git checkout -b <新建分支名2> <原分支名># 创建并切换到新建分区 @常用命令
> ```
>
> ```bash
> # 无法删除当前所在分支,切换到master再执行命令
> git branch -d <分支名1> # 删除已经合并(merge)的分支(该分支commit存在于其他分支)
> git branch -D <分支名1> # 强制删除分支
> ```

```bash
git merge <other-branch> 
```

将其他分支合并到当前活动分支; 当前分支HEAD指针一定会向前移动commit

> ```bash
> git reset --hard HEAD^ # 撤销合并
> ```
> 
>合并出现冲突->`git status`显示具体冲突位置->手动修改提交

### 6. 撤销更改

```bash
git restore --staged <file> # 撤销暂存区文件到工作区
git restore <file> # 撤销工作区文件修改到原文件
```

```bash
git commit --amend
```

修改最近提交的commit; 避免反复创建相似的commit

```bash
git revert <SHA-of-commit-to-revert> # 还原commit
```

- 将撤消目标 commit 所做出的更改
- 创建一个新的 commit 来记录这一更改

```bash
git reset <reference-to-commit> # 重置commit
```

- 将撤消目标 commit 所做出的更改
- 清除 commit 

> **相关commit引用**
>
> - `^` – 表示父 commit (HEAD^^表示fufu)
> - `~` – 表示第一个父 commit (HEAD~3表示fufufu)
> -  `^` 引用用来表示第一个父 commit，而 `^2` 表示第二个父 commit。第一个父 commit 是当你运行 `git merge` 时所处的分支，而第二个父 commit 是被合并的分支。 (HEAD^^2表示fufu2)

> ```bash
> git reset --mixed HEAD^ # 撤销commit到工作区;默认选项可省略
> git reset --soft HEAD^ # 撤销commit到暂存区 @巧记:来软的
> git reset --hard HEAD^ # 撤销commit到回收站 @巧记:来硬的
> ```
>
> ```bash
> git branch backup # 重置命令前先备份分支
> ```

## 流程规范

### 1. 新建分支

 首先，每次开发新功能，都应该新建一个单独的分支 

```bash
# ssh方式克隆到本地
git clone git@url 
# 获取主干最新代码
git checkout master
git pull # 拉取
# 新建一个开发分支myfeature;同时切换到myfeature活动分支
git checkout -b myfeature
```

### 2. 提交分支commit

```bash
git add . # 添加全部修改文件到暂存区
git status 
git commit [--verbose] # 跳转编辑器;verbose参数(可选)，会列出 diff 的结果。
```

### 3. 与主干同步

 分支的开发过程中，要经常与主干保持同步。 个人开发可忽略

```bash
git fetch origin
git rebase origin/master
```

### 4. 合并分支commit

 分支开发完成后，很可能有一堆commit，但是合并到主干的时候，往往希望只有一个（或最多两三个）commit。 

```bash
git rebase -i origin/master
```

> - pick：正常选中
> - reword：选中，并且修改提交信息；
> - edit：选中，rebase时会暂停，允许你修改这个commit（参考[这里](https://schacon.github.io/gitbook/4_interactive_rebasing.html)）
> - squash：选中，会将当前commit与上一个commit合并
> - fixup：与squash相同，但不会保存当前commit的提交信息
> - exec：执行其他shell命令

### 5. 推送到远程仓库

```bash
git push --force origin myfeature # 合并commit后，就可以推送当前分支到远程仓库
```

 git push命令要加上force参数，因为rebase以后，分支历史改变了，跟远程分支不一定兼容，有可能要强行推送 

### 6. 发出pull request 

 提交到远程仓库以后，就可以发出 Pull Request 到master分支，然后请求别人进行代码review，确认可以合并到master。 

## 参考

- [udacity(优达学城)版本控制课程]( https://classroom.udacity.com/courses/ud123/lessons/437a88fc-15f5-48b8-a6a5-0cf3347e6183/concepts/fa8f761a-d0a2-4be1-a5b9-60116ea4ecd1 )

- [git使用规范-阮一峰博客]( http://www.ruanyifeng.com/blog/2015/08/git-use-process.html)

## 后记 

- 学习了git常用的命令
- 实现本地仓库和GitHub云端通信
- vscode编辑器很好用
- 尝试代码托管, 实践项目流程



