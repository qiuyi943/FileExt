#FileEXT 文件树型结构拷贝工具


#1、概述

其实在为这篇博文起标题的时候有点纠结，不知当前的标题能否明确概括本文介绍的这个工具的功能。也许结合以下场景的描述能够帮助大家了解这个工具到底是干什么用的。

假设有一个文件夹“1”，其树型结构如下所示
```
1
├── 2
│   └── 3
│       ├── 4
│       │   └── D.txt
│       ├── A.txt
│       ├── B.txt
│       └── C.txt
├── 5
│   ├── 6
│   │   ├── 7
│   │   │   └── F.txt
│   │   └── G.txt
│   └── E.txt
├── 8
│   └── H.txt
└── I.txt
```
此时， 有一个file.list文件里面记录了想要拷贝的文件（可以是相对路径或者绝对路径）
```
./2/3/A.txt
./8/H.txt
./I.txt
./5/6/G.txt
```
然后使用本文介绍的工具能够基于源文件夹“1”的树形结构，并按照file.list的内容，创建一个新的树型文件夹“1_[datatime]”，其结构如下所示

```
1_20160830014128/
├── 2
│   └── 3
│       └── A.txt
├── 5
│   └── 6
│       └── G.txt
├── 8
│   └── H.txt
└── I.txt
```

****

#2、使用场景
该工具用于将你感兴趣的文件从一个复杂的树型结构路径中摘取出来，并通过创建另外一个完备的树型结构路径来保存这些文件。例如，Android 的一个模块中可能会编译出多个JNI库文件、bin文件以及app文件（可能不常见，但博主现在维护的模块却是如此）；如果每次对该模块进行整编，就会在多个路径中生成多个文件，当对外分发时需要创建一个跟源路径相同的文件树型结构，然后再将各个文件从源路径中拷贝出来，费时费力，还容易出错。

****
#3、系统兼容
该工具基于Python3开发，在win10以及ubuntu 16.04 LTS测试均可使用，前提当然是系统要已经安装Pyhton3；由于使用了tkinter这个库，所以在ubuntu下使用时，需要安装python3-tk
```
sudo apt-get install python3-tk
```
****
#4、功能扩展
如果file.list中的路径表示的是一个文件夹，那么这个文件夹中的所有内容都会被拷贝。例如，file.list的内容如下

```
/media/sf_share/FileExt/1/2/3
```
此时被创建出来的文件树型结构则是

```
1_20160830020434
└── 2
    └── 3
        ├── 4
        │   └── D.txt
        ├── A.txt
        ├── B.txt
        └── C.txt
```
如果想要拷贝出当前路径中的所有名为“D.txt”的文件，那么file.list可以这么写

```
**/D.txt
```
此时被创建出来的文件树型结构如下

```
1_20160830020711
└── 2
    └── 3
        └── 4
            └── D.txt
```

#5、工具使用
工具的使用非常简单，进入命令行终端输入以下命令，便会弹出对话框分别选择源文件夹和file.list（任意文件名）
```
python3 FileExt.py
```

 选择文件夹
![选择文件夹](http://upload-images.jianshu.io/upload_images/2712913-f0f172ebc7e149fb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

选择file.list文件
![选择file.list文件](http://upload-images.jianshu.io/upload_images/2712913-51cd2fca72aab563.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

选择完文件夹file.list文件之后，如果文件存在便会在console窗中输出类似以下内容
```
./2/3/A.txt --> /media/sf_share/FileExt/1_20160831003900/./2/3/A.txt
./8/H.txt --> /media/sf_share/FileExt/1_20160831003900/./8/H.txt
./I.txt --> /media/sf_share/FileExt/1_20160831003900/./I.txt
./5/6/G.txt --> /media/sf_share/FileExt/1_20160831003900/./5/6/G.txt
```
