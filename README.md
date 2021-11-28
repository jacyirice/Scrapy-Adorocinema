# Scrapy-Adorocinema

# 🏁 Indice

- [Sobre](#-sobre)
- [Features](#-features)
- [Tecnologias Utilizadas](#%EF%B8%8F-tecnologias-utilizadas)
- [Como baixar o projeto](#-como-baixar-o-projeto)
- [Desenvolvedores](#desenvolvido-por)

## 🔖&nbsp; Sobre

O projeto Scrapy-Adorocinema foi desenvolvido a fim de realizar a extração de dados específicos dos [melhores filmes do AdoroCinema](https://www.adorocinema.com/filmes/melhores/), utilizando apenas expressões regulares.

### Informações extraidas

São extraídas todas as notas de todos os filmes presentes na página, incluindo os que estão em cartaz. Com essas notas obteve-se a quantidade de filmes e a nota média de todos os filmes. Veja o exemplo abaixo.

```json
[
  {
    "total_films": 20,
    "all_notes": [
      4.8, 3.9, 4.8, 4.8, 4.8, 5.0, 4.7, 4.7, 3.9, 4.7, 4.0, 4.7, 4.7, 4.7, 4.1,
      3.9, 3.8, 3.1, 3.0, 3.0
    ],
    "average": 4.3
  },
  {
    "total_films": 22,
    "all_notes": [
      4.7, 4.7, 3.6, 4.7, 4.0, 4.7, 3.7, 4.7, 4.5, 4.7, 4.7, 4.7, 4.3, 4.7, 5.0,
      4.7, 4.1, 3.9, 3.8, 3.1, 3.0, 3.0
    ],
    "average": 4.2
  }
]
```

### Expressão regular

A expressão abaixo foi utilizada para extrair textos que são iniciados por >, seguido por um número de 0 a 5, seguido por uma vírgula, seguido por um número de 0 a 9 e finalizadas com <. Dessa forma foi possível extrair as notas dos filmes utilizando apenas uma expressão regular. Exemplo: 3,2

    >([0-5]{1},{1}[0-9]{1})<

A próxima foi utilizada para saber se existe uma página posterior.

    Próxima

### Como funciona?

O software consiste em um projeto scrapy que utiliza uma [spyder](https://docs.scrapy.org/en/latest/topics/spiders.html) chamada adorocinema_spyder. Veja o metodo parse da spyder abaixo.

```python
response_string = response.text
films = re.findall(r">([0-5]{1},{1}[0-9]{1})<", response_string)
yield {
    'total_films': len(films),
    'all_notes': films,
}

next_page = re.findall("Próxima", response_string)
if next_page is not None:
    self.page += 1
    yield response.follow(f'{response.url.split("?")[0]}?page={self.page}', callback=self.parse)
```

Nessa spyder ocorre o seguinte:

1. Gera a primeira requisição para as urls iniciais, no caso [essa](https://www.adorocinema.com/filmes/melhores/), e a resposta é enviada para o método parse;
2. Analisa as informações recebidas utilizando as expressões regulares e então gera itens com os dados analisados;
3. Os itens passam por um pipeline para limpeza de dados HTML, validar dados extraídos e calcular a média;
4. Verifica se existe uma página seguinte. Se a página existir, então é feito o mesmo processo para as outras páginas.

---

## 🚀 Features

- [x] Extração da quantidade de filmes na página
- [x] Extração das notas de todos os filmes
- [x] Cálculo da média das notas extraídas

---

## ⚒️ Tecnologias utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias

- [Python](https://python.org)
- [Scrapy](https://scrapy.org)

---

## 🗂 Como baixar o projeto e executar

```bash
    # Clonar o repositório
    $ git clone https://github.com/jacyirice/Scrapy-Adorocinema

    # Entrar no diretório
    $ cd Scrapy-Adorocinema

    # Instalar dependências
    $ pip install -r requirements.txt

    # Entrar no diretório do projeto scrapy
    $ cd adorocinema

    # Executar o projeto, será gerado um arquivo saida.json com as informações obtidas
    $ scrapy crawl adorocinema -O saida.json
```

## Desenvolvido por

[Jacyiricê Silva Oliveira](https://github.com/jacyirice/)

[Rayanna Quirino](https://github.com/rayannaQuirino/)

## Disponivel em

[GitHub](https://github.com/jacyirice/Scrapy-Adorocinema)
