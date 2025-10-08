#list类型，一种可以改变元素的列表
L = [
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Bob']
]

#打印Apple
print(L[0][0])
#打印python
print(L[1][1])
#打印Bob
print(L[2][2])

G = ['Hyacine','Hysilens','Cerydra']
print(G)
print(G[1])
#增加元素到列表尾部
G.append('Tribble')
print(G)
#增加元素到指定位置
G.insert(1,'Castorice')
print(G)
#删除指定元素
G.pop(-1)
print(G)
#变更元素可以靠赋值
G[1] = 'Danheng'
print(G)

#tuple类型，不能修改的列表
t = (1,2)
p = (1,)    #定义一维tuple时要加上“，”防止歧义