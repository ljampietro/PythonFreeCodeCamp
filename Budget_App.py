import math


class Category:
    def __init__(self, name, ):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': - amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, destination_category):
        if self.withdraw(amount, f'Transfer to {destination_category.name}'):
            destination_category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def __str__(self):
        title = f"{self.name:*^30}\n"

        items = ""
        for entry in self.ledger:
            desc = f"{entry['description'][:23]:23}"
            amt = f"{entry['amount']:>7.2f}"
            items += f"{desc}{amt}\n"

        total = f"Total: {self.get_balance()}"
        return title + items + total


def create_spend_chart(categories):
    # 1. Calculate total withdrawals for each category
    withdrawals = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total += abs(item['amount'])
        withdrawals.append(total)

    # 2. Calculate percentages (rounded down to nearest 10)
    total_spent = sum(withdrawals)
    percentages = [math.floor((w / total_spent * 100) / 10) * 10 for w in withdrawals]

    # 3. Build the chart header and bars
    res = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        res += f"{i:3}| "
        for percent in percentages:
            if percent >= i:
                res += "o  "
            else:
                res += "   "
        res += "\n"

    # 4. Add the horizontal line
    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 5. Format the vertical names
    names = [category.name for category in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        res += "     "
        for name in names:
            if i < len(name):
                res += name[i] + "  "
            else:
                res += "   "
        if i < max_len - 1:
            res += "\n"

    return res


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25, "socks")

auto = Category("Auto")
auto.deposit(1000, "deposit")
auto.withdraw(15, "gas")

print(create_spend_chart([food, clothing, auto]))