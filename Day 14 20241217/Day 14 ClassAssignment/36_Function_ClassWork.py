def forProfit(cp,sp):
    profit=sp-cp
    subsidy=(cp*5)/100
    grossProfit=profit+subsidy
    print("You gained a profit  = ",profit)
    print("Your subsidy = ",subsidy)
    print("Your gross profit(profit+subsidy)= ",grossProfit)
def forLoss(cp,sp):
    loss = cp-sp
    subsidy = (cp*20)/100
    if loss>subsidy:
        grossLoss=loss-subsidy
        print("You suffered a loss = ",loss)
        print("Your subsidy = ",subsidy)
        print("Your gross loss(loss-subsidy)= ",grossLoss)
        return loss, grossLoss
    else:
        grossProfit=subsidy-loss
        print("You suffered a loss = ",loss)
        print("Your subsidy = ",subsidy)
        print("Your gross profit(subsidy-loss)= ",grossProfit)
        return loss, grossProfit



costPrice=float(input("Enter the cost price of the commodity= "))
sellingPrice=float(input("Enter the selling price of the commodity= "))

if costPrice<sellingPrice:
    result=forProfit(costPrice,sellingPrice)
else:
    result=forLoss(costPrice,sellingPrice)