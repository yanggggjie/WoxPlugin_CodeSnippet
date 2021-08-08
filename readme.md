# CodeSnippet
## 介绍

使用代码片段能够大大提高编程效率，几乎每个IDE都有建立自己代码片段的功能，比如vscode、pycharm等等。

但像jupyter notebook，Google colab等在线IDE，就没有代码片段的功能，或者说使用起来并不方便。

CodeSnippet为wox带来了代码片段的功能，wox可以全局使用，因此你可以在任何地方打开wox复制自己的代码片段，然后粘贴到任何地方。

## 配置方法

1.需要在wox设置中指定Python路径（含有python.exe的文件夹的路径）

2.该Python环境要安装有pywin32这个库，安装方法 pip install pywin32

3.将整个CodeSnippet文件夹复制到C:\Users\USER_NAME\AppData\Local\Wox\app-1.4.1196\Plugins下

4.重启wox

## 使用

打开wox，然后输入cp(默认触发关键字,可以随意更改)+空格+关键字（例如:cp map），在出现的选项中按鼠标点选，或者回车键即可将代码片段复制到粘贴板。然后使用ctrl + v在任何地方粘贴。

## 注意事项

1.如何自定义你的代码片段？

你需要打开CodeSnippet的文件夹（一般是C:\Users\USER_NAME\AppData\Local\Wox\app-1.4.1196\Plugins\CodeSnippet）找到data.json文件，然后仿照给定的例子输入你自己的代码片段，更改代码片段后请重启wox。

2.定义代码片段的格式？

和vscode的用户代码片段格式一模一样，请自行搜索。

2.匹配算法原理

当你输入的关键词是代码片段中prefix属性字符串的子串时，我们就认为匹配成功，然后加入wox显示供你选择列表。










