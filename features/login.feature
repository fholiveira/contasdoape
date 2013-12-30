#language: pt

Funcionalidade: Login
	
    Cenário: Usuário não logado tenta se autenticar
        Dado que eu não estou logado
        Quando eu clicar no botão de login
        Então eu devo ser redirecionado para a página de login do Facebook

    Esquema do Cenário: Informar novo usuário que ele deve criar apartamento
        Dado que eu sou um novo usuário
        Quando eu fizer login com <usuário> e <senha>
        Então devo ser direcionado a página de criação de apartamento

    Exemplos: usuários
        | usuário                            | senha  |
        | barbara_iprrihk_da_silva@tfbnw.net | 123456 |
