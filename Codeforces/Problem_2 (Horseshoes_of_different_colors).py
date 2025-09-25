'''

Valera the Horse is going to the party with friends. He has been following the fashion trends for a while, and he knows
that it is very popular to wear all horseshoes of different color. Valera has got four horseshoes left from the last year,
but maybe some of them have the same color. In this case he needs to go to the store and buy some few more horseshoes,
not to lose face in front of his stylish comrades.

Fortunately, the store sells horseshoes of all colors under the sun and Valera has enough money to buy any four of them.
However, in order to save the money, he would like to spend as little money as possible, so you need to help Valera and
determine what is the minimum number of horseshoes he needs to buy to wear four horseshoes of different colors to a party.

Input
The first line contains four space-separated integers the colors of horseshoes Valera has.

Consider all possible colors indexed with integers.

Output
Print a single integer — the minimum number of horseshoes Valera needs to buy.

'''

# Input Data list
numbers = map(int, input().split())
# Remove Dublicate Data
num = set(numbers)
# Count List Number
count = len(num)
# Shoe Buy Number
shoes_buy = 4 - count
print(shoes_buy)