
# coding: utf-8

# In[95]:


def sum(s):
    sum = 0
    for i, c in enumerate(s):
        next = i+1 if i+1 < len(s) else 0
        if c == s[next]:
            sum += int(c)
    return sum


# In[96]:


assert sum('1122') == 3
assert sum('1111') == 4
assert sum('11111') == 5
assert sum('1234') == 0
assert sum('91212129') == 9


# In[97]:


with open("input.txt") as f:
    for line in f:
        input = line

sum(input)


# In[98]:


def sum2(s):
    sum = 0
    step = int(len(s)/2)
    for i, c in enumerate(s):
        if i+step < len(s):
            next = i+step 
        else:
            next = step - (len(s) - i)
        if c == s[next]:
            sum += int(c)
    return sum


# In[99]:


assert sum2('1212') == 6
assert sum2('1221') == 0
assert sum2('123425') == 4
assert sum2('123123') == 12
assert sum2('12131415') == 4


# In[100]:


sum2(input)

