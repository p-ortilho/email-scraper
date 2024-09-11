import sqlite3


class EmailStorage:
    def __init__(self, db_name: str = 'email.db') -> None:
        self.db_name = db_name

    # Método para inicializar a conexão com o banco de dados
    def __connecting_database(self):
        """
        Método de conexão com o banco de dados, retorna a conexão
        """
        try:
            if self.db_name:
                connect = sqlite3.connect(self.db_name)
                return connect
            else:
                print('Nome do banco não foi fornecido.')
                return None

        except sqlite3.Error as error:
            print(f'Erro ao tentar se conectar a {self.db_name}: {error}')
            return None

    # Método para verificar se já existe a tabela email dentro do banco
    def __table_exists(self):
        """
        Método verifica se a tabela email já existe no banco de dados.
        Se a tabela existir retorna True.
        """
        connect = self.__connecting_database()
        cursor = connect.cursor()
        query = """SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'email';"""

        cursor.execute(query)
        response = cursor.fetchall()

        cursor.close()
        connect.close()

        return len(response) > 0

    # Método para criar a tabela de e-mails
    def __create_table(self):
        """
        Método responsável por criar a tabela do banco de dados.
        Para fazer a criação primeiro veirifica se a tabela já existe.
        Se não, ela cria a tabela
        """
        try:
            connect = self.__connecting_database()
            cursor = connect.cursor()
            table_exist = self.__table_exists()

            if table_exist == False:
                query = """CREATE TABLE email(id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT NOT NULL, email TEXT NOT NULL);"""

                cursor.execute(query)
                connect.commit()
                #print('Tabela criada com sucesso!')

                return True
            else:
                #print("Tabela já existe.")

                return None

        except sqlite3.OperationalError as error:
            print(f'Erro ao tentar criar a tabela: {error}')

            return False

        finally:
            cursor.close()
            connect.close()

    # Método para inserção dos dados no banco
    def store_email(self, registro: list):
        """
        Método recebe uma lista de registros, esses registros são inseridos dentro do banco
        """
        try:
            self.__create_table()

            connect = self.__connecting_database()
            cursor = connect.cursor()
            query = """INSERT INTO email(url, email) VALUES(?, ?);"""

            cursor.executemany(query, registro)
            connect.commit()
            cursor.close()
            connect.close()

        except sqlite3.OperationalError as error:
            print(f'Erro ao tentar inserir dados  na tabela: {error}')
            return False
