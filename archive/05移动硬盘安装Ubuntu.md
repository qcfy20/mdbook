## 移动硬盘安装Ubuntu1604

### 准备

- ubuntu镜像文件：ubuntu系统文件（官网下载：https://ubuntu.com/download/desktop）

- UltraISO软件：把ubuntu系统刻入U盘制作启动盘（官网下载：https://cn.ultraiso.net/xiazai.html 试用版即可）

- DiskGenius软件：硬盘分区软件（官网下载：http://www.diskgenius.cn/download.php）

> 个人参考：
>
> - Acer笔记本win10固态硬盘480G分区表类型GPT启动类型仅UEFI(分区类型用DiskGenius软件可以看)
> - 移动硬盘500G（其实是机械硬盘+硬盘盒）
> - U盘32G

**注意:** 以下教程仅针对移动硬盘安装; BIOS设置启动类型为仅UEFI

### 开始

1. **把ubuntu系统刻入U盘制作启动盘**

   会格式化U盘请备份好数据;启动盘后续还可能用到建议长期留存

2. **使用分区软件对移动硬盘分区**

   先在win系统下对硬盘进行分区，到了安装ubuntu系统过程中手动分区那一步直接选择就行了（如果不事先在win系统分区，可能出现很多教程中说的“分区4k对齐”问题）(Ubuntu安装时分区大小会发生细微变化,不要在意)

   | 分区名 | 文件系统类型                                       | 分区大小 |
   | ------ | -------------------------------------------------- | -------- |
   | efi    | FAT32，用于将Ubuntu系统启动引导放在此分区          | 1~2G     |
   | swap   | Linux swap partition，交换分区，一般为电脑内存大小 | 8G~16G   |
   | /      | EXT4，用于挂载 `/`作为Linux的根目录                | >20G     |
   | /home  | EXT4，用于挂载`/home`作为Linux主文件目录           | >80G     |

> 个人参考:
>
> efi-2G | swap-8G | /-100G| /home-150G

3. **进行ubuntu系统安装**

   重启进入bios(一般F2进入bios)

   - [ ] 确认Boot类型仅UEFI;USB-Boot启动类型仅UEFI
   - [ ] 关闭 **Secure Boot**（大多数教程都这么写的,要求关闭）
   - [ ] 调整boot option启动顺序, USB启动盘放在首位
   - [ ] F10保存设置并重启

   进入Ubuntu安装界面, 根据引导到安装类型界面->选择其他选项->开始手动分区

   - [ ] 根据分区大小确认Ubuntu系统安装盘
   - [ ] 按照文件类型分区(efi分区一定要选efi系统分区如果没有选择保留bios区域;千万别选/boot后面没办法修复引导)
   - [ ] 安装完成

4. 修复引导

   安装完重启F12进入boot Menu发现看不到移动硬盘, 别急这是因为efi分区并没有系统引导,需要自己修复

   插上U盘启动器选择试用Ubuntu(不要再重新安装一遍了)

   进入试用桌面, 打开终端安装boot-repair工具

   ```
   sudo apt-add-repository ppa:yannubuntu/boot-repair
   sudo apt update
   sudo apt install boot-repair
   ```

   安装完成后，执行 boot-repair 即可启动软件，然后选择 “Recommended repair” 等待引导修复完成。
   修复完成之后，在ESP分区会出现一个名为 EFI 的目录，里面有 BOOT 和 ubuntu 两个子目录，用来启动 Ubuntu 系统的引导文件就是位于 ubuntu 目录中的 shimx64.efi 文件 。

5. **bios设置(主要针对Acer笔记本了)**

   - [ ] 先打开**Secure Boot** 选项,不然下一个选项可能是灰色不可选状态;
   - [ ] **Security** 选项卡中选择 **Select an UEFI file as trusted for executing:**在目标设备上（移动硬盘的ESP分区）选择 `/EFI/ubuntu/shimx64.efi` ，输入引导项的<自定义名称>，回车即可；
   - [ ] 再次关闭 **Secure Boot**(大多数教程都是这么要求的)
   - [ ] 保存并重启再次进入BIOS,调整启动顺序EFI : <自定义名称>放在Windows启动项前边(这样插上移动硬盘启动就会直接进入Linux系统)

### 参考

- [移动硬盘安装Ubuntu系统（UEFI引导）的一些记录](https://blog.csdn.net/u012939909/article/details/80753115)
- [Acer 笔记本双硬盘安装Ubuntu18.04](https://blog.csdn.net/Lsm868/article/details/104801818)
- [记一次艰难的 Ubuntu 双系统安装过程及问题的解决](https://houkaifa.com/2018/12/08/ubuntuInstall/)

### 后续

  终于通过移动硬盘台实现式机和笔记本都可以启动Linux系统, 算是第一次正式使用Ubuntu,当然双系统必然会遇到一些问题, 比如双系统切换导致windows时间不准确(可能造成无法科学上网), Ubuntu桌面分辨率无法调整, 安装搜狗输入法; anaconda; v2rayL客户端问题, 期待后面的文章解决这些问题.