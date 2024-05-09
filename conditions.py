print('Welcome to Tucs!')
order_name = input('What would you like to order today?')

if len(order_name) == 0:
    print('You need to add something to your cart :)')
elif (len(order_name) > 18):
    print('Sorry, we cant process orders that long')
elif (order_name == 'empanadas'): 
    print('Great!We love empanadas too')
    order_amount = input('How many would you like?') 
    if (int(order_amount) >= 1):
        print('Your ' + order_amount + ' ' + order_name + ' will be ready soon.') 
    else:
        print('Oh, I will cancel the order then.')
else:
    order_amount = input('How many would you like?')  
    if (int(order_amount) == 0):
        print('Oh, I will cancel the order then')
    else:
        print('Your ' + order_amount + ' ' + order_name + ' will be ready soon.') 
        
         