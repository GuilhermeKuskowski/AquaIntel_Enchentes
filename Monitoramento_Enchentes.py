#Enzo de Faria Ferreira / 562448
#Guilherme Eduardo de Lima / 566045
#Guilherme de Paula Kuskowski / 562471
# -----------------------------------------
# Projeto Aqua Intel - Monitoramento de Enchentes
# Computational Thinking Using Python
# Cidade: Petrópolis - RJ
# -----------------------------------------

def exibir_menu():
    print("=" * 60)
    print("🛰️  Monitoramento de Enchentes - Aqua Intel")
    print("=" * 60)


def coletar_niveis(dias):
    niveis = []
    for dia in range(1, dias + 1):
        while True:
            try:
                nivel = float(input(f"🌊 Digite o nível do rio no dia {dia} (em metros): "))
                if nivel < 0:
                    print("❌ O nível não pode ser negativo. Tente novamente.")
                else:
                    niveis.append(nivel)
                    break
            except ValueError:
                print("❌ Valor inválido. Digite um número.")
    return niveis

def analisar_nivel(nivel):
    if nivel < 1.5:
        return "✅ Seguro"
    elif 1.5 <= nivel <= 2.0:
        return "⚠️ Atenção"
    else:
        return "🚨 ALERTA DE ENCHENTE"
    
def exibir_dicas():
    print("\n🛟 Dicas de Segurança em Caso de Enchente:")
    print("- Afaste-se de áreas alagadas e encostas.")
    print("- Não tente atravessar ruas inundadas.")
    print("- Desligue energia elétrica se perceber risco de inundação.")
    print("- Acompanhe os alertas da Defesa Civil de Petrópolis.")
    print("- Mantenha documentos e objetos de valor em local elevado e seguro.")
    print("- Prepare uma mochila de emergência com água, alimentos, lanternas e remédios.")

def exibir_rotas():
    print("\n🗺️ Rotas de Evacuação Sugeridas em Petrópolis:")
    print("➝ Rua do Imperador ➝ Avenida Ipiranga ➝ Ginásio Dom Pedro II (Ponto de Encontro).")
    print("➝ Rua Coronel Veiga ➝ Avenida Barão do Rio Branco ➝ Escola Municipal Rosalina Nicolai.")
    print("➝ Rua Mosela ➝ Rua Teresa ➝ Centro de Convenções da Universidade Católica de Petrópolis (UCP).")

def gerar_relatorio(niveis):
    print("\n📊 Relatório de Monitoramento:\n")
    dias_criticos = 0

    for i, nivel in enumerate(niveis):
        status = analisar_nivel(nivel)
        print(f"Dia {i + 1}: Nível = {nivel}m -> {status}")
        if nivel > 2.0:
            dias_criticos += 1

    max_nivel = max(niveis)
    min_nivel = min(niveis)
    dia_max = niveis.index(max_nivel) + 1

    print("\n📈 Dados Resumidos:")
    print(f"👉 Nível Máximo: {max_nivel}m (Dia {dia_max})")
    print(f"👉Nível Mínimo: {min_nivel}m")
    print(f"👉 Dias com risco de enchente (nível > 2.0m): {dias_criticos} dia(s)")

    if dias_criticos > 0:
        print("🚨 Atenção! Foram detectados dias com risco de enchente.")
    else:
        print("✅ Nenhum risco de enchente detectado.")

    exibir_dicas()
    exibir_rotas()