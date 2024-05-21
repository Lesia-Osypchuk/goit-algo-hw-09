def find_coins_greedy(amount):
    # Номінали монет, впорядковані за спаданням
    denominations = [50, 25, 10, 5, 2, 1]
    
    # Результуючий словник для збереження кількості кожного номіналу
    result = {}
    
    # Перебираємо кожен номінал
    for coin in denominations:
        if amount >= coin:
            # Визначаємо кількість монет цього номіналу
            num_coins = amount // coin
            # Додаємо кількість монет цього номіналу до результату
            result[coin] = num_coins
            # Зменшуємо залишкову суму на вартість використаних монет
            amount -= num_coins * coin
    
    return result

# Приклад використання функції
amount = 113
print(find_coins_greedy(amount))  # {50: 2, 10: 1, 2: 1, 1: 1}