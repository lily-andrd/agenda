from sqlite3 import Cursor
from models.database import Database
from typing import Self, Any, Optional

class Tarefa:
        def __init__(self: Self, titulo_tarefa: Optional[str], data_conclusao: Optional[str] = None, id: Optional[int] = None) -> None:
                self.titulo_tarefa: Optional[str] = titulo_tarefa
                self.data_conclusao: Optional[str] = data_conclusao
                self.id: Optional[int] = id
                # Atrbutos que pertencem ao OBJETO.

        @classmethod
        def id(cls, id: int) -> Self:
                with Database('./data/tarefas.sqlite3') as db:
                        query: str = "SELECT titulo_tarefa, data_conclusao FROM tarefas WHERE id = ?;"
                        params: tuple = (id,)
                        resultado: list[Any] = db.buscar_todos(query, params)
                        if resultado:
                                titulo_tarefa, data_conclusao = resultado[0]
                                return cls(titulo_tarefa, data_conclusao, id)


        def salvar_tarefa(self: Self) -> None:
                with Database('./data/tarefas.sqlite3') as db:
                        query: str = "INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
                        params: tuple = (self.titulo_tarefa, self.data_conclusao)
                        db.executar(query, params)
                        # POST;

        @classmethod
        def obter_tarefas(cls) -> list[Self]:
                with Database('./data/tarefas.sqlite3') as db:
                        query: str = "SELECT titulo_tarefa, data_conclusao FROM tarefas;"
                        resultados: list[Any] = db.buscar_todos(query)
                        tarefas: list[Self] = [cls(titulo, data) for titulo, data in resultados]
                        return tarefas
                        # GET;

        def excluir_tarefa(self) -> Cursor:
                with Database('./data/tarefas.sqlite3') as db:
                        query: str = "DELETE FROM tarefas WHERE id = ?;"
                        params: tuple = (self.id,)
                        resultado: Cursor = db.executar(query, params)
                        return resultado
                        # DELETE;