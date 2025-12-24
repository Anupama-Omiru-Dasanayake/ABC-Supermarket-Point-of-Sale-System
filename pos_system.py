# ---- New functions used-----
# .strip() - to ignore spaces
# .upper() - To capitalize all the english characters
# print(f'''{Variable Name} '''') - To print Variables inside a print function
# continue - this skips steps under that when the condition is true

# ------ Title -------
print('''
         ____________________________________________________________
        |                                                            |
        |                            A B C                           |
        |                    S U P E R   M A R K E T                 |
        |------------------------------------------------------------|''')
# -------- Variable Intialization --------
choice = 0
# ---------- data storage for id registration----------
customer = []
register = []
# ----------- data storage for order placemets----------
orders = []
order_details = []
# ------ There are more lists in the order placement section (Figure 02) (Temperary Storages)
# -------- Start processing --------
run = True
while run == True:
    print('''
         ____________________________________________________________
        |                                                            |
        |                     M a i n  M e n u                       |
        |------------------------------------------------------------|
        |            [1] Register a new customer                     |
        |            [2] Place an order                              |
        |            [3] View sales                                  |
        |            [4] Customer details                            |
        |            [5] Order details                               |
        |            [6] Exit                                        |
        |____________________________________________________________|
          ''')
    choice = input('''
                                           Enter your choice ➡ ''').strip()
# -------- Check user inputs --------
    while not choice.isdigit() or int(choice) < 1 or int(choice) > 6:
        print('''
            Error: Invalid input!. Please enter a number between 0 and 7''')
        choice = input('''
                                           Enter your choice ➡ ''').strip()
    # ------ choice 01 - Register a new customer ------
    if int(choice) == 1:
        print('''
         ____________________________________________________________
        |                                                            |
        |                  REGISTER A NEW CUSTOMER                   |
        |------------------------------------------------------------|
        ''')
        # -------- Get customer ID --------
        id = input('''
          Enter customer ID [Ex.(C001)]        ➡ ''').strip().upper()
        lenth = len(id)
        # -------- check if the ID is valid --------
        while lenth != 4 or id[0] != 'C' or not id[1:].isdigit() or id in register:
            # -------- check if the ID is valid --------
            while lenth != 4 or id[0] != 'C' or not id[1:].isdigit():
                print('''
             Error: Invalid ID!. Please enter a valid ID. Ex.(C001)''')
                id = input('''
          Enter customer ID                    ➡ ''').strip().upper()
                lenth = len(id)
            # -------- check if the ID is already registered --------
            while id in register:
                print('''
             Error: ID already registered. Please enter a new ID''')
                id = input('''
          Enter customer ID                    ➡ ''').strip().upper()
                lenth = len(id)

        # -------- if id is valid and not registered --------
        if len(id) == 4 and id[0] == 'C' and id[1:].isdigit() and id not in register:
            # -------- Get customer name --------
            name = input('''
          Enter customer Name                  ➡ ''')
            while len(name) > 20 or name.isspace() or name == '':
                if name.isspace() or name == '':
                    print('''
             Error: Invalid name!. Please enter a valid name.''')
                if len(name) > 20:
                    print('''
             Error: too long name. Please enter a name with less than 20 characters''')
                name = input('''
          Enter customer Name                  ➡ ''')
        # ---------- check all the above conditions are true before taking birthdate -----------
        if len(id) == 4 and id[0] == 'C' and id not in register and len(name) <= 20 and not name.isspace() and not name == '':
            # -------- birthdate --------
            birthdate = input('''
          Enter customer birthdate (DD/MM/YYYY)➡ ''')
            while len(birthdate) != 10 or not birthdate[2] == '/' or not birthdate[5] == '/' or not birthdate[:2].isdigit() or not birthdate[3:5].isdigit() or not birthdate[6:].isdigit():
                print('''
            Error: Invalid birthdate!. Please enter a valid birthdate (DD/MM/YYYY)''')
                birthdate = input('''
          Enter customer birthdate (DD/MM/YYYY)➡ ''')
            birth_year = int(birthdate[6:])
            # datetime.now().year - can be used for 2025 But I used 2025
            if not (birth_year <= (2025 - 18)):
                print('''
            Error: Customer must be 18 years or older''')
                continue  # using this function skip everything under this if this is True, and go back to the main menu
        if len(id) == 4 and id[0] == 'C' and id not in register and len(name) <= 20 and len(birthdate) == 10 and birthdate[2] == '/' and birthdate[5] == '/' and birthdate[:2].isdigit() and birthdate[3:5].isdigit() and birthdate[6:].isdigit() and (birth_year <= (2025 - 18)):
            # -------- Get customer contact number --------
            contact = input('''
          Enter customer contact number        ➡ ''')
            while not len(contact) == 10 or not contact.isdigit():
                print('''
            Error: Invalid contact number. Please enter a valid contact number''')
                contact = input('''
          Enter customer contact number        ➡ ''')
            # -------- Get customer address --------
        if len(id) == 4 and id[0] == 'C' and id not in register and len(name) <= 20 and len(birthdate) == 10 and birthdate[2] == '/' and birthdate[5] == '/' and birthdate[:2].isdigit() and birthdate[3:5].isdigit() and birthdate[6:].isdigit() and (birth_year <= (2025 - 18)) and len(contact) == 10 and contact.isdigit():
            address = input('''
          Enter customer address               ➡ ''')
            while len(address) > 50 or address.isspace() or address == '':
                if address.isspace() or address == '':
                    print('''
            Error: Invalid address. Please enter a valid address''')
                if len(address) > 50:
                    print('''
            Error: too long address. Please enter an address with less than 50 characters''')
                address = input('''
          Enter customer address               ➡ ''')
            if len(address) <= 50 and not address.isspace() and not address == '':
                save = input('''
          Save the customer details? (Yes/No): ''').strip().upper()
                # ----------- Check the user input (YES/NO)--------------
                if save == 'YES':
                    # -------- Add customer to the register --------
                    register.append(id)
                    # -------- Add customer to the customer list --------
                    customer.append(
                        [id, name, birthdate, contact, address])
                    print('''
        |------------------------------------------------------------|
        |                                                            |
        |              CUSTOMER SUCCESSFULLY REGISTERED              |
        |____________________________________________________________|
                                                                
                ''')
                elif save == 'NO':
                    print('''
        |------------------------------------------------------------|
        |                                                            |
        |                  CUSTOMER NOT REGISTERED                   |                                         
        |____________________________________________________________|
        ''')
                while save != 'YES' and save != 'NO':
                    print('''
            Error: Invalid input. Please enter Yes or No''')
                    save = input('''
          Save the customer details? (Yes/No): ''').strip().upper()
                    if save == 'YES':
                        # -------- Add customer to the register --------
                        register.append(id)
                        # -------- Add customer to the customer list --------
                        customer.append(
                            [id, name, birthdate, contact, address])
                        print('''
        |------------------------------------------------------------|
        |                                                            |
        |              CUSTOMER SUCCESSFULLY REGISTERED              |                                      
        |____________________________________________________________|
        ''')
                    elif save == 'NO':
                        print('''
        |------------------------------------------------------------|
        |                                                            |
        |                  CUSTOMER NOT REGISTERED                   |                                   
        |____________________________________________________________| 
        ''')

    # ------ choice 02 - Place an order ------
    if int(choice) == 2:
        print('''
         ____________________________________________________________
        |                                                            |
        |                       PLACE AN ORDER                       |
        |------------------------------------------------------------|
        ''')
        # --------- check if there are any customers registered ---------
        if len(register) == 0:
            print('''
            No customers registered. Please register a customer first''')
            continue  # if this is true skipp everything and go back to main menu
        # --------- if there are customers registered ---------
        if len(register) > 0:
            # -------- Get customer ID --------
            id = input('''
          Enter customer ID [Ex.(C001)]  ➡ ''').strip().upper()
            lenth = len(id)
        # -------- check if the ID is valid --------
            while lenth != 4 or id[0] != 'C' or not id[1:].isdigit() or id not in register:
                # -------- check if the ID is valid --------
                while lenth != 4 or id[0] != 'C' or not id[1:].isdigit():
                    print('''
            Error: Invalid ID. Please enter a valid ID [Ex.(C001)]''')
                    id = input('''
          Enter customer ID              ➡ ''').strip().upper()
                    lenth = len(id)
                # -------- check if the ID is already registered --------
                while id not in register:
                    print('''
            Error: ID is not registered. Please enter a registered ID''')
                    id = input('''
          Enter customer ID              ➡ ''').strip().upper()
                    lenth = len(id)
            cant_place = False
            for i in range(len(order_details)):
                if id == order_details[i][1]:
                    cant_place = True

            if cant_place == True:
                print('''
            Error: Maximum order limit reached !. 
                   Please contact the Developer.
                   Dveloper: anupama.20241811@iit.ac.lk''')
                continue  # if this true go back to main menu
            # -------- Get order ID --------
            if id in register and lenth == 4 and id[0] == 'C' and id[1:].isdigit() and cant_place == False:
                order_id = input('''
          Enter order ID [Ex.(OD01)]     ➡ ''').strip().upper()
                lenth = len(order_id)
            # -------- check if the order ID is valid --------
                while lenth != 4 or order_id[0:2] != 'OD' or not order_id[2:].isdigit() or order_id in orders:
                    # -------- check if the ID is valid --------
                    while lenth != 4 or order_id[0:2] != 'OD' or not order_id[2:].isdigit():
                        print('''
            Error: Invalid ID. Please enter a valid ID [Ex.(OD01)]''')
                        order_id = input('''
          Enter order ID                 ➡ ''').strip().upper()
                        lenth = len(order_id)
                # -------- check if the order ID is already registered --------
                    while order_id in orders:
                        print('''
            Error: ID is already registered. Please enter a another ID''')
                        order_id = input('''
          Enter order ID                 ➡ ''').strip().upper()
                        lenth = len(order_id)
            # -------- if id is valid and not registered --------
            if len(order_id) == 4 and order_id[0:2] == 'OD' and order_id[2:].isdigit() and order_id not in orders and cant_place == False:
                # ---------- print branch codes -----------
                print('''
        -------------------------------------------------------------
                        B R A N C H  -  C O R D S              
        -------------------------------------------------------------
                      ____________________________
                     |                            |
                     |    Colombo      -   B001   |
                     |    Nugegoda     -   B002   |
                     |    Piliyandala  -   B003   |
                     |    Gampaha      -   B004   |
                     |____________________________|
                     
        -------------------------------------------------------------
                  ''')
                # --------- Get branch code ---------
                branch = input('''
          Enter branch code              ➡ ''').strip().upper()
                while branch not in ['B001', 'B002', 'B003', 'B004']:
                    print('''
            Error: Invalid branch code. Please enter a valid branch code''')
                    branch = input('''
          Enter branch code              ➡ ''').strip().upper()
                # -------- Get order date --------
                order_date = input('''
          Enter order date (DD/MM/YYYY)  ➡ ''')
                while len(order_date) != 10 or not order_date[2] == '/' or not order_date[5] == '/' or not order_date[:2].isdigit() or not order_date[3:5].isdigit() or not order_date[6:].isdigit():
                    print('''
            Error: Invalid order date. Please enter a valid date (DD/MM/YYYY)''')
                    order_date = input('''
          Enter order date (DD/MM/YYYY)  ➡ ''')
                # --------- Temp Storage for store order details until user want to save---------
                items = []
                quantitys = []
                unit_prices = []
                totals = []
                # -------- Get item name --------
                item = input('''
          Enter item name                ➡ ''')
                while item.isspace() or item == '':
                    print('''
            Error: Invalid item name. Please enter a valid item name''')
                    item = input('''
          Enter item name                ➡ ''')
                items.append(item)
                # -------- Get quantity --------
                quantity = input('''
          Enter quantity                 ➡ ''')
                while not quantity.isdigit():
                    print('''
            Error: Invalid quantity. Please enter a valid quantity''')
                    quantity = input('''
          Enter quantity                 ➡ ''')
                quantitys.append(quantity)
                # -------- Get unit price --------
                unit_price = input('''
          Enter unit price               ➡ ''')
                while not unit_price.isdigit():
                    print('''
            Error: Invalid unit price. Please enter a valid unit price''')
                    unit_price = input('''
          Enter unit price               ➡ ''')
                if unit_price.isdigit() and quantity.isdigit():
                    # --------- convert unit price to float ---------
                    unit_prices.append(float(unit_price))
                    # -------- Get total price --------
                    total = int(quantity) * float(unit_price)
                    totals.append(total)
                # -------- add more items --------
                more = input('''
          Do you want to add more items? (Yes/No): ''').strip().upper()
                while more not in ['YES', 'NO']:
                    print('''
            Error: Invalid input. Please enter Yes or No''')
                    more = input('''
          Do you want to add more items? (Yes/No): ''').strip().upper()
                # --------- assign limit -----------
                limit = 1
                while more == 'YES' and limit < 3:
                    # -------- Get item name --------
                    item = input('''
          Enter item name                ➡ ''')
                    while item.isspace() or item == '':
                        print('''
            Error: Invalid item name. Please enter a valid item name''')
                        item = input('''
          Enter item name                ➡ ''')
                    items.append(item)
                    # -------- Get quantity --------
                    quantity = input('''
          Enter quantity                 ➡ ''')
                    while not quantity.isdigit():
                        print('''
            Error: Invalid quantity. Please enter a valid quantity''')
                        quantity = input('''
          Enter quantity                 ➡ ''')
                    quantitys.append(quantity)
                # -------- Get unit price --------
                    unit_price = input('''
          Enter unit price               ➡ ''')
                    while not unit_price.isdigit():
                        print('''
            Error: Invalid unit price. Please enter a valid unit price''')
                        unit_price = input('''
          Enter unit price               ➡ ''')
                    if unit_price.isdigit() and quantity.isdigit():
                        # --------- convert unit price to float ---------
                        unit_prices.append(float(unit_price))
                        # -------- Get total price --------
                        total = int(quantity) * float(unit_price)
                        totals.append(total)
                    # -------- add more items --------
                    if limit < 2:
                        more = input('''
          Do you want to add more items? (Yes/No): ''').strip().upper()
                    while more not in ['YES', 'NO']:
                        print('''
            Error: Invalid input. Please enter Yes or No''')
                        more = input('''
          Do you want to add more items? (Yes/No): ''').strip().upper()
                    limit += 1
                # ---------- check the limit -----------
                while more == 'YES' and limit == 3:
                    print('''
            Maximum limit reached !''')
                    more = 'NO'
                # ----- if user dont want to add more items --------
                if more == 'NO' or limit < 3:
                    # --------- Print the total ----------
                    total = 0.0
                    for i in totals:
                        total = total + float(i)
                    print(f'''
        |------------------------------------------------------------|              
        |    Branch: {branch}    Date: {order_date}                  
        |------------------------------------------------------------|
        |                                                            |
        |    TOTAL PRICE = Rs.{total:.2f}
        |____________________________________________________________|''')
                    save = input('''
          Do you want to save the order details? (Yes/No): ''').strip().upper()
                    while save not in ['YES', 'NO']:
                        print('''
            Error: Invalid input. Please enter Yes or No''')
                        save = input('''
          Do you want to save the order details? (Yes/No): ''').strip().upper()
                        if save in ['YES', 'NO']:
                            break
                    # -------- if the user inputs yes --------
                    if save == 'YES':
                        # -------- Add order to the order list --------
                        orders.append(order_id)
                        # -------- Add order to the order details --------
                        order_details.append(
                            [order_id, id, branch, order_date, items, quantitys, unit_prices, totals])
                        print('''
        |------------------------------------------------------------|
        |                                                            |
        |                 ORDER PLACED SUCCESSFULLY                  |
        |____________________________________________________________|
                          ''')
                    # -------- if the user inputs no --------
                    if save == 'NO':
                        print('''
        |------------------------------------------------------------|
        |                                                            |
        |                     ORDER NOT PLACED                       |
        |____________________________________________________________|
                          ''')

    # ------ choice 03 - View sales ------
    if int(choice) == 3:
        print('''
         ____________________________________________________________
        |                                                            |
        |                         VIEW SALES                         |
        |------------------------------------------------------------|
        ''')
        # --------- check if there are any sales if not redirect to main menu ---------
        if len(order_details) == 0:
            print('''
            No sales to display !''')
            continue  # if this is true go back to main menu
        # --------- if there are sales ---------
        else:
            print('''
        -------------------------------------------------------------
                        B R A N C H  -  C O R D S              
        -------------------------------------------------------------
                      ____________________________
                     |                            |
                     |    Colombo      -   B001   |
                     |    Nugegoda     -   B002   |
                     |    Piliyandala  -   B003   |
                     |    Gampaha      -   B004   |
                     |____________________________|
                     
        -------------------------------------------------------------
            ''')
            # ------------- Get branch code ---------
            branch = input('''
          Enter branch code                 ➡ ''').strip().upper()
            # --------- check if the branch code is valid ---------
            while branch not in ['B001', 'B002', 'B003', 'B004']:
                print('''
            Error: Invalid branch code. Please enter a valid branch code''')
                branch = input('''
          Enter branch code                 ➡ ''').strip().upper()
            # -------- Get date ---------
            work = True
            while work == True:
                date = input('''
          Enter date (DD/MM/YYYY)           ➡ ''').strip()
                # ----------- check if the date is valid --------
                while len(date) != 10 or not date[2] == '/' or not date[5] == '/' or not date[:2].isdigit() or not date[3:5].isdigit() or not date[6:].isdigit():
                    print('''
            Error: Invalid date. Please enter a valid date''')
                    date = input('''
          Enter date (DD/MM/YYYY)           ➡ ''').strip()
                # ---------- check if there are any sales on the given branch on the given date -----------
                total = 0
                # ----- create boolian variable to check if the order is found or not -----
                found = False
                # ------ check order details list for the given date and branch -----
                for order in order_details:
                    # ----- if the entered date and branch equal to order details list's date and branch -----
                    if date == order[3] and branch == order[2]:
                        # ----- assing found to True ------
                        found = True
                        # ----- if the entered date and branch is equal access the order details list's 8th item which is 7th index and storing Totals of every items -----
                        for item_total in order[7]:
                            # ----- go through the list and add the total of each item to the total -----
                            total += float(item_total)
                # ----- if the order is found print the total sales -----
                if found == True:
                    print(f'''
        |------------------------------------------------------------|
        |    Branch: {branch}    Date: {date}
        |------------------------------------------------------------|
        |                                                            |
        |    TOTAL SALES = Rs.{total:.2f}
        |____________________________________________________________|
                      ''')
                # ----- if the order is not found print 0 sales -----
                else:
                    print(f'''
        |------------------------------------------------------------|
        |    Branch: {branch}    Date: {date}
        |------------------------------------------------------------|
        |                                                            |
        |    TOTAL SALES = Rs.0.00
        |____________________________________________________________|
                      ''')

                another = input('''
          Do you want to view sales for another date? (Yes/No): ''').strip().upper()
            # --------- check if the user input is valid ---------
                while another not in ['YES', 'NO']:
                    print('''
            Error: Invalid input. Please enter Yes or No''')
                    another = input('''
          Do you want to view sales for another date? (Yes/No): ''').strip().upper()
                if another == 'YES':
                    work = True
                if another == 'NO':
                    work = False

    # ------ choice 04 - Customer details ------
    if int(choice) == 4:
        print('''
         ____________________________________________________________
        |                                                            |
        |                      CUSTOMER DETAILS                      |
        |------------------------------------------------------------|
        ''')
        # --- check if there are any customer details to display------------
        if len(customer) == 0:
            print('''
            No customers to display''')
            continue  # if this is true go back to main menu
        # ----- if there are customer details to display do other process everything work only if this is true------
        if len(customer) > 0:
            work = True
            while work == True:
                id = input('''
          Enter customer ID [Ex.(C001)]        ➡ ''').strip().upper()
                while id not in register:
                    print('''
            Error: ID is not registered. Please enter a registered ID [Ex.(C001)]''')
                    id = input('''
          Enter customer ID                    ➡ ''').strip().upper()
                if id in register:
                    index = 0
                    found = False
                    while index < len(customer):
                        if id == customer[index][0]:
                            found = True
                            print(f'''
        |------------------------------------------------------------|
        |                                                            |
        |     Customer ID :- {customer[index][0]}
        |     Name        :- {customer[index][1]}
        |     Birthdate   :- {customer[index][2]}
        |     Contact     :- {customer[index][3]}
        |     Address     :- {customer[index][4]}
        |____________________________________________________________|
                        ''')
                        index += 1
                    if not found:
                        print('''
            Error: Customer not found''')
                # --------- check if the user wants to view another customer details ---------
                if len(register) > 1:
                    another = input('''
          Do you want to view another customer details? (Yes/No): ''').strip().upper()
                    # --------- check if the user input is valid ---------
                    while another not in ['YES', 'NO']:
                        print('''
            Error: Invalid input. Please enter Yes or No''')
                        another = input('''
          Do you want to view another customer details? (Yes/No): ''').strip().upper()
                    if another == 'NO':
                        work = False
                    if another == 'YES':
                        work = True
                else:
                    work = False

    # ------ choice 05 - Order details ------
    if int(choice) == 5:
        print('''
         ____________________________________________________________
        |                                                            |
        |                       ORDER DETAILS                        |
        |------------------------------------------------------------|
        ''')
        if len(order_details) == 0:
            print('''
            Error: No orders to display''')
            continue  # if this is true go back to main menu
        if len(order_details) > 0:
            work = True
            while work == True:
                id = input('''
          Enter customer ID [Ex.(C001)]        ➡ ''').strip().upper()
                while id not in register:
                    print('''
            Error: ID is not registered. Please enter a registered ID [Ex.(C001)]''')
                    id = input('''
          Enter customer ID                    ➡ ''').strip().upper()
                if id in register:
                    index = 0
                    found = False
                    while index < len(order_details):
                        if id == order_details[index][1]:
                            found = True
                            # Find customer name
                            cust_name = ""
                            for cust in customer:
                                if cust[0] == id:
                                    cust_name = cust[1]
                                    break
                            print(f'''
        |------------------------------------------------------------|
        |     Customer ID  :- {id} | Name :- {cust_name}
        |------------------------------------------------------------|
        |                                                            |
        |     Order ID    :- {order_details[index][0]}
        |  
        |     Branch      :- {order_details[index][2]}
        |
        |     Order Date  :- {order_details[index][3]}
        |
        |------------------------------------------------------------|              
              Items       :-''')
                            # -------- loop till number of item in the order details every list's 5th list item which is 4th index (that is also a list)--------
                            for i in range(len(order_details[index][4])):
                                # ---------print the unit price of each item------
                                # -------- print the item names------
                                # -------- print the quantity of each item------
                                # -------- print the total of each item------
                                print(f'''
                {order_details[index][4][i]} = Rs.{order_details[index][6][i]:.2f}
                {order_details[index][4][i]}  x  {order_details[index][5][i]}  =  Rs.{float(order_details[index][7][i]):.2f} ''')
                            # -------- print the total of all items------
                            print(f'''
        |------------------------------------------------------------|
        |                                                            |
        |     TOTAL AMOUNT    =    Rs.{sum(float(i) for i in order_details[index][7]):.2f}
        |____________________________________________________________|
        ''')
                        index += 1
                    if not found:
                        print('''
            Error: No Orders placed by this customer''')
                    another = input('''
          Do you want to view another order details? (Yes/No): ''').strip().upper()
                    while another not in ['YES', 'NO']:
                        print('''
            Error: Invalid input. Please enter Yes or No''')
                        another = input('''
          Do you want to view another order details? (Yes/No): ''').strip().upper()
                    if another == 'YES':
                        work = True
                    if another == 'NO':
                        work = False

    # ------ choice 06 - Exit ------
    if int(choice) == 6:
        exit = input('''
          Are you sure you want to exit (Yes/No) ➡ ''').strip().upper()
        while exit not in ['YES', 'NO']:
            print('''
            Error: Invalid input. Please enter Yes or No''')
            exit = input('''
          Are you sure you want to exit (Yes/No) ➡ ''').strip().upper()
        if exit == 'YES':
            run = False
            print('''
        |------------------------------------------------------------|
        |                                                            |
        |                   THANK YOU ! FOR USING                    |
        |                      ABC SUPERMARKET                       |
        |____________________________________________________________|
        ''')
        if exit == 'NO':
            run = True
# ------ End of the program ------
#  _______________________________________________
# |                                               |
# |  Developed By :- ©Anupama Omiru               |
# |  Contact      :- anupama.20241811@iit.ac.lk   |
# |_______________________________________________|
