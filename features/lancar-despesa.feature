#language: pt

@firefox
Funcionalidade: Lançar despesa
    Contexto:
	Dado que não estou logado
	Quando me logo como Rorschach
        E clico no botão "Vou criar o apê agora mesmo"

    Cenário: Usuário tenta lançar despesa com dados inválidos
	Dado estou na página de lançar despesas
	E que eu não preenchi os campos
	Quando clico no botão "Lançar"
	Então o campo "data" deve indicar um erro
	Então o campo "valor" deve indicar um erro
	Então o campo "descrição" deve indicar um erro
	E preencho o campo "data" com "aaa" 	
	E clico no botão "Lançar"
	Então o campo "data" deve indicar um erro
	E preencho o campo "valor" com "aaa" 	
	E clico no botão "Lançar"
	Então o campo "valor" deve indicar um erro

    Cenário: Usuário tenta lançar despesa com data no formato "dd/mm/aaaa" e valor inteiro
	Dado que estou na página de lançar despesas
	E preencho o campo "data" com "26/11/1999" 	
	E preencho o campo "valor" com "20" 	
	E preencho o campo "descrição" com "Teste" 	
	Quando clico no botão "Lançar"
	Então devo ser direcionado à página de despesas

    Cenário: Usuário lança despesa com data no formato "aaaa-mm-dd" e valor decimal
	Dado estou na página de lançar despesas
	E preencho o campo "data" com "1999-11-26" 	
	E preencho o campo "valor" com "20,50" 	
	E preencho o campo "descrição" com "Teste" 	
	Quando clico no botão "Lançar"
	Então devo ser direcionado à página de despesas
