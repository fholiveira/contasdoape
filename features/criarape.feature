#language: pt

Funcionalidade: Criar apê 
	
    Esquema do Cenário: Novo usuário cria apê
        Dado que eu sou um novo usuário
        E que eu não estou logado
        Quando eu fizer login com <usuário> e <senha>
        E clicar no botão "Vou criar o apê agora mesmo"
        Então eu devo ser redirecionado a página de convidar amigos

    Exemplos: usuários
        | usuário                            | senha  |
        | barbara_iprrihk_da_silva@tfbnw.net | 123456 |
