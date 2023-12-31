from typing import Any, List
import sqlite3
from usuario import Usuario

class UsuarioRepositorio:
    """Repositório de usuários.
    
    Attributes:
        db_nome (str): Nome do banco de dados.
    """

    def __init__(self, db_nome: str):
        self.db_nome = db_nome

    # CRUD
    # CREATE
    # READ
    # UPDATE
    # DELETE

    def __executar_query(self, query: str, *params: Any):
        """Executa uma query no banco de dados.
        
        Args:
            query (str): Query que será executada.
            params (Any): Parâmetros da query.
        """
        connection = sqlite3.connect(self.db_nome) # Abriu uma conexão com sqlite
        cursor = connection.cursor()
        cursor.execute(query, params) # Executar a query
        connection.commit() # Commitar as alterações feitas pela consulta
        connection.close() # Fecha a conexão com o banco de dados

    def inserir_usuario(self, usuario: Usuario):
        """Insere um usuário no banco de dados. O objeto usuário é atualizado com o ID do banco.
        
        Args:
            usuario (Usuario): Usuário que será criado no banco de dados.
        """
        query = "INSERT INTO usuarios (nome, email) VALUES (?, ?)"
        self.__executar_query(query, usuario.nome, usuario.email)

        usuario.id = self.__get_ultimo_id_inserido()
        return usuario

    def obter_usuarios(self) -> List[Usuario]:
        """Obtém todos os usuários cadastrados no banco de dados."""
        query = "SELECT * FROM usuarios;"
        connection = sqlite3.connect(self.db_nome)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        return [Usuario(row[1], row[2], row[0]) for row in rows]
    
    def atualizar_usuario(self, usuario: Usuario):
        """Atualiza um usuário no banco de dados.
        
        Args:
            usuario (Usuario): Usuário que será atualizado.
        """
        query = "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?;"
        self.__executar_query(query, usuario.nome, usuario.email, usuario.id)

    def remover_usuario(self, usuario: Usuario):
        """Remove um usuário do banco de dados.
        
        Args:
            usuario (Usuario): Usuário que será resolvido.
        """
        query = "DELETE FROM usuarios WHERE id = ?;"
        self.__executar_query(query, usuario.id)

    def __get_ultimo_id_inserido(self) -> int:
        """Retorna o ID do ultimo registro inserido na tabela de usuários."""
        query = "SELECT id FROM usuarios ORDER BY id DESC LIMIT 1"
        connection = sqlite3.connect(self.db_nome)
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        connection.close()
        return row[0]
