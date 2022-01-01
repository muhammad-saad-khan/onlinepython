#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Twinkle,twinkle, little star,");
print("\tHow i wonder what you are!");
print("\t\tUp above the world so high,");
print("\t\tLike a diamond in the sky.");
print("Twinkle,twinkle, little star,");
print("\tHow i wonder what you are!");


# In[4]:


from platform import python_version
print(python_version())


# In[5]:


from datetime import datetime
t=datetime.now();
print("The date and time is ",t);


# In[14]:


print("Enter radius of circle")
a=float(input());
x=2*3.14*a;
print("The area of circle is",x);


# In[27]:


print("Enter first name");
a=input()[::-1];
print("Enter last name");
b=input()[::-1];
print(b," " ,a);


# In[21]:


print("Enter first number");
a=float(input());
print("Enter second number");
b=float(input());
x=a+b;
print("The sum is",x);

