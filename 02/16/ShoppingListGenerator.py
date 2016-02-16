shoppingList = []
iscount="true"
while iscount=="true":
  item=input("Type Item: ")
  if item == "done":
    print(shoppingList)
    iscount = "false"
  else:
   shoppingList.append(item)

