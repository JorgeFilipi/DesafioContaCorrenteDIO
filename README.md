# 🏦 Sistema Bancário - Desafio DIO

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)]()

Um sistema bancário completo desenvolvido em Python como parte do desafio da Digital Innovation One (DIO) para o curso "Back-end com Python".

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Executar](#-como-executar)
- [Regras de Negócio](#-regras-de-negócio)
- [Exemplos de Uso](#-exemplos-de-uso)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

## 🎯 Sobre o Projeto

Este projeto implementa um sistema bancário completo com gestão de clientes e contas correntes. O sistema permite cadastrar clientes, criar contas bancárias e realizar operações financeiras básicas como depósitos, saques e consulta de extratos.

### 🎯 Objetivos do Desafio

- Implementar um sistema bancário funcional
- Aplicar conceitos de programação orientada a funções
- Gerenciar estruturas de dados em listas
- Implementar validações de negócio
- Criar interface de usuário via terminal

## ✨ Funcionalidades

### 👤 Gestão de Clientes
- ✅ **Cadastro de Clientes**: Registro completo com dados pessoais e endereço
- ✅ **Validação de CPF**: Garantia de unicidade no sistema
- ✅ **Listagem de Clientes**: Visualização de todos os clientes cadastrados

### 🏦 Gestão de Contas
- ✅ **Cadastro de Contas Correntes**: Vinculação de contas aos clientes
- ✅ **Uma Conta por Cliente**: Regra de negócio implementada
- ✅ **Numeração Automática**: Contas numeradas sequencialmente
- ✅ **Listagem de Contas**: Visualização de todas as contas ativas

### 💰 Operações Bancárias
- ✅ **Depósitos**: Adição de valores às contas
- ✅ **Saques**: Retirada de valores com validações
- ✅ **Extratos**: Consulta de movimentações e saldo
- ✅ **Operações por Cliente**: Todas as operações vinculadas ao CPF

### 🔒 Validações e Regras
- ✅ **CPF Único**: Não permite duplicatas
- ✅ **Limite de Saque**: R$ 500,00 por operação
- ✅ **Limite Diário**: Máximo de 3 saques por dia
- ✅ **Saldo Suficiente**: Validação antes de saques
- ✅ **Valores Positivos**: Validação de entradas

## 🛠 Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal
- **Estruturas de Dados**: Listas e dicionários
- **Programação Funcional**: Organização em funções
- **Interface Terminal**: Menu interativo
- **Validações**: Regras de negócio implementadas

## 📁 Estrutura do Projeto

```
Sistema-Bancario/
│
├── desafio.py          # Código principal do sistema
├── README.md           # Documentação do projeto
└── LICENSE            # Licença do projeto
```

### 📊 Estrutura de Dados

#### Cliente
```python
{
    "nome": "João Silva",
    "data_nascimento": "15/03/1990",
    "cpf": "12345678901",
    "endereco": "Rua A, Centro - São Paulo/SP"
}
```

#### Conta Corrente
```python
{
    "agencia": "0001",
    "numero_conta": 1,
    "cpf": "12345678901",
    "saldo": 1500.00,
    "extrato": "Depósito: R$ 1000.00\nSaque: R$ 200.00\n",
    "numero_saques": 1
}
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- Terminal ou prompt de comando

### Instalação e Execução

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/sistema-bancario-dio.git
cd sistema-bancario-dio
```

2. **Execute o programa**
```bash
python desafio.py
```

3. **Use o menu interativo**
```
[u] Cadastrar Usuário
[c] Cadastrar Conta Corrente
[d] Depositar
[s] Sacar
[e] Extrato
[l] Listar Clientes
[k] Listar Contas
[q] Sair
```

## 📋 Regras de Negócio

### 🏦 Sistema Bancário
- **Agência Fixa**: Todas as contas pertencem à agência "0001"
- **Numeração Sequencial**: Contas numeradas automaticamente
- **Saldo Inicial**: R$ 0,00 para novas contas
- **Extrato Vazio**: Novas contas começam sem movimentações

### 👤 Clientes
- **CPF Único**: Não permite cadastro duplicado
- **Dados Completos**: Nome, data de nascimento, CPF e endereço
- **Endereço Estruturado**: Logradouro, bairro, cidade e UF
- **Uma Conta por Cliente**: Limitação de negócio

### 💰 Operações Financeiras
- **Depósitos**: Valores positivos apenas
- **Saques**: Respeitam limite de R$ 500,00
- **Limite Diário**: Máximo 3 saques por dia
- **Saldo Suficiente**: Validação obrigatória
- **Extrato Atualizado**: Todas as operações registradas

## 💡 Exemplos de Uso

### 1. Cadastrar Cliente
```
=== CADASTRO DE CLIENTE ===
Informe o CPF (somente números): 12345678901
Informe o nome completo: João Silva
Informe a data de nascimento (dd/mm/aaaa): 15/03/1990

--- Endereço ---
Logradouro: Rua das Flores, 123
Bairro: Centro
Cidade: São Paulo
UF: SP
Cliente cadastrado com sucesso!
```

### 2. Criar Conta Corrente
```
=== CADASTRO DE CONTA CORRENTE ===
Informe o CPF do cliente: 12345678901
Conta cadastrada com sucesso! Número da conta: 1
```

### 3. Realizar Depósito
```
Informe o CPF: 12345678901
Informe o valor do depósito: 1000.00
Depósito realizado com sucesso!
```

### 4. Consultar Extrato
```
================ EXTRATO ================
Depósito: R$ 1000.00

Saldo: R$ 1000.00
==========================================
```

## 🧪 Testando o Sistema

### Cenário Completo
1. **Cadastre um cliente** com dados completos
2. **Crie uma conta corrente** para o cliente
3. **Realize depósitos** para adicionar saldo
4. **Faça saques** respeitando os limites
5. **Consulte extratos** para verificar movimentações
6. **Liste clientes e contas** para visualizar dados

### Validações a Testar
- ✅ CPF duplicado (deve ser rejeitado)
- ✅ Cliente sem conta (não pode fazer operações)
- ✅ Saque sem saldo (deve ser rejeitado)
- ✅ Saque acima do limite (deve ser rejeitado)
- ✅ Mais de 3 saques por dia (deve ser rejeitado)

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

### 📝 Sugestões de Melhorias
- [ ] Validação de CPF com algoritmo
- [ ] Persistência de dados em arquivo
- [ ] Interface gráfica
- [ ] Relatórios em PDF
- [ ] Sistema de login
- [ ] Histórico de transações
- [ ] Transferências entre contas

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Desafio DIO - Back-end com Python**

- **Digital Innovation One**: [DIO](https://digitalinnovation.one)
- **Curso**: Back-end com Python
- **Desafio**: Sistema Bancário

## 🙏 Agradecimentos

- Digital Innovation One pela oportunidade de aprendizado
- Comunidade Python pela documentação e recursos
- Mentores e colegas pelo suporte durante o desenvolvimento

---

⭐ **Se este projeto foi útil, considere dar uma estrela!** ⭐

---

## 📞 Contato

Para dúvidas ou sugestões sobre este projeto:

- **GitHub**: [@JorgeFilipi](https://github.com/JorgeFilipi)
- **LinkedIn**: [jfdias](https://www.linkedin.com/in/jfdias/)
- **Gmaiil**: jorgefelipe1986@gmail.com

---

**Desenvolvido com ❤️ para o Desafio DIO**
