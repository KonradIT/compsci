Days,TopPrice=0,0
while Days < 30:
    teams=0
    while teams < 2:
        TotalPrize,silverCoins,blackCoins,blackCoinLoss=0,0,0,0
        print("Team: " + str(teams+1) + " Day: " + str(Days))
        goldCoins=int(input("Gold Coins won: "))
        silverCoins=int(input("Silver Coins won: "))
        blackCoins=int(input("Black Coins won: "))
        TotalPrize=goldCoins * 50
        silverCoinPrize=silverCoins * 10
        blackCoinLoss=blackCoinLoss * 12
        TotalPrize=TotalPrize + silverCoinPrize - blackCoinLoss
        if TotalPrize > TopPrice:
            TopPrice=TotalPrize
        teams=teams + 1
        Days=Days + 1
print("The biggest prize of the year was: " + TopPrice)
