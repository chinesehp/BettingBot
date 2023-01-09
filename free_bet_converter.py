odd_a =5
odd_b =1.2
free_bet =100
hedge = free_bet*(odd_a-1)/odd_b

profit = hedge*(odd_b-1)
margin = profit/free_bet *100
print("Hedge: $",round(hedge,2))
print("Profit: $",round(profit,2))
print("Margin: ",round(margin,2),"%")
