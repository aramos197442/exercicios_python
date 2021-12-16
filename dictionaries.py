users_list = [
    {
        'nome':'Alexandre',
        'sexo':'M',
        'idade':47,
        'peso':98
    },
    {
        'nome':'Cristiane',
        'sexo':'F',
        'idade':46,
        'peso':62
    },
    {
        'nome':'Enzo',
        'sexo':'M',
        'idade':11,
        'peso':31
    },
    {
        'nome':'Valentina',
        'sexo':'F',
        'idade':9,
        'peso':20
    },
]

for user_dict in users_list:
    for user in user_dict:
        print(F'{user}: {user_dict[user]}')

    print('-----------------------')