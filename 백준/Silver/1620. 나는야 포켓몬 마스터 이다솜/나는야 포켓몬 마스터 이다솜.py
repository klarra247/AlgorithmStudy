
n, m = map(int, input().split())

pokemon_list = []
pokemon_dict = {}

for i in range(n):
    pokemon = input()
    pokemon_list.append(pokemon)
    pokemon_dict[pokemon] = i + 1


for i in range(m):
    given = input()
    if given[0].isalpha():
        print(pokemon_dict[given])
    else:
        print(pokemon_list[int(given) - 1])