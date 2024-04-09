class Category:

    #constructor 
    def __init__(self, Category, food=" ", clothing=" ", auto=" ", entertainment=" "):
        self.element_category = Category
        self.food = food
        self.clothing = clothing
        self.auto = auto
        self.entertainment = entertainment
        self.ledger = []


    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def check_funds (self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

    def withdraw (self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer (self, amount, Category):
        if self.check_funds(amount):
            self.withdraw(amount, description="Transfer to " + str(Category.element_category))
            Category.deposit(amount, description="Transfer from " + str(self.element_category))
            return True
        else:
            return False 

    #Method that converts budget object to string
    def __str__(self):
        #initial value for the object printout
        ledger_out=""

        #Print title Category (Food)
        ledger_out += '*' * int((30 - len(self.element_category)) / 2) + self.element_category + '*' * int((30 - len(self.element_category)) / 2)

        #loop to iterate ledger
        for item in self.ledger:
            #key/description extraction
            if (len(item["description"]) > 23):
                ledger_out += "\n" + item["description"] [0:23]
            else:
                ledger_out += "\n" + item["description"] + " " * (23 - len(item["description"]))
            
            #value extraction
            ledger_out += " " * (7-len("{:.2f}".format(item["amount"]))) + "{:.2f}".format(item["amount"])
        #return Total
        total = str(self.get_balance())
        ledger_out += "\nTotal: " + total

        return ledger_out
    
    def get_withdrawls(self):
        withdraw = 0
        for item in self.ledger:
            if item["amount"] < 0:
                withdraw += item["amount"]
                posi_withdraw = abs(withdraw)
                return posi_withdraw
        else:
            return None
    


def create_spend_chart(categories): 
    title = "Percentage spent by category"
    horiz_bar = "-" * 10
    horiz_bar = horiz_bar.rjust(14)
    category_name = []
    vertical_categories = []

    #Calculate total withdrawals
    withdraw_total = 0
    for category in categories:
        for item in category.ledger:
            if item["amount"] < 0:
                a += item["amount"]
                positive_total = abs(withdraw_total)
    
    #loop to grab category name
    for i in categories:
        category_name.append(i.element_category)

    #produce the categories vertically
    for cat in category_name:
        vertical_category = ''
        for i in cat:
            vertical_category += i + '\n'
        vertical_categories.append(vertical_category)


    #Get max number of lines/rows
    max_lines = 0
    for vertical_category in vertical_categories:
        num_lines = vertical_category.count('\n')
        if num_lines > max_lines:
            max_lines = num_lines

    #print categories side-by-side
    output = ""
    for i in range(max_lines):
        output += ' ' * 5
        for vertical_category in vertical_categories:
            lines = vertical_category.split('\n')
            if i < len(lines) - 1:
                output += lines[i] + '  '
            else:
                output += '   '
        output += '\n'

    c1_percent = (categories[0].get_withdrawls() / positive_total) * 100
    c1_percent = int(f'{c1_percent:.0f}')
    c2_percent = (categories[1].get_withdrawls() / positive_total) * 100
    c2_percent = int(f'{c2_percent:.0f}')
    c3_percent = (categories[2].get_withdrawls() / positive_total) * 100
    c3_percent = int(f'{c3_percent:.0f}')

    #print o's
    percentage_col = ""
    
    #print (chart_print)
    for k in range(100, -10, -10):
        percentage = f"{k:3}|"
        if c1_percent >= k:
            if c1_percent >= k and c1_percent > k - 10:
                percentage += " o"

        else:
            percentage += "  "

        if c2_percent >= k and c2_percent > k - 10:
            percentage += "  o"

        else:
            percentage += "   "

        if c3_percent >= k and c3_percent > k - 10:
            percentage += "  o"

        else:
            percentage += "  "

        percentage_col += "\n" + percentage
        #print(percentage_col)
        

    
    return(title + percentage_col + "\n" + horiz_bar + "\n" + output)


# Define categories
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(600, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
clothing.deposit(1000, "deposit")
clothing.withdraw(200, "jacket")
# clothing.withdraw(100, "pants")

auto = Category("Auto")
auto.deposit(1000, "deposit")
auto.withdraw(100, "new tires")
# auto.withdraw(250, "new brakes")

toy = Category("Toy")
toy.deposit(200, "deposit")
toy.withdraw(80, "new toy")

# Create a list of categories
categories = [food, clothing, auto]

# Generate and print the spend chart
chart = create_spend_chart(categories)

print(chart)

#  chart_lines = []
#     chart_lines.append("Percentage spent by category")
#     for i in range(100, -10, 0):
#         line = i:3
#         for percentage in percentages.values():
#             if percentage >= i:
#                 line += "o"
#             else:
#                 line += " "
#         chart_lines.append(line)


# line += "   " * (3 * len(categories) + 1 - len(line)) - Adjust the number of spaces?

# User
# Test 
# 'Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|          \n 60| o        \n 50| o        \n 40| o        \n 30| o        \n 20| o  o     \n 10| o  o  o  \n  0| o  o  o  \n    ----------\n     F  C  A  \n     o  l  u  \n     o  o  t  \n     d  t  o  \n        h     \n        i     \n        n     \n        g     '
# Chart
# 'Percentage spent by category\n100|         \n 90|         \n 80|         \n 70|         \n 60| o       \n 50| o       \n 40| o       \n 30| o       \n 20| o  o    \n 10| o  o  o \n  0| o  o  o \n    ----------\n      F  C  A \n      o  l  u \n      o  o  t \n      d  t  o \n                     h \n                     i \n                     n \n                     g '


# To make it easier for you to see where the issues are, I have replace all space characters with ☐ characters.

# Expected String:

# Percentage☐spent☐by☐category
# 100|☐☐☐☐☐☐☐☐☐☐
# ☐90|☐☐☐☐☐☐☐☐☐☐
# ☐80|☐☐☐☐☐☐☐☐☐☐
# ☐70|☐☐☐☐o☐☐☐☐☐
# ☐60|☐☐☐☐o☐☐☐☐☐
# ☐50|☐☐☐☐o☐☐☐☐☐
# ☐40|☐☐☐☐o☐☐☐☐☐
# ☐30|☐☐☐☐o☐☐☐☐☐
# ☐20|☐☐☐☐o☐☐o☐☐
# ☐10|☐☐☐☐o☐☐o☐☐
# ☐☐0|☐o☐☐o☐☐o☐☐
# ☐☐☐☐----------
# ☐☐☐☐☐B☐☐F☐☐E☐☐
# ☐☐☐☐☐u☐☐o☐☐n☐☐
# ☐☐☐☐☐s☐☐o☐☐t☐☐
# ☐☐☐☐☐i☐☐d☐☐e☐☐
# ☐☐☐☐☐n☐☐☐☐☐r☐☐
# ☐☐☐☐☐e☐☐☐☐☐t☐☐
# ☐☐☐☐☐s☐☐☐☐☐a☐☐
# ☐☐☐☐☐s☐☐☐☐☐i☐☐
# ☐☐☐☐☐☐☐☐☐☐☐n☐☐
# ☐☐☐☐☐☐☐☐☐☐☐m☐☐
# ☐☐☐☐☐☐☐☐☐☐☐e☐☐
# ☐☐☐☐☐☐☐☐☐☐☐n☐☐
# ☐☐☐☐☐☐☐☐☐☐☐t☐☐

# Actual Returned String:

# Percentage☐spent☐by☐category
# 100|☐☐☐☐☐☐☐
# ☐90|☐☐☐☐☐☐☐
# ☐80|☐☐☐☐☐☐☐
# ☐70|☐☐☐☐o☐☐
# ☐60|☐☐☐☐o☐☐
# ☐50|☐☐☐☐o☐☐
# ☐40|☐☐☐☐o☐☐
# ☐30|☐☐☐☐o☐☐
# ☐20|☐☐☐☐o☐☐o
# ☐10|☐☐☐☐o☐☐o
# ☐☐0|☐o☐☐o☐☐o
# ☐☐☐☐----------
# ☐☐☐☐☐B☐☐F☐☐E☐☐
# ☐☐☐☐☐u☐☐o☐☐n☐☐
# ☐☐☐☐☐s☐☐o☐☐t☐☐
# ☐☐☐☐☐i☐☐d☐☐e☐☐
# ☐☐☐☐☐n☐☐☐☐☐r☐☐
# ☐☐☐☐☐e☐☐☐☐☐t☐☐
# ☐☐☐☐☐s☐☐☐☐☐a☐☐
# ☐☐☐☐☐s☐☐☐☐☐i☐☐
# ☐☐☐☐☐☐☐☐☐☐☐n☐☐
# ☐☐☐☐☐☐☐☐☐☐☐m☐☐
# ☐☐☐☐☐☐☐☐☐☐☐e☐☐
# ☐☐☐☐☐☐☐☐☐☐☐n☐☐
# ☐☐☐☐☐☐☐☐☐☐☐t☐☐
