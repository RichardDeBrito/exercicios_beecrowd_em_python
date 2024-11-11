list_pairs = []
list_odds = []
list_positives = []
list_negatives = []


for _ in range(0, 5):
    value = int(input())
    if value % 2 == 0:
        list_pairs.append(value)
    if value % 2 != 0:
        list_odds.append(value)
    if value > 0:
        list_positives.append(value)
    if value < 0:
        list_negatives.append(value)
        
print(f'{len(list_pairs)} valor(es) par(es)')
print(f'{len(list_odds)} valor(es) impar(es)')
print(f'{len(list_positives)} valor(es) positivo(s)')
print(f'{len(list_negatives)} valor(es) negativo(s)')