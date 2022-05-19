'''
Functions

a set of code 
a block of code
'''
#1000 lines

# def Sujith(a,b,c='kiran'):# function definatioon
#     print('this is function',a,b,c)
#     #function body 
# Sujith(1,5,'aravind')#function call
# Sujith(2,5,'siva')
# Sujith(1,5)


#arbitrary
# def hemanth(*a):
#     print(a)
# hemanth(1,2,3,4,5,6,7,8)

# #kwarg
# def kumari(**ramu):
#     print(ramu)
# kumari(sno=1,name='teja')
# kumari(sno=2,name='Kumari')


#nested function

# def narayana():
#     print('this is func')
#     def python():
#         print('this is inner func')
#     python()
# narayana()


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

'''
lambda
'''
# sanjay=lambda a : a/a
# print(sanjay(2))

'''
filter
filter(fun,sequence(list,tuple,set))
'''
# sai=[1,2,3,34,4,5,6,7,87,8,9,0,0,22,2,34,4,4,54,5]
# def san(i):
#     if i%2==0:
#         print(i)
# for i in sai:
#     san(i)
# pavan=filter(san,sai)
# print(list(pavan))