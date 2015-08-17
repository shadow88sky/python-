#Python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。用if语句可以构成分支结构。它根据给定的条件进行判断，以决定执行某个分支程序段。
#if (表达式) :  
#    语句1  
#else :  
#    语句2 
flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
   flag = True          # 条件成立时设置标志为真
   print 'welcome boss'    # 并输出欢迎信息
else:
   print name              # 条件不成立时输出变量名称


num = 5     
if num == 3:            # 判断num的值
    print 'boss'        
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # 值小于零时输出
    print 'error'
else:
    print 'roadman'     # 条件均不成立时输出


#Python 编程中 while 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。其基本形式为：
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
 
print "Good bye!"

#在 python 中，while … else 表示这样的意思，while 中的语句和普通的没有区别，else 中的语句会在循环正常执行完的情况下执行。其格式如下：
count = 0
while count < 5:
     print count, " is  less than 5"
     count = count + 1
else:
     print count, " is not less than 5"

#Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。for循环的第一种语法格式如下：
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print 'Current fruit :', fruit

#python不支持类似c的for(i=0;i<5;i++)这样的循环语句，但可以借助range函数模拟：
for x in range(0,5,1):  
    print x 

#break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。break语句用在while和for循环中。
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print 'Current Letter :', letter
 
var = 10                    # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      break
 
print "Good bye!"


#continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。continue语句用在while和for循环中。
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'Current Letter :', letter
 
var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print 'Current variable value :', var
print "Good bye!"