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