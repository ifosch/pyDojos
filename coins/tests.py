import unittest
import coins

def coin_value(coin):
    if coin.rfind('c') > 0:
        return float(coin.strip('c')) / 100
    else:
        return float(coin.strip('e'))

def quantity_is_optimal(silver, wallet = None):
    accum = 0.0
    for i, k in enumerate(coins.coins):
        if k in silver.keys():
            accum += silver[k] * coin_value(k)
            if i + 1 < len(coins.coins):
                n = coins.coins[i + 1]
                if n in silver.keys() and silver[n] > 0:
                    next_value = silver[n] * coin_value(n)
                else:
                    next_value = 1 * coin_value(n)
            else:
                return True
            if wallet is None and accum >= next_value:
                return False
    return True

def extract_list(change):
    coins = ['5c', '10c', '20c', '50c', '1e', '2e']
    base = []
    for k in coins:
        base.append(change[k])
    return base
    
def consumed_too_much(wallet, change):   
    return False in [False for n, m in zip(extract_list(wallet), extract_list(change)) if n - m < 0]
        
class TestCoinChanger(unittest.TestCase):
    def test_5c(self):
        silver = coins.change(0.05)
        self.assertEqual(silver['5c'], 1)

    def test_generic(self):
        amounts = [0.05, 0.10, 0.25, 2.35, 3.00, 5.50]
        for amount in amounts:
            silver = coins.change(amount)
            change = round(sum([q * coin_value(k) for k, q in silver.items()]), 2)
            self.assertEqual(change, amount)
            self.assertTrue(quantity_is_optimal(silver))

    def test_limited(self):
        amounts = [0.05, 0.10, 0.25, 2.35, 3.00, 5.50]
        for amount in amounts:
            wallet = {'5c': 2, '10c': 2, '20c': 2, '50c': 2, '1e': 2, '2e': 1}
            silver = coins.change(amount, wallet)
            change = round(sum([q * coin_value(k) for k, q in silver.items()]), 2)
            self.assertEqual(change, amount)
            self.assertFalse(consumed_too_much(wallet, silver))
            self.assertTrue(quantity_is_optimal(silver, wallet))

if __name__ == '__main__':
    unittest.main()