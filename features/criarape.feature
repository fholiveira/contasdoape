#language: pt

Funcionalidade: Criar apê 
	
    Cenário: Novo usuário cria apê
        Dado que eu sou um novo usuário
        E que eu não estou logado
        Quando eu fizer login como o Coruja 
        E clicar no botão "Vou criar o apê agora mesmo"
        Então eu devo ser redirecionado a página de convidar amigos
