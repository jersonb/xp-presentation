# Etreme Programming (XP)

## Programação Extrema

- Metodologia ágil focada em desenvolvimento de software
- Descrita em 1996 por Kent Back
- Popularizada em 2000
- Inspirou o manisfesto ágil

<div align="center">
    <img width="200px" src="./kent_beck.jpg"/>
    <p>Kent Beck Criador do XP</p>
</div>

<hr/>

## Livros sobre XP

||||
|---|---|---|
|![dev_agil_limpo](./dev_agil_limpo.jpeg)|![extreme_programming](./extreme_programming.jpeg)|![programador_pragmatico](./programador_pragmatico_Grande.jpg)|

## Baseado em Valores e Práticas

### Valores

- Feedback
- **Comunicação**
- Simplicidade
- Coragem

### Práticas

- Cliente Presente
- Jogo do Planejamento
- Stand up metting (Reunião de pé)
- **Pair Programming (Programação em Par)**
- **Desenvolvimento Guiado Pelos Testes (TDD)**
- **Refactoring (Refatoração)**
- Código Coletivo
- Código Padronizado
- **Design Simples (de código)**
- Metáfora
- Ritmo Sustentável
- Integração Contínua
- Releases Curtos (Entregas pequenas)

<hr/>

## Dia a dia

### Estória (User Story)

> Escrita pelo PO representa a vontade do usuário

<div align="center">
    <img width="500px" src="./est01.png"/>
</div>

### Caso de teste (Test Case)

> Escrita pelo QA

<div align="center">
    <img width="500px" src="./test_case.png"/>
</div>

### Desenvolvimento Guiado a testes (TDD)

#### Passo 1 - Função soma sem implementação

> Implementar apenas o básico para poder escrecer os testes. Os testes devem falhar.

```py
def soma(valor1, valor2):
    return 0

assert soma(1, 1) == 2
```

> Erro

#### Passo 2 - Implementar função

> Implementar código para fazer os testes passarem

```py
def soma(valor1, valor2):
    return valor1 + valor2

assert soma(1, 1) == 2
```

> Sem erro

#### Passo 3

> Escreve os testes

```py
def exibe_mensagem(valor):
    return False

assert exibe_mensagem("123456")
assert not exibe_mensagem("12345")
```

> Erro

#### Passo 4

> Faz os testes passar

```py
def exibe_mensagem(valor):
    return len(valor) > 5

assert exibe_mensagem("123456")
assert not exibe_mensagem("12345")
```

> Sem erro
