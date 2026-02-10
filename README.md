# Agenda em Python usando flask 

Este projeto teve como objetivo aprender mais sobre os conceitos como o padrão de projeto MVC (Model-view-controller), framework Flask e seus componentes, variaveis de ambiente , paradigma de programação orientado a objetos e reforço da linguagem de programçao Python.

Para a seguinte implementção, siga os seguintes passos:

1. Faça um fork deste repositorio, clicando no botão `Fork`

2. Clone este repositorio local 

~~~bash
git clone <url_repositorio>
~~~

3. Abra o projeto utilizando o sei IDE de preferencia

4. Crie um abiente virtual (opcional), utilizando uma 
versão do python >3.12.10

~~~bash
python -m venv .venv
~~~

5. Ative seu ambiente virtual
    
    No bash:

    ~~~bash
    source .venv/Scripts/activate
    ~~~

    No Powershell:

    ~~~powershell
    .\.venv\scripts\activate.ps1
    ~~~~

6. Instale todas as dependencias constantes no arquivo `requeriments.txt`:

~~~python
pip install -r requirements.txt
~~~

7. Copie o arquivo `.env.example`, cole na raiz do projeto e reoneimeie
a copia do arquivo para `.env`

8. Edite o arquivo `.env` para definir seu caminho do banco de dados na 
constante `DATABASE` . Exemplo:

~~~env
DATABASE= './data/meubanco.db'
~~~

9. Rode a aplicação no Python utilizando o comando:

~~~bash
flask run 
~~~

10. Acesse a aplicação do endereço e porta indicados no terminal.
Exemplo:
`http://127.0.0.1:5000`