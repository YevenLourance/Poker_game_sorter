#!/usr/bin/env python
# coding: utf-8

# In[122]:


import sys


# In[106]:


from collections import defaultdict
Character2number = {"T":10,"J":11,"Q":12,"K":13,"A":14} # convert string to int values
for i in range(2,11):
    Character2number[str(i)]=i


# In[108]:


def if_flush(suits):
    return len(set(suits))==1


# In[109]:


def if_straight(values):
    for i in range(4):
        if values[i] != values[i+1]-1:
            return False
    return True


# In[110]:


def kind(values): # return the counts of different values card and a list of ranked values.
    unique = defaultdict(int) # dictionary with dafault values 0
    for i in values:
        unique[i] = unique[i]+1

    ranked_value = [] # a list of values orderd by the counts. If counts tie then orderd by value.
    
    counts = sorted(list(set(unique.values())),reverse=True) # the counts of values in descending order.

    keys = sorted(list(unique.keys()),reverse=True)

    for n in counts:
        for i in keys:
            if unique[i]==n:
                ranked_value.append(i) # firstly insert the most frequent value, then insert the higher value.
    
    return list(unique.values()),ranked_value
    


# In[111]:


def hand2rank(hand):
    # input a hand, return a tuple (rank, ranked values)
    values = []
    suits = []

    for card in hand.split():
        values.append(Character2number[card[:-1]]) # obtain the value of each card
        suits.append(card[1]) # obtain the suit of each card
    values.sort() # sort the values

    flush = if_flush(suits)
    straight = if_straight(values)

    if flush and straight: # check if Royal or Straight flush
        return (9,values[-1]) # return 9 rank and highest value. 0 is a placeholder
    else:
        kinds,ranked_value = kind(values)

        if 4 in kinds: # Four of a kind
            return (8,ranked_value)
        elif 3 in kinds and 2 in kinds: #Full house
            return (7,ranked_value)
        elif flush: #Flush
            return (6,reversed(values))
        elif straight:
            return (5,values[-1])
        elif 3 in kinds: # Three of a kind
            return (4,ranked_value)
        elif kinds.count(2) == 2: #two paris
            return (3,ranked_value)
        elif 2 in kinds: # pair 
            return (2,ranked_value)
        else:
            return (1,ranked_value)


# In[124]:


first_won = 0
second_won = 0
for line in sys.stdin:
    cards = line.split()
    first_hand = " ".join(cards[:5])
    second_hand = " ".join(cards[5:])
    
    first_rank = hand2rank(first_hand)
    second_rank = hand2rank(second_hand)
    
    if first_rank > second_rank:
        first_won +=1
    elif first_rank < second_rank:
        second_won +=1
print("Player 1: "+str(first_won))
print("Player 2: "+str(second_won))


# In[ ]:




