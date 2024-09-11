import requests
import re


class WebScraper:
    """
    Objeto recebe url na sua declaração.
    """

    def __init__(self, url: str) -> None:
        self.url = url

    # Método para fazer a requisição na url e retorna o a resposta da página
    def __fetch_page(self):
        """
        Método responsavel por fazer a requisição na página web, retorna a resposta do get
        """
        try:
            response = requests.get(self.url, timeout=10)

            if response.status_code == 200:
                return response.text
            else:
                print(
                    f'Falha ao acessar {self.url}. Status Code: {response.status_code}')

                return None

        except requests.exceptions.RequestException as error:
            print(f'Falha ao fazer a requisição para {self.url}: {error}')

            return None

    # Método que usa o regex para encontrar o e-mail no conteúdo html
    def extract_email(self):
        """
        Método responsavel por procurar e-mail dentro da resposta do get, usa regex para encontrar o padrão de e-mail, retorna uma lista de e-mail.
        """
        html_content = self.__fetch_page()
        list_email = list(set(re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', html_content)))

        return list_email
