class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f'{self.name:*^30}\n'

        ledger_items = ""
        total = 0
        for item in self.ledger:
            ledger_items += f'{item["description"][:23]:23}' + f'{item["amount"]:>7.2f}\n'

            total += item["amount"]

        ledger_list = f'{title}\n{ledger_items}Total: {str(total)}'
        return ledger_list

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]

        return balance

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False


############### CHART ###############
def create_spend_chart(categories):
    cat_names_list = []
    layout_cat_names_list = []
    withdrawals_list = []
    percentages_list = []

    for category in categories:
        name = category.name
        cat_names_list.append(name)
        name_height = len(max(cat_names_list, key=len))
        layout_cat_names_list = [names.ljust(name_height) for names in cat_names_list]

        cat_withdrawals = 0
        for item in category.ledger:
            amount = item['amount']
            if amount < 0:
                cat_withdrawals += amount
        withdrawals_list.append(cat_withdrawals)
    total_withdrawals = int(round(sum(withdrawals_list)))

    for value in withdrawals_list:
        percentage = value * 100 / total_withdrawals
        percentage = round(percentage // 10) * 10
        percentages_list.append(percentage)

    # Chart
    chart = 'Percentage spent by category\n'

    for number in reversed(range(0, 110, 10)):
        chart += f"{str(number) + '|':>4}"

        for percent in percentages_list:
            if percent >= number:
                chart += ' o '
            else:
                chart += '   '

        chart += ' \n'

    chart += '    ' + '-' * (3 * len(categories) + 1) + '\n'

    for name in zip(*layout_cat_names_list):
        chart += '     ' + ('  '.join(name)) + '  \n'

    return chart.rstrip('\n')
