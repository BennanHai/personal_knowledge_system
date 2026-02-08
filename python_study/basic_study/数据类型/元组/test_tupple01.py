# @Author: Benanahai
# @Time  : 2025/3/22 16:37 
# @Desc  :

tup1 = ('baidu', 'google',1,2)

print (tup1)
del tup1;
print ("删除后的元组 tup : ")
print (tup1)

# 报错信息如下，证明整个元组已经被删除
# 删除后的元组 tup1 :
# Traceback (most recent call last):
#   File "tupple.py", line 29, in <module>
#     print(tup1)
# NameError: name 'tup1' is not defined