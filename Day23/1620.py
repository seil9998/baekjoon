import sys

N, M = [int(num) for num in sys.stdin.readline().split()]
pokemon_dict = {}
pokemon_dict_reverse = {}

for index in range(1, N+1):
    pokemon = sys.stdin.readline().strip()
    pokemon_dict[index] = pokemon
    pokemon_dict_reverse[pokemon] = index

for _ in range(M):
    question = sys.stdin.readline().strip()

    if question in pokemon_dict_reverse:
        print(pokemon_dict_reverse[question])
    
    else:
        print(pokemon_dict[int(question)])