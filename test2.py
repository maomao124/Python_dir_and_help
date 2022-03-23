"""
 * Project name(项目名称)：Python_dir和help
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 21:43
 * Version(版本): 1.0
 * Description(描述)：
 Python help() 函数用来查看某个函数或者模块的帮助文档，它的用法为：
help(obj)
obj 表示要查看的对象。obj 可以不写，此时 help() 会进入帮助子程序。

 """

if __name__ == '__main__':
    print(help(str.format))
    print(help(list.pop))
    print(help(list))

    print(help())
