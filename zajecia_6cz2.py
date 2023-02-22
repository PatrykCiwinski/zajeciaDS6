nums = {
    'dave': 3,
    'albert': 1,
    'michał': 3,
    'tomek': 5,
    'dave': 9,
    'jim': 5
}
 # Nie może być 2 takich samych kluczy w słowniku. W przeciwnym przypadku pierwszy taki klucz zostanie zastąpiony drugim
 # Nie tworzymy dwóch takich samych kluczy (błąd semantyczny ale nie syntaktyczny)
print(nums)

# Iterując po zduplikowanych kluczach automatycznie usuwa te duplikaty (można w tym celu jawnie użyć też metody set())
for k in nums.keys():
    print(k)

for v in nums.values():
    print(v)
# Dzięki metodzie set() usuwam duplikat wartości
for v in set(nums.values()):
    print(v)