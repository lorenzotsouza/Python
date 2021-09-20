class Category:
    def __init__(this, name):
        this.name = name
        this.ledger = list()

    def __str__(this):
        output = '******************************'
        l = len(this.name)
        p = len(output) - l
        p //= 2
        output = output[:p] + this.name + output[p + l:]
        for item in this.ledger:
            output += '\n' + item['description'][:23]
            i = len(item['description'][:23])
            amount = round(item['amount'], 2)
            amount = '{0:.2f}'.format(amount)
            if len(amount) > 7:
                amount = amount[len(amount) - 7:]

            for n in range(30 - i - len(amount)):
                output += ' '
            output += amount
        output += '\n' + 'Total: ' + str(round(this.get_balance(), 2))
        # print(output)
        return output

    def deposit(this, amount, description=''):
        this.ledger.append({'amount': amount, 'description': description})

    def withdraw(this, amount, description=''):
        if this.check_funds(amount):
            this.ledger.append({
                'amount': 0 - amount,
                'description': description
            })
        return this.check_funds(amount)

    def get_balance(this):
        balance = 0.00
        for dic in this.ledger:
            balance += dic['amount']
        return balance

    def transfer(this, amount, category):
        if this.check_funds(amount):
            this.withdraw(amount, 'Transfer to ' + category.name)
            category.deposit(amount, 'Transfer from ' + this.name)
        return this.check_funds(amount)

    def check_funds(this, amount):
        return this.get_balance() >= amount


def create_spend_chart(categories):
    items = len(categories)
    if items == 0:
        return 'No categories provided'
    chart = 'Percentage spent by category\n'
    data = list()
    lines = 0
    total = 0.00

    for cat in categories:
        # takes longest cat name to set number of lines
        if lines < len(cat.name):
            lines = len(cat.name)

        spent = 0.00
        for wit in cat.ledger:
            if wit['amount'] < 0:
                spent += wit['amount']
        total += spent
        data.append([cat.name, abs(spent)])

    total = abs(total)

    for d in data:
        percent = d[1] / total * 100
        d[1] = percent

    # print(data)
    for n in reversed(range(11)):
        n = n * 10
        num = str(n)
        line = str()
        if num == '0':
            line += ' '
        if num != '100':
            line += ' '
        line += num + '|'

        for d in data:
            if n < d[1]:
                line += ' o '
            else:
                line += '   '

        chart += line + ' \n'

    chart += '    -'
    for n in range(items):
        chart += '---'

    for n in range(lines):
        chart += '\n    '
        for d in data:
            try:
                chart += ' ' + d[0][n] + ' '
            except:
                chart += '   '
        chart += ' '

    return chart
