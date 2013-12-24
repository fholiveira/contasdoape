#language: pt

Funcionalidade: Login
	
    Cenário: Usuário não logado tenta se autenticar
	Dado que eu não estou logado
	Quando eu clicar no botão de login
	Então eu devo ser redirecionado para a página de login do Facebook
