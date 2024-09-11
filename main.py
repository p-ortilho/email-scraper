import sys
from modules import WebScraper
from modules import EmailStorage


if __name__ == '__main__':
    argumentos = sys.argv
    
    if argumentos[1] == '--help':
        print("Para você usar o email scraping você pode usar as seguintes flags:")
        print("--help : Abrir esse menu de ajuda.")
        print("\t Exemplo de execução:")
        print("\t python main.py --help")

        print("-u : Você passa diretamente uma url como argumento.")
        print("\t Exemplo de execução:")
        print("\t python main.py -u https://www.exemplo.io/")
        print("Por padrão os e-mail extraidos através de url única são armazenados em arquivo de texto. Para armazenar em um banco de dados use -db depois da url.")

        print("-a : Passagem de urls através de uma wordlist.")
        print("\t Exemplo de execução:")
        print("\t python main.py -a arquivo.txt")
        print("Por padrão os e-mail extraidos através de wordlist são armazenados em um banco de dados sqlite. Para armazenar em um arquivo de texto use depois da url -o")

        print("-o : A coleta de e-mail é armazenada em um arquivo de texto.")
        print("\t Exemplo de execução:")
        print("\t python main.py -a arquivo.txt -o")

        print("-db : A coleta de e-mail é armazenada em um banco de dados sqlite.")
        print("\t Exemplo de execução:")
        print("\t python main.py -a arquivo.txt -db")
        
    elif argumentos[1] == '-u' and len(argumentos) == 3:
        url = argumentos[2]
    
        obj_scraping = WebScraper(url)
        lista_email = obj_scraping.extract_email()
        
        with open('output.txt', 'a') as arquivo:
            for i in lista_email:
                arquivo.write(i + '\n')
        
        print(f'Extração em {url} finaliza!')

    elif argumentos[1] == '-u' and argumentos[3] == '-db':
        url = argumentos[2]
        lista_tuplas = []

        obj_scraping = WebScraper(url)
        obj_database = EmailStorage()
        lista_email = obj_scraping.extract_email()

        for i in lista_email:
            lista_tuplas.append((url, i))
        
        obj_database.store_email(lista_tuplas)

        print('Extração e armazenamento finalizado!')

        
    elif argumentos[1] == '-a' and argumentos[3] == '-db':
        lista_tuplas = []
        obj_database = EmailStorage()

        with open(argumentos[2], 'r') as arquivo:
            urls_bruta = arquivo.readlines()

        url = [i.rstrip() for i in urls_bruta]

        for u in  url:
            obj_scraping = WebScraper(u)
            lista_email = obj_scraping.extract_email()

            for i in lista_email:
                lista_tuplas.append((u, i))

        obj_database.store_email(lista_tuplas)
        print('Extração e armazenamento finalizado!')

    elif argumentos[1] == '-a' and argumentos[3] == '-o':
        with open(argumentos[2], 'r') as arquivo:
            urls_bruta = arquivo.readlines()

        url = [i.rstrip() for i in urls_bruta]

        for u in  url:
            obj_scraping = WebScraper(u)
            lista_email = obj_scraping.extract_email()

            for i in lista_email:
                with open('output_email.txt', 'a') as arquivo:
                    arquivo.write(i + '\n')
        print('Extração e escrita finalizado!')
