# Полином Зажигалкина

from string import ascii_lowercase as letters

num_of_vars = int(input())
vars = list(letters[:num_of_vars])
table = sorted([tuple(map(int, input().split())) for _ in range(2 ** num_of_vars)])

result, refresh_col = [], [line[-1] for line in table]

if refresh_col[0]:
    result.append('1')

for line in range(1, 2 ** num_of_vars):
    new_col = []
    for i in range(0, len(refresh_col) - 1):
        new_col.append(refresh_col[i] ^ refresh_col[i + 1])

    if new_col[0]:
        params = table[line][:-1]
        result.append(''.join([vars[i] for i in range(num_of_vars) if params[i]]))

    refresh_col = new_col

print(' + '.join(result))