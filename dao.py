from models import Usuario

SQL_CRIA_CLIENTE = 'INSERT into cliente (nome,senha,email,cpf) values (%s,%s,%s,%s)'
SQL_DELETA_CLIENTE = 'DELETE from cliente where id=%s'
SQL_ATUALIZA_CLIENTE = 'UPDATE cliente SET nome=%s, senha=%s, email=%s, cpf=%s where id=%s '
SQL_USUARIO_ID = 'SELECT id,nome,senha,email,cpf from cliente where id=%s '
SQL_BUSCA_USUARIO = 'SELECT id,nome,senha,email,cpf from cliente where id=%s '

class UsuarioDao:
    def __init__(self,db):
        self.__db=db
        #cria e atualiza usuario
        def salvar(self,cliente):
            cursor = self.__db.connection.cursor()

            if(cliente._id):
                cursor.execute(SQL_ATUALIZA_CLIENTE,(cliente._nome,cliente._senha,cliente._email, cliente._cpf,cliente._id))
            else:
                cursor.execute(SQL_CRIA_CLIENTE,(cliente._nome,cliente._senha,cliente._email, cliente._cpf))
                cursor._id = cursor.lastrowid

                self.__db.connection.commit()
            return cliente    

        #Deleta usuario
            def deletar_usuario(self,id):
                self.__db.connection.cursor().execute(SQL_DELETA_USUARIO,(id,))
                self.__db.connection.commit()   
        #Busca por id
            def busca_por_id(self,email):
                cursor = self.__db.connection.cursor()
                cursor.execute(SQL_USUARIO_POR_ID,(email,))
                dados = cursor.fetchone()
                usuario = traduz_usuario(dados) if dados else None
                return cliente     