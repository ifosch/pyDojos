coins = ['5c', '10c', '20c', '50c', '1e', '2e']
values = {'5c': 0.05, '10c': 0.1, '20c': 0.2, '50c': 0.5, '1e': 1, '2e': 2}
reversed_coins = coins.copy()
reversed_coins.reverse()

def change(amount, wallet = None):
    original = amount
    diff = 1
    if wallet is None:
        wallet = {'2e': 1, '1e': 1, '50c': 1, '20c': 1, '10c': 1, '5c': 1}
        diff = 0
    result = {}
    for coin in reversed_coins:
        result[coin] = amount // values[coin]
        if wallet[coin] < result[coin]:
            carry = (result[coin] - wallet[coin]) * diff
            result[coin] -= carry
        amount -= result[coin] * values[coin]
        amount = round(amount, 2)
    print("{} {}".format(original, result))
    return result