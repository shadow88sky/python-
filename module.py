#简单地说，模块就是一个保存了Python代码的文件。模块能定义函数，类和变量。模块里也能包含可执行的代码。
#一个叫做aname的模块里的Python代码一般都能在一个叫aname.py的文件中找到。下例是个简单的模块support.py。
#想使用Python源文件，只需在另一个源文件里执行import语句，语法如下：
#import module1[, module2[,... moduleN]
import moduleTest
moduleTest.print_func("Zara")

#from…import
#Python的from语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：
#from modname import name1[, name2[, ... nameN]]
from moduleTest import print_func
print_func("Zara")

#把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
#from modname import *
#这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。

#当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。因此，如果你想重新执行模块里顶层部分的代码，可以用reload()函数。该函数会重新导入之前导入过的模块。语法如下：
#reload(module_name)
#在这里，module_name要直接放模块的名字，而不是一个字符串形式。比如想重载moduleTest模块，如下
reload(moduleTest)