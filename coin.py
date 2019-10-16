#Sean McConkey
#Script to find fewest amount for any value of coins 
# 10/10/2019
#

#Create a function that takes in an argument of a dollar figure in cents. For example, $1.25 would be 125.

#The function should return the least number of coins to come up with that dollar figure. The denominations are a 25 cent coin,  a 10 cent coin, a  5 cent coin, and a 1 cent coin.

#For an input of 125, the result should be 5.
#For an input of 98, the result should be 8.
#For an input less than 1, the result should be 0.

coins=[25,10,5,1] #coins being used
def count(amt,coincount): 
    amt!=0 
    while True:#while amount is not 0 continue
        for coin in coins:
           coincount=coincount +(amt//coin) #adding number of coins being used
           amt=amt%coin #reducing remaining amount
            
        return coincount


       
     

print(count(125,0))
      