#language: pt

Funcionalidade: Login
    Contexto: 

    Cenário: Usuário não logado tenta se autenticar
        Dado que eu não estou logado
        Quando eu clicar no botão de login
        Então eu devo ser redirecionado para a página de login do Facebook

    Esquema do Cenário: Informar novo usuário que ele deve criar apartamento
        Dado que eu sou um novo usuário
        Quando eu fizer login com <usuário> e <senha>
        Então devo ser direcionado a página de criação de apartamento

    Exemplos: usuários
        | usuário                            | senha   |
        | adrian_fqrabxr_veidt@tfbnw.net     | 123@abc |
    
    Esquema do Cenário: Direcionar novo usuário ao Facebook
        Dado que eu sou um novo usuário
        E eu fizer login com <usuário> e <senha>
        Quando eu clicar no botão 'Vou falar com meus colegas no Facebook'
        Então devo ser redirecionado ao Facebook

    Exemplos: usuários
        | usuário                            | senha   |
        | dan_udodmuj_dreiberg@tfbnw.net     | 123@abc |
