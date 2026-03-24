# Sistema de gerenciamento de salão de beleza (CRUD simples)

tabela_precos = {
    'corte': 30.0,
    'tintura': 20.0,
    'completo': 45.0
}

agendamentos = []

def agendar():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    servico = input("Serviço (corte/tintura/completo): ").lower()

    valor = tabela_precos.get(servico, 0.0)

    if valor > 0:
        agendamento = {
            "nome": nome,
            "telefone": telefone,
            "servico": servico,
            "valor": valor
        }
        agendamentos.append(agendamento)
        print(">> Agendamento realizado com sucesso!")
    else:
        print(">> Serviço inválido.")

def ver_agenda():
    if not agendamentos:
        print(">> Agenda vazia.")
        return

    for i, ag in enumerate(agendamentos):
        print(f"\n[{i}] Cliente: {ag['nome']}")
        print(f"Telefone: {ag['telefone']}")
        print(f"Serviço: {ag['servico']}")

def atualizar_servico():
    ver_agenda()
    try:
        indice = int(input("Escolha o número do agendamento: "))
        novo = input("Novo serviço: ").lower()

        valor = tabela_precos.get(novo, 0.0)

        if valor > 0:
            agendamentos[indice]['servico'] = novo
            agendamentos[indice]['valor'] = valor
            print(">> Serviço atualizado!")
        else:
            print(">> Serviço inválido.")
    except:
        print(">> Erro ao atualizar.")

def cancelar():
    ver_agenda()
    try:
        indice = int(input("Escolha o número para remover: "))
        agendamentos.pop(indice)
        print(">> Agendamento removido.")
    except:
        print(">> Erro ao remover.")

def relatorio():
    total = sum(ag['valor'] for ag in agendamentos)
    print(f">> Total a receber: R${total:.2f}")

def menu():
    while True:
        print("\n=== SISTEMA SALÃO ===")
        print("1. Agendar")
        print("2. Ver Agenda")
        print("3. Atualizar Serviço")
        print("4. Cancelar")
        print("5. Relatório")
        print("0. Sair")

        op = input("Escolha: ")

        if op == '1':
            agendar()
        elif op == '2':
            ver_agenda()
        elif op == '3':
            atualizar_servico()
        elif op == '4':
            cancelar()
        elif op == '5':
            relatorio()
        elif op == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()