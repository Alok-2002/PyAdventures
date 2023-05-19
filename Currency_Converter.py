def Currency_Converter():
    print("-----Welcome To The Currency Converter-----")
    print(" ")
    dollars = eval(input("Enter The Amount In Dollars: "))
    print(" ")
    rupees = convert_to_Rupees(dollars)
    print(dollars,"Dollars is Equal To",rupees,"Rupees")
    
convert_to_Rupees = lambda dollars: dollars * 81.94  

Currency_Converter()