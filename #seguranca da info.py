import hashlib

def cadastrar_usuario():
    nome = input("Digite o nome do usuário (até 20 caracteres): ")
    senha = input("Digite a senha do usuário (4 caracteres): ")
    
    # Verifica se o nome e a senha têm o tamanho correto
    if len(nome) > 20:
        print("O nome deve ter até 20 caracteres.")
        return
    elif len(senha) != 4:
        print("A senha deve ter exatamente 4 caracteres.")
        return
    
    # Gera o hash MD5 da senha
    senha_hash = hashlib.md5(senha.encode()).hexdigest()
    
    # Cria uma string com os dados do usuário
    usuario = f"Nome: {nome}\nSenha: {senha_hash}\n"
    
    # Abre o arquivo para adicionar o usuário
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(usuario)
    
    print("Usuário cadastrado com sucesso.")

def autenticar_usuario():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")
    
    senha_hash = hashlib.md5(senha.encode()).hexdigest()
    
    # Abre o arquivo para ler os usuários cadastrados
    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()
    
    # Verifica se o usuário e a senha estão corretos
    for usuario in usuarios:
        nome_cadastrado = usuario.split("\n")[0].split(": ")[1]
        senha_cadastrada = usuario.split("\n")[1].split(": ")[1]
        
        if nome == nome_cadastrado and senha_hash == senha_cadastrada:
            print("Usuário autenticado com sucesso.")
            return
    
    print("Usuário ou senha incorretos.")

# Menu principal
while True:
    print("Selecione uma opção:")
    print("1 - Cadastrar usuário")
    print("2 - Autenticar usuário")
    print("3 - Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        autenticar_usuario()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")