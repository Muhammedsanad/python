l=[1,2,3,4,5]
output=dict(map(lambda x:(x,x*2),l))
output={i:i*2 for i in l}
print(output)
###############################################################
l=[1,2,3,4,5]
output={i:i*2 for i in l}
print(output)
########################################################################################
customer=['Rahul','Antony','Salman','Arun','Kiran']
customer_startwith_A=[customer for customer in customer if customer.startswith('A')]
print(customer_startwith_A)
##########################################################################################
prices= [15,25,10,30,50]
prices_below_20=[price for price in prices if price<20]
print(prices_below_20)
####################################################################
employees={'Antony':55000,'Susan':45000,'Kiran':60000}
employees={name:'high'if salary>50000 else 'low' for name,salary in employees.items()}
print(employees)
###############################################################################
words={'Apple','Banana','Apple','Orange','Banana','Apple'}
count_word={word:word.count(word)for word in set(words)}
print(count_word) 




















