notes, coins = map(int, input().split('.'))
list_notes = [100, 50, 20, 10, 5, 2]
list_coins = [1000, 500, 250, 100, 50, 10]

print('NOTAS:')
for note in list_notes:
    quant = notes//note
    notes = notes%note
    print(f'{quant} nota(s) de R$ {note:.2f}')

print('MOEDAS:')
notesrest = notes*1000
coinsfloat = notesrest + (coins*10)
for coins in list_coins:
    quantcoins = coinsfloat//coins
    coinsfloat = coinsfloat%coins
    print(f'{quantcoins} moeda(s) de R$ {coins/1000:.2f}')