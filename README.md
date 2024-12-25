# Árvore de Natal em Arte ASCII

Este projeto consiste em um script Python que imprime uma árvore de Natal estilizada com arte ASCII, incluindo a copa, tronco, base, e uma mensagem de "FELIZ NATAL". É uma maneira criativa e festiva de celebrar o Natal usando programação!

---

## Estrutura do Projeto

### 1. Impressão da Copa da Árvore

A copa da árvore é composta por linhas de asteriscos (`*`) alinhados ao centro, formando um formato triangular. O código utiliza um loop `for` com incrementos de 2 para criar a forma:

```python
for i in range(1, 30, 2):
    print(('*' * i).center(50))
```

### 2. Impressão do Tronco

O tronco é representado por cinco linhas de caracteres `||`, centralizados com espaços em branco:

```python
for _ in range(5):
    print(' ' * 22, '||')
```

### 3. Impressão da Base

A base é criada com duas linhas representando a parte inferior da árvore, usando sequências de igual (`=`):

```python
for i in ['\======/', ' \====/ ']:
    print(' ' * 19, i)
```

### 4. Mensagem de "FELIZ NATAL"

A mensagem é uma arte ASCII que é armazenada em uma string multi-linha e exibida ao final:

```python
message = """
    ######## ######## ##       #### ########    ##    ##    ###    ########    ###    ##
    ##       ##       ##        ##       ##     ###   ##   ## ##      ##      ## ##   ##
    ##       ##       ##        ##      ##      ####  ##  ##   ##     ##     ##   ##  ##
    ######   ######   ##        ##     ##       ## ## ## ##     ##    ##    ##     ## ##
    ##       ##       ##        ##    ##        ##  #### #########    ##    ######### ##
    ##       ##       ##        ##   ##         ##   ### ##     ##    ##    ##     ## ##
    ##       ######## ######## #### ########    ##    ## ##     ##    ##    ##     ## ########
"""
print(message.center(50))
```

---

## Requisitos

Para executar este script, você precisa de:

- Python 3.x instalado em seu computador.
- Um terminal ou IDE para executar o script.

---

## Como Usar

1. Copie o código para um arquivo Python (por exemplo, `arvore_natal.py`).
2. Execute o script em um terminal ou IDE de sua preferência:

   ```
   python arvore_natal.py
   ```

3. O resultado será uma árvore de Natal impressa no terminal.

---

## Resultado Esperado

O script exibe:

1. A copa da árvore em forma triangular.
2. Um tronco com cinco linhas de "||".
3. Uma base com formas estilizadas.
4. Uma mensagem ASCII de "FELIZ NATAL" centralizada.

---

## Contribuições

Contribuições são bem-vindas! Caso deseje adicionar mais elementos decorativos ou melhorar o design, sinta-se à vontade para enviar um pull request.

---

## Licença

Este projeto é de uso livre e pode ser modificado ou compartilhado conforme desejado.

Feliz Natal e boas festas!
