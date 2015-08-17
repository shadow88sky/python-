#函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
#定义一个由自己想要功能的函数，以下是简单的规则：
#函数代码块以def关键词开头，后接函数标识符名称和圆括号()。
#任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
#函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
#函数内容以冒号起始，并且缩进。
#Return[expression]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回None。

#def functionname( parameters ):
#	"函数_文档字符串"
#   function_suite
#	return [expression]


#定义一个函数只给了函数一个名称，指定了函数里包含的参数，和代码块结构。这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从Python提示符执行。
# Function definition is here
def printme( str ):
   "打印任何传入的字符串"
   print str;
   return;
 
# Now you can call printme function
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");

#所有参数（自变量）在Python里都是按引用传递。如果你在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print "函数内取值: ", mylist
   return
 
# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print "函数外取值: ", mylist

#用lambda关键词能创建小型匿名函数。这种函数得名于省略了用def声明函数的标准步骤。
#Lambda函数能接收任何数量的参数但只能返回一个表达式的值，同时只能不能包含命令或多个表达式。
#匿名函数不能直接调用print，因为lambda需要一个表达式。
#lambda函数拥有自己的名字空间，且不能访问自有参数列表之外或全局名字空间里的参数。
#虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
#lambda函数的语法格式如下：
#lambda [arg1 [,arg2,.....argn]]:expression
sum = lambda arg1, arg2: arg1 + arg2;
 
#调用sum函数
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )
