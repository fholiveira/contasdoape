#language: pt

Funcionalidade: Login
    Contexto: 

    Cenário: Usuário não logado tenta se autenticar
        Dado que eu não estou logado
        Quando eu clicar no botão de login
        Então eu devo ser redirecionado para a página de login do Facebook

    Cenário: Informar novo usuário que ele deve criar apartamento
        Dado que eu sou um novo usuário
        Quando eu fizer login como o Comediante
        Então devo ser direcionado a página de criação de apartamento

    Cenário: Direcionar novo usuário ao Facebook
        Dado que eu sou um novo usuário
        Quando eu fizer login como o Ozymandias
        E eu clicar no botão 'Vou falar com meus colegas no Facebook'
        Então devo ser redirecionado ao Facebook

