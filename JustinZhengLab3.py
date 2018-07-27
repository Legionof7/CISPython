from decimal import Decimal
def FileOpen():
    FileName = input('Enter your shopping list file:')
    try:
        TestOpen =  open(FileName)
    except IOError:
        print("This is not a shopping list!")
    InList = open(FileName)
    Output = open('justinzhenglab3out.txt', 'w')
    ShoppingList = InList.readlines()       
    total = 0
    float(total)    
    
    for line in ShoppingList:
        if ":" in line:
            item, price = line.split(":")
            Output.write('{:20}{:>20}'.format(item, price, '.2f'))
            total = (total + float(price))
            
            
        else:
            print ("No Colon")
            
        
        
    RoundedTotal = round(total,2)    
    Output.write('{:20}{:>20}'.format("Total:", str(RoundedTotal)))
    Output.close


for i in range(0,10):
    FileOpen()

##########################
#Run
#
#Enter your shopping list file:thisisnotafile
#This is not a shopping list!
#Enter your shopping list file:lab3.txt
#No Colon <-- I inserted this to make sure that it was reading the lines right
#No Colon
#Enter your shopping list file:
##########################
