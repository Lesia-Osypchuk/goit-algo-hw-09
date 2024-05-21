def find_min_coins(amount):
    # Номінали монет, впорядковані за зростанням
    denominations = [1, 2, 5, 10, 25, 50]
    
    # Масив для збереження мінімальної кількості монет для кожної суми
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    
    # Масив для збереження останнього номіналу монети, який додається для кожної суми
    last_coin = [0] * (amount + 1)
    
    # Заповнюємо масив мінімальної кількості монет
    for i in range(1, amount + 1):
        for coin in denominations:
            if i >= coin:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    last_coin[i] = coin
    
    # Відновлюємо результатуючий словник з кількістю кожного номіналу монет
    result = {}
    while amount > 0:
        coin = last_coin[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

# Приклад використання функції
amount = 113
print(find_min_coins(amount))  # {1: 1, 2: 1, 10: 1, 50: 2}
