"""
Sistema Bancário - Desafio DIO
==============================

Este módulo implementa um sistema bancário completo com as seguintes funcionalidades:
- Cadastro de clientes com dados pessoais e endereço
- Cadastro de contas correntes vinculadas aos clientes
- Operações bancárias (depósito, saque, extrato) por cliente
- Listagem de clientes e contas
- Validações de negócio (CPF único, uma conta por cliente)

Autor: Desafio DIO - Back-end com Python
Data: 2024
"""

# =============================================================================
# ESTRUTURAS DE DADOS GLOBAIS
# =============================================================================

# Lista para armazenar todos os clientes cadastrados
# Cada cliente é um dicionário com: nome, data_nascimento, cpf, endereco
clientes = []

# Lista para armazenar todas as contas correntes
# Cada conta é um dicionário com: agencia, numero_conta, cpf, saldo, extrato, numero_saques
contas = []


def cadastrar_cliente():
    """
    Cadastra um novo cliente no sistema bancário.
    
    Esta função coleta os dados pessoais do cliente incluindo:
    - Nome completo
    - Data de nascimento
    - CPF (com validação de unicidade)
    - Endereço completo (logradouro, bairro, cidade, UF)
    
    Returns:
        bool: True se o cliente foi cadastrado com sucesso, False caso contrário
        
    Validações:
        - CPF deve ser único no sistema
        - Todos os campos são obrigatórios
    """
    print("\n=== CADASTRO DE CLIENTE ===")
    
    # Solicita e valida CPF (deve ser único)
    cpf = input("Informe o CPF (somente números): ")
    if buscar_cliente_por_cpf(cpf):
        print("Erro: CPF já cadastrado!")
        return False
    
    # Coleta dados pessoais do cliente
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    
    # Coleta dados de endereço
    print("\n--- Endereço ---")
    logradouro = input("Logradouro: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")
    
    # Formata o endereço completo
    endereco = f"{logradouro}, {bairro} - {cidade}/{uf}"
    
    # Cria o dicionário do cliente com todos os dados
    cliente = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    
    # Adiciona o cliente à lista global
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")
    return True


def cadastrar_conta_corrente():
    """
    Cadastra uma nova conta corrente para um cliente existente.
    
    Esta função cria uma conta bancária vinculada ao CPF do cliente.
    Cada cliente pode ter apenas uma conta corrente no sistema.
    
    Returns:
        bool: True se a conta foi cadastrada com sucesso, False caso contrário
        
    Validações:
        - Cliente deve existir no sistema
        - Cliente não pode ter mais de uma conta
        - Número da conta é gerado automaticamente
        
    Estrutura da conta:
        - Agência: 0001 (fixa)
        - Número: sequencial automático
        - Saldo inicial: R$ 0,00
        - Extrato: vazio
        - Saques realizados: 0
    """
    print("\n=== CADASTRO DE CONTA CORRENTE ===")
    
    # Solicita CPF e verifica se o cliente existe
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente_por_cpf(cpf)
    
    if not cliente:
        print("Erro: Cliente não encontrado!")
        return False
    
    # Verifica se o cliente já possui uma conta
    for conta in contas:
        if conta["cpf"] == cpf:
            print("Erro: Cliente já possui uma conta!")
            return False
    
    # Gera número da conta sequencial
    numero_conta = len(contas) + 1
    
    # Cria a estrutura da conta corrente
    conta = {
        "agencia": "0001",           # Agência fixa
        "numero_conta": numero_conta, # Número sequencial
        "cpf": cpf,                   # Vinculação ao cliente
        "saldo": 0,                   # Saldo inicial zerado
        "extrato": "",                # Extrato vazio
        "numero_saques": 0            # Contador de saques
    }
    
    # Adiciona a conta à lista global
    contas.append(conta)
    print(f"Conta cadastrada com sucesso! Número da conta: {numero_conta}")
    return True


def buscar_cliente_por_cpf(cpf):
    """
    Busca um cliente na lista global pelo CPF.
    
    Args:
        cpf (str): CPF do cliente a ser buscado
        
    Returns:
        dict or None: Dicionário com dados do cliente se encontrado, None caso contrário
        
    Nota:
        Esta função é usada para validações de existência e recuperação de dados do cliente.
    """
    # Percorre a lista de clientes procurando pelo CPF
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None


def buscar_conta_por_cpf(cpf):
    """
    Busca uma conta corrente na lista global pelo CPF do cliente.
    
    Args:
        cpf (str): CPF do cliente proprietário da conta
        
    Returns:
        dict or None: Dicionário com dados da conta se encontrada, None caso contrário
        
    Nota:
        Esta função é usada para localizar a conta do cliente para operações bancárias.
    """
    # Percorre a lista de contas procurando pelo CPF
    for conta in contas:
        if conta["cpf"] == cpf:
            return conta
    return None


def depositar(cpf):
    """
    Realiza um depósito na conta corrente do cliente.
    
    Esta função permite que o cliente adicione dinheiro à sua conta.
    O valor é adicionado ao saldo e registrado no extrato.
    
    Args:
        cpf (str): CPF do cliente proprietário da conta
        
    Validações:
        - Conta deve existir no sistema
        - Valor deve ser positivo
        - Valor é solicitado via input do usuário
        
    Efeitos:
        - Atualiza o saldo da conta
        - Adiciona transação ao extrato
        - Exibe mensagem de sucesso ou erro
    """
    # Localiza a conta do cliente
    conta = buscar_conta_por_cpf(cpf)
    if not conta:
        print("Erro: Conta não encontrada!")
        return
    
    # Solicita o valor do depósito
    valor = float(input("Informe o valor do depósito: "))

    # Valida e processa o depósito
    if valor > 0:
        # Atualiza o saldo da conta
        conta["saldo"] += valor
        # Registra a transação no extrato
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")


def sacar(cpf):
    """
    Realiza um saque na conta corrente do cliente.
    
    Esta função permite que o cliente retire dinheiro de sua conta,
    respeitando as regras de negócio do banco.
    
    Args:
        cpf (str): CPF do cliente proprietário da conta
        
    Regras de Negócio:
        - Limite por saque: R$ 500,00
        - Limite de saques por dia: 3 saques
        - Saldo deve ser suficiente
        - Valor deve ser positivo
        
    Validações:
        - Conta deve existir
        - Saldo suficiente
        - Não exceder limite por saque
        - Não exceder limite de saques diários
        - Valor deve ser positivo
        
    Efeitos:
        - Atualiza o saldo da conta
        - Adiciona transação ao extrato
        - Incrementa contador de saques
        - Exibe mensagem de sucesso ou erro
    """
    # Localiza a conta do cliente
    conta = buscar_conta_por_cpf(cpf)
    if not conta:
        print("Erro: Conta não encontrada!")
        return
    
    # Solicita o valor do saque
    valor = float(input("Informe o valor do saque: "))
    
    # Define as regras de negócio
    limite = 500              # Limite por saque
    LIMITE_SAQUES = 3         # Limite de saques por dia

    # Verifica todas as condições para o saque
    excedeu_saldo = valor > conta["saldo"]                    # Saldo insuficiente
    excedeu_limite = valor > limite                          # Valor excede limite por saque
    excedeu_saques = conta["numero_saques"] >= LIMITE_SAQUES # Excedeu limite de saques

    # Processa o saque baseado nas validações
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        # Saque aprovado - atualiza a conta
        conta["saldo"] -= valor                              # Reduz o saldo
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"      # Registra no extrato
        conta["numero_saques"] += 1                          # Incrementa contador
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")


def exibir_extrato(cpf):
    """
    Exibe o extrato bancário da conta corrente do cliente.
    
    Esta função mostra todas as transações realizadas na conta
    e o saldo atual, formatados de forma legível.
    
    Args:
        cpf (str): CPF do cliente proprietário da conta
        
    Validações:
        - Conta deve existir no sistema
        
    Exibição:
        - Cabeçalho formatado
        - Lista de transações (se houver)
        - Saldo atual
        - Rodapé formatado
        
    Nota:
        Se não houver transações, exibe mensagem informativa.
    """
    # Localiza a conta do cliente
    conta = buscar_conta_por_cpf(cpf)
    if not conta:
        print("Erro: Conta não encontrada!")
        return
    
    # Exibe o extrato formatado
    print("\n================ EXTRATO ================")
    
    # Verifica se há transações para exibir
    if not conta["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        print(conta["extrato"])
    
    # Exibe o saldo atual
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")


def listar_clientes():
    """
    Lista todos os clientes cadastrados no sistema.
    
    Esta função exibe informações completas de todos os clientes
    cadastrados, incluindo dados pessoais e endereço.
    
    Exibição:
        - Nome completo
        - CPF
        - Data de nascimento
        - Endereço completo
        - Separador visual entre clientes
        
    Nota:
        Se não houver clientes cadastrados, exibe mensagem informativa.
    """
    # Verifica se há clientes cadastrados
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    
    # Exibe cabeçalho da lista
    print("\n=== LISTA DE CLIENTES ===")
    
    # Percorre e exibe cada cliente
    for cliente in clientes:
        print(f"Nome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")
        print(f"Data de Nascimento: {cliente['data_nascimento']}")
        print(f"Endereço: {cliente['endereco']}")
        print("-" * 40)  # Separador visual


def listar_contas():
    """
    Lista todas as contas correntes cadastradas no sistema.
    
    Esta função exibe informações completas de todas as contas,
    incluindo dados da conta e do cliente proprietário.
    
    Exibição:
        - Dados da conta (agência, número)
        - Dados do cliente (nome, CPF)
        - Saldo atual
        - Separador visual entre contas
        
    Nota:
        Se não houver contas cadastradas, exibe mensagem informativa.
        Busca o nome do cliente através do CPF vinculado à conta.
    """
    # Verifica se há contas cadastradas
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    
    # Exibe cabeçalho da lista
    print("\n=== LISTA DE CONTAS ===")
    
    # Percorre e exibe cada conta
    for conta in contas:
        # Busca dados do cliente proprietário da conta
        cliente = buscar_cliente_por_cpf(conta["cpf"])
        
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero_conta']}")
        print(f"Cliente: {cliente['nome'] if cliente else 'Cliente não encontrado'}")
        print(f"CPF: {conta['cpf']}")
        print(f"Saldo: R$ {conta['saldo']:.2f}")
        print("-" * 40)  # Separador visual


def main():
    """
    Função principal do sistema bancário.
    
    Esta função controla o fluxo principal da aplicação, exibindo
    o menu de opções e direcionando para as funções apropriadas
    baseado na escolha do usuário.
    
    Menu de Opções:
        [u] Cadastrar Usuário - Cadastra novo cliente
        [c] Cadastrar Conta Corrente - Cria conta para cliente existente
        [d] Depositar - Realiza depósito em conta específica
        [s] Sacar - Realiza saque em conta específica
        [e] Extrato - Exibe extrato de conta específica
        [l] Listar Clientes - Lista todos os clientes cadastrados
        [k] Listar Contas - Lista todas as contas correntes
        [q] Sair - Encerra o programa
        
    Fluxo:
        1. Exibe menu de opções
        2. Solicita escolha do usuário
        3. Executa função correspondente
        4. Retorna ao menu (exceto opção sair)
        
    Nota:
        O programa roda em loop infinito até que o usuário escolha sair.
        Todas as operações bancárias requerem CPF do cliente.
    """
    # Define o menu principal do sistema
    menu = """

[u] Cadastrar Usuário
[c] Cadastrar Conta Corrente
[d] Depositar
[s] Sacar
[e] Extrato
[l] Listar Clientes
[k] Listar Contas
[q] Sair

=> """

    # Loop principal do programa
    while True:
        # Solicita a opção do usuário
        opcao = input(menu)

        # Direciona para a função apropriada baseado na opção
        if opcao == "u":
            # Cadastra novo cliente no sistema
            cadastrar_cliente()

        elif opcao == "c":
            # Cria conta corrente para cliente existente
            cadastrar_conta_corrente()

        elif opcao == "d":
            # Realiza depósito - solicita CPF e chama função
            cpf = input("Informe o CPF: ")
            depositar(cpf)

        elif opcao == "s":
            # Realiza saque - solicita CPF e chama função
            cpf = input("Informe o CPF: ")
            sacar(cpf)

        elif opcao == "e":
            # Exibe extrato - solicita CPF e chama função
            cpf = input("Informe o CPF: ")
            exibir_extrato(cpf)

        elif opcao == "l":
            # Lista todos os clientes cadastrados
            listar_clientes()

        elif opcao == "k":
            # Lista todas as contas correntes
            listar_contas()

        elif opcao == "q":
            # Encerra o programa
            print("Saindo do sistema bancário. Até logo!")
            break

        else:
            # Opção inválida - exibe mensagem de erro
            print("Operação inválida, por favor selecione novamente a operação desejada.")


# =============================================================================
# PONTO DE ENTRADA DO PROGRAMA
# =============================================================================

if __name__ == "__main__":
    # Inicia o sistema bancário
    main()