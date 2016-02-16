shoppingList = []
iscount="true"
while iscount=="true":
  print("Type done to get the shopping list")
  item=input("Type Item: ")
  if item == "done":
    print(shoppingList)
    iscount = "false"
  else:
   shoppingList.append(item)

