# # Addition Chain

# In[3]:


class P():
    chain = []
    length = 0
    def __init__(self):
        self.chain.append(1)
        self.chain.append(2)
        self.length = 2
        
    def val(self):
        print("Lenght {}".format(self.length))


# # completeIndividual

# In[4]:


def f():
    return randint(1, 10)


# In[75]:



def completeIndividual(i, p, chain, e):
    r = 0
    while chain[p-1] <= e:
        if chain[p-1] == e:
            return chain
        if (f() <= 2):
            r = p - 1
        elif (f() > 2):
            r = p - 2
        else:
            r = randint(0, p-1)
        
        chain.append(chain[p-1] + chain[r])
        r = r - 1
        
        while chain[p] > e:
            chain[p] = chain[p-1] + chain[r]
            r = r-1
        p += 1
        Pops[i].length = Pops[i].length+1
    else:
        return chain
            


# In[80]:


Pops = []
Pops.append(P())
cad = []
Pops[0].chain.clear()
Pops[0].chain.append(1)
Pops[0].chain.append(2)
e = int(input("e > "))
cad = completeIndividual(0, 2, Pops[0].chain, e)
print(cad)


# In[ ]:




