def knapsack(weights,cost,capacity):
  num_items=len(weights)
  table=[[0]*(capacity+1) for __ in range(num_items+1)]

  for i in range(1,num_items+1):
    for j in range(1,capacity+1):
      if weights[i-1]<=j:
        table[i][j]=max(cost[i-1]+table[i-1][j-weights[i-1]],table[i-1][j])
      else:
        table[i][j]=table[i-1][j]

  selected_items=[]
  remaining_capacity=capacity
  for i in range(num_items,0,-1):
    if table[i][remaining_capacity]!=table[i-1][remaining_capacity]:
      selected_items.append(i-1)
      remaining_capacity-=weights[i-1]

  selected_items.reverse()
  return table[num_items][capacity],selected_items

weights=[int(x) for x in input("Enter the weights of the coffee beans seperated by spaces:").split()]
cost=[int(x) for x in input("Enter the costs of the coffee beans seperated by spaces:").split()]
capacity=int(input("Capacity:"))

max_profit,selected_items=knapsack(weights,cost,capacity)

print("Max profiit:",max_profit)
print("Selected items (index)",selected_items)
print("Selected items weight",[weights[i] for i in selected_items])
print("Selected items costs:",[cost[i] for i in selected_items])
