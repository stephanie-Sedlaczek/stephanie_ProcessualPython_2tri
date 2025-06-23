print("Seja bem-vindo")
print("qual seria sua duvida?")
print("1. O que é o sistema PIX e como usá-lo?")
print("2. Como posso realizar transferências entre contas?")
print("3. Como posso bloquear meu cartão?")
print("4. fale conosco")
numero = int(input("selecione um numero que melhor descreve sua duvida: "))
if numero == 1:
    print("O que é o sistema PIX e como usá-lo?\n")
    print("Você pode abrir uma conta bancária de forma simples através do nosso site, no aplicativo do banco ou em uma de nossas agências. Para isso, basta apresentar um documento de identificação oficial com foto (RG ou CNH), comprovante de residência recente e CPF. Caso você tenha menos de 18 anos, é necessário que um responsável legal esteja presente no momento da abertura.")
if numero == 2:
    print("Como posso realizar transferências entre contas?\n")
    print("As transferências entre contas podem ser feitas através do nosso aplicativo, internet banking ou diretamente nas agências. Para transferências entre contas do mesmo banco, basta inserir os dados da conta destinatária. Para transferências entre bancos diferentes, você pode utilizar o sistema TED ou PIX, que são rápidos e eficientes.")
if numero == 3:
    print("Como posso bloquear meu cartão?\n")
    print("O PIX é uma forma de pagamento instantâneo que permite transferências entre contas de diferentes bancos em qualquer dia e horário, com rapidez e sem custos. Para usar, basta acessar o aplicativo do banco, escolher a opção Transferir ou Pagar, selecionar a chave PIX do destinatário (que pode ser o CPF, e-mail ou número de telefone) e confirmar a transação.")
if numero == 4:
    print("fale conosco")
    duvida = input("qual sua duvida? \n")
    print("Mensagem enviada!")
