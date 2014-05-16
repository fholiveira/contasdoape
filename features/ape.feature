#language: pt

Funcionalidade: Criar apê 
    Contexto:
	Dado que não estou logado
	Quando me logo como Rorschach
        E clico no botão "Vou criar o apê agora mesmo"
	
    Cenário: Usuário tenta mudar o dia para um valor que não é um dia
        Dado que eu estou na página de informações do apê
	E eu clico no link de alterar o dia
	Quando eu deixo o campo em branco
	E clico no botão "Salvar"
        Então eu devo ver uma mensagem de erro
	Quando eu preencho o campo com "AAAA"
        Então eu devo ver uma mensagem de erro
	Quando eu preencho o campo com "54"
        Então eu devo ver uma mensagem de erro

    Cenário: Usuário alterar dia do acerto
        Dado que eu estou na página de informações do apê
	E eu clico no link de alterar o dia
	Quando eu preencho o campo com "17"
	E clico no botão "Salvar"
	Então devo ver que dia do acerto agora é "17"
