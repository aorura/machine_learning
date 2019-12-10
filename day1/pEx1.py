#!/usr/bin/env python
# coding: utf-8

# In[1]:


a =10


# In[10]:


h='{:>10}'.format('kim')


# In[11]:


h


# In[13]:


dic={}
dic['python'] = 'www.python.org'
dic['apple']='www.apple.com'
dic['python']


# In[14]:


type(dic)


# In[15]:


dic


# In[17]:


dic.items()


# In[18]:


'www.python.org' in dic.values()


# In[20]:


print('input day :')
dow=input()
if dow == 'mon' :
    print('monday')
elif dow == 'tue':
    print('tuesday')
else:
    print("else")


# In[21]:


for k, v in dic.items():
    print("{0}:{1}".format(k,v))


# In[22]:


def print_personnel(name, position='staff', nationality='korea'):
    print('name = {0}'.format(name))
    print('position = {0}'.format(position))
    print('nationality={0}'.format(nationality))

print_personnel(nationality="japan", name="park")


# In[23]:


def add(*data):
    result=0
    for i in data:
        result += i
    return result

add(10,30)


# In[24]:


def pr_team(**players):
    for k in players.keys():
        print('{0} = {1}'.format(k, players[k]))


# In[25]:


pr_team(k1='v1', k2='v2')


# In[27]:


def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
d=[plus,minus]
d[0](1,3)
d[1](1,3)


# In[28]:


def hello_korean():
    print('안녕하세요')
def hello_english():
    print('hello')
    
def greet(hello):
    hello()
greet(hello_korean)


# In[29]:


greet(hello_english)


# In[38]:


class InstanceVar:
    #text_list=[]
    def __init__(self):
        self.text_list=[]
        print('init call')
        
    def add(self, text):
        self.text_list.append(text)
        
    def print_data(self):
        print(self.text_list)


# In[39]:


a=InstanceVar()


# In[40]:


a.add('one')


# In[41]:


a.print_data()


# In[42]:


b=InstanceVar()


# In[43]:


b.add('two')


# In[44]:


b.print_data()


# In[45]:


class HasPrivate:
    def __init__(self):
        self.name='kim'
        self.__weight=80
        
    def print_info(self):
        print('name', self.name)
        print('weight', self.__weight)
        
obj = HasPrivate()
obj.name


# In[47]:


obj.print_info()


# In[52]:


class A:
    def __init__(self):
        print("A.__init__()")
        self.message = 'Hello'
    def printA(self):
        print(self.message)
        
class B(A):
    def __init__(self):
        print("B.__init__()")
        
        super().__init__()
        print("self.message is " + self.message)
        self.message = "world"
        
if __name__ == "__main__":
    b = B()
    b.printA()


# In[53]:


class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration()
            
for i in MyRange(0, 5):
    print(i)


# In[56]:


def YourRange(start, end):
    current = start
    while current < end:
        yield current
        current += 1
    return

for i in YourRange(0, 5):
    print(i)


# In[57]:


a=(1,2,3)
b=(10,20,30)
c=(100,200,300)


# In[58]:


data3=[sum(x) for x in zip(a,b,c)]


# In[59]:


data3


# In[62]:


data4 = [x for x in zip(a,b,c)];


# In[63]:


data4


# In[64]:


sum((1,10,100))


# In[69]:


data5 = [x+y+z for x,y,z in zip(a,b,c)];


# In[70]:


data5


# In[84]:


class paySystem:
    def __init__(self):
        self.workedHours = 0
        self.hourlyPay=0
        self.weekPay=0
        self.__threshold=40
        
    def enterHoursAndPay(self):
        print("Enter Hours worked: ")
        self.workedHours = int(input())
        print("Enter Hourly Pay: ")
        self.hourlyPay = int(input())
        
    def calculateWeekPay(self):
        if (self.workedHours > self.__threshold):
            self.weekPay = self.__threshold * self.hourlyPay
            self.weekPay += (self.workedHours-self.__threshold) * self.hourlyPay * 1.5
        else:
            self.weekPay = self.workedHours * self.hourlyPay
    
    def printWeekPay(self):
            print("Week's pay: ${:>10}".format(self.weekPay))
            
if __name__ == "__main__":
    ps = paySystem()
    ps.enterHoursAndPay()
    ps.calculateWeekPay()
    ps.printWeekPay()


# In[94]:


class Purchase:
    def __init__(self):
        self.article = ''
        self.price = 0
        self.quantity = 0
    
    def setArticle(self, name):
        self.article = name
    
    def setPrice(self, price):
        self.price = price
        
    def setQuantity(self, quantity):
        self.quantity = quantity
        
class Cart:
    def __init__(self):
        self.itemsOfArticle = []
        
    def addArticle(self):
        item = Purchase()
        print("Enter description of article: ")
        item.setArticle(input())
        print("Enter price of article: ")
        item.setPrice(input())
        print("Enter quantity of article: ")
        item.setQuantity(input())
        self.itemsOfArticle.append(item)
        
    def printArticle(self):
        print("Article    Price    Quantity")
        for item in self.itemsOfArticle:
            print("{0}    {1}    {2}".format(item.article, item.price, item.quantity))

            
if __name__ == "__main__":
    cart = Cart()
    cart.addArticle()
    print("Do you want to enter more articles (Y/N)?")
    yOrN = input()
    while (yOrN == 'Y' or yOrN == 'y'):
        cart.addArticle()
        print("Do you want to enter more articles (Y/N)?")
        yOrN = input()    
        
    cart.printArticle()
    
    
        


# In[ ]:




