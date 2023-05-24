import matplotlib.pyplot as plt

def graph():

    # x = [2, 4, 5]

    x = list(input("Enter The Co-ordinates For The X-Axis :" ))

    # y = [2, 3, 6]

    y = list(input("Enter The Co-ordinates For The Y-Axis :" ))

    plt.plot(x, y, color='green', linestyle = "dashed" , linewidth = 3, marker = 'o', markerfacecolor = 'black', markersize = 10, label = 'Line 1')

    # plt.ylim(1,8)

    # plt.xlim(1,8)

    plt.xlabel('X Axis')

    plt.ylabel( 'Y Axis')

    plt.title('Graph')

    plt.show()
    

def Graph_Plotter():
    flag = True
    while flag:
        print(" ")
        print("----------Welcome To The Graph Plotter------------")
        print(" ")
        print(" ")
        print("-----Do You Want To Plot A Graph : ")
        user_input = input('''Enter Y To Plot
Enter E To Exit ''').lower()
        if user_input == 'y':
            graph()
        else:
            print("Exiting.........")
            break
            
Graph_Plotter()