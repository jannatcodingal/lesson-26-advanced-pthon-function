list1={1,2,3}
list2={'a','b','c'}
s3=list(zip(list1,list2))
print(s3,"\n")
a=['a','b','c','d','e']
b=[1,2,3,4,5]
for a, b in zip(a,b[::1]):
    print(a,b)
stocks=['shoes','clothes','jewellery']
prices=[1000,2000,3000]
new_dict={stocks:prices for stocks, prices in zip(stocks,prices)}
print('\n{}'.format(new_dict))