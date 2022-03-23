"""
 * Project name(项目名称)：Python_dir和help
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 21:38
 * Version(版本): 1.0
 * Description(描述)： Python dir() 函数用来列出某个类或者某个模块中的全部内容，包括变量、方法、函数和类等，它的用法为：
dir(obj)
obj 表示要查看的对象。obj 可以不写，此时 dir() 会列出当前范围内的变量、方法和定义的类型。

如果在没有参数的情况下调用，则返回当前范围内的名称。否则，返回一个按字母顺序排列的名称列表，
其中包括（部分）给定对象的属性，以及可从该对象访问的属性。如果对象提供了一个名为 __dir__ 的方法，它将被使用；否则使用默认的 dir() 逻辑并返回：
对于模块对象：模块的属性。对于一个类对象：它的属性，以及递归的属性的基地。
对于任何其他对象：它的属性、它的类的属性和
递归其类的基类的属性。
 """

if __name__ == '__main__':
    list1 = list[1, 2, 3]
    list2 = list(range(0, 20))
    # print(list1)
    print(dir())

    print(dir(str))
    print(dir(list2))
    print(dir(list))

    input()
