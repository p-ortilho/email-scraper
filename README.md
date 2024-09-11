# 📧 Email Scraper - Aplicação de Extração de Emails
![alt text](_e90f7f4e-87cc-4b55-84e2-c08a011b1da2.jpeg)
Esta aplicação realiza requisições HTTP para sites específicos e, a partir do conteúdo retornado, busca por endereços de email utilizando expressões regulares (regex). Os emails encontrados podem ser armazenados em um banco de dados ou em um arquivo de texto, conforme a preferência do usuário. O código é modular e segue os princípios da Programação Orientada a Objetos (OOP) para garantir fácil manutenção e extensibilidade.

# 🔧 Funcionalidades
- Faz requisições HTTP para páginas web.
- Busca por emails no conteúdo retornado usando regex.
- Armazena os emails encontrados em um banco de dados ou em um arquivo .txt.
- Permite configurar a aplicação através de argumentos passados via linha de comando.
- Modularidade garantida através de OOP, facilitando a manutenção e expansão do projeto.

# 💻 Tecnologias Utilizadas
Python: Linguagem principal para desenvolvimento do script.
Regex: Utilizado para a busca de e-mails no conteúdo retornado da página.
SQLite: Banco de dados leve para armazenar os e-mails, quando escolhido pelo usuário.
Arquivo de texto: Alternativa para armazenamento simples de e-mails.
OOP (Programação Orientada a Objetos): Para garantir um código organizado, modular e de fácil manutenção.
Argumentos via Prompt de Comando: O usuário pode passar parâmetros na execução do script, como o URL do site e o método de armazenamento.

# ✏️ Como usar

1. Clone este repositório:
~~~
git clone git@github.com:p-ortilho/email-scraper.git
~~~

2. Navegue até o diretório do projeto:
~~~
cd email-scraper
~~~

3. Execute o script com os argumentos necessários. Exemplo:
~~~
python main.py -u https://exemplo.com -db
~~~

4. Para saber sobre os comandos execute:
~~~
python main.py --help
~~~