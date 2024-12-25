# Imprime a árvore
for i in range(1, 30, 2):
    print(('*' * i).center(50))

# Imprime o tronco da árvore
for _ in range(5):
    print(' ' * 22, '||')

# Imprime a base da árvore
for i in ['\======/', ' \====/ ']:
    print(' ' * 19, i)

# Mensagem "FELIZ NATAL" em arte ASCII
message = """
    ######## ######## ##       #### ########    ##    ##    ###    ########    ###    ##
    ##       ##       ##        ##       ##     ###   ##   ## ##      ##      ## ##   ##
    ##       ##       ##        ##      ##      ####  ##  ##   ##     ##     ##   ##  ##
    ######   ######   ##        ##     ##       ## ## ## ##     ##    ##    ##     ## ##
    ##       ##       ##        ##    ##        ##  #### #########    ##    ######### ##
    ##       ##       ##        ##   ##         ##   ### ##     ##    ##    ##     ## ##
    ##       ######## ######## #### ########    ##    ## ##     ##    ##    ##     ## ########

"""

# Imprime a mensagem centralizada
print(message.center(50))