class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            description = item["description"][:23]
            amount = "{:.2f}".format(item["amount"])
            total += item["amount"]
            items += f"{description:<23}{amount:>7}\n"
        output = title + items + "Total: {:.2f}".format(total)
        return output

def create_spend_chart(categories):
    # Calculate total spent for each category
    total_spent = {category.name: sum(transaction['amount'] for transaction in category.ledger if transaction['amount'] < 0) for category in categories}

    # Calculate total expenses
    total_expenses = sum(total_spent.values())

    # Calculate percentage spent for each category
    percentages = {name: (amount / total_expenses) * 100 for name, amount in total_spent.items()}

    # Create the chart lines
    chart_lines = []
    chart_lines.append("Percentage spent by category")
    for i in range(100, -1, -10):
        line = f"{i:3}|"
        for percentage in percentages.values():
            if percentage >= i:
                line += " o "
            else:
                line += "   "
        chart_lines.append(line)

    # Add the horizontal line
    chart_lines.append("    " + "-" * (3 * len(categories)) + "-")

    # Get category names and determine maximum length
    category_names = [category.name for category in categories]
    max_name_length = max(len(name) for name in category_names)

    # Add the category names below the chart
    for i in range(max_name_length):
        line = "     "
        for name in category_names:
            if i < len(name):
                line += f"{name[i]}  "
            else:
                line += "   "
        chart_lines.append(line)

    # Adjust the last line to ensure proper alignment
    last_line_length = len(chart_lines[-1])
    chart_lines[-1] += " " * (last_line_length - len(chart_lines[-1]))

    # Add spaces for proper alignment in each line
    for i in range(len(chart_lines)):
        chart_lines[i] = chart_lines[i].ljust(last_line_length)

    # Join all the lines to form the chart
    chart = "\n".join(chart_lines)

    return chart

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

test = """Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     """

# print(chart)

print("Test \n" + repr(test))
print("Chart\n" + repr(chart))
