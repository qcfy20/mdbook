# virtualBox 安装 Ubuntu1604

## 准备

- win10 64-bit系统环境
- virtualBox 安装程序
- Ubuntu1604 .iso文件

## 开始

### 创建虚拟电脑

1. 全局设定->常规, 修改: 默认虚拟电脑位置
2. 新建, 修改: 名称<自定义>;类型<Linux>;版本<Ubuntu(64-bit)>
3. 内存大小: 2048MB
4. 现在创建硬盘->虚拟硬盘文件类型VDI
5. 存储类型->固定分配(适合存储空间充足,追求使用速度)->大小: 48GB
6. 点击创建(至此相当于有了一台虚拟电脑, 但是没有任何系统)

### 安装Ubuntu1604

1. 选择创建好的电脑->设置->系统, 调整启动顺序: 光驱位于顶端
2. 存储, 修改: 控制器IDE添加下载好的iso系统盘片
3. 保存设置,启动虚拟电脑
4. 以下和空盘中正常安装Ubuntu系统一致(直接选择清除系统安装)
5. 安装完成,关机重启

### 修改virtualBox窗口栏

1. 设备->安装增强功能, 弹出窗口点击运行, 安装完成后重启虚拟电脑
2. 视图->自动调整显示尺寸(最大化窗口运行不要全屏运行)
3. 设备->粘贴,拖放,都选择双向
4. 仅保留控制,视图,设备选项

### 修改虚拟电脑配置

