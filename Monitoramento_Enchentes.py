# Enzo de Faria Ferreira / 562448
# Guilherme Eduardo de Lima / 566045
# Guilherme de Paula Kuskowski / 562471
# -----------------------------------------
# Projeto Aqua Intel - Monitoramento de Enchentes
# Computational Thinking Using Python
# Cidade: Petrópolis - RJ
# -----------------------------------------

import tkinter as tk
from tkinter import simpledialog, messagebox


def exibir_menu():
    messagebox.showinfo(
        "Aqua Intel",
        "🛰️ Monitoramento de Enchentes - Aqua Intel\n\nCidade: Petrópolis - RJ"
    )


def coletar_niveis(dias):
    niveis = []
    for dia in range(1, dias + 1):
        while True:
            entrada = simpledialog.askstring(
                "Entrada de Dados",
                f"🌊 Digite o nível do rio no dia {dia} (em metros):"
            )

            if entrada is None:
                confirmar = messagebox.askyesno(
                    "Cancelar",
                    "Deseja realmente encerrar o programa?"
                )
                if confirmar:
                    exit()
                else:
                    continue

            try:
                nivel = float(entrada.replace(",", "."))
                if nivel < 0:
                    messagebox.showerror("Erro", "❌ O nível não pode ser negativo. Tente novamente.")
                else:
                    niveis.append(nivel)
                    break
            except ValueError:
                messagebox.showerror("Erro", "❌ Valor inválido. Digite um número.")
    return niveis


def analisar_nivel(nivel):
    if nivel < 1.5:
        return "✅ Seguro"
    elif 1.5 <= nivel <= 2.0:
        return "⚠️ Atenção"
    else:
        return "🚨 ALERTA DE ENCHENTE"


def exibir_dicas():
    return (
        "\n🛟 Dicas de Segurança em Caso de Enchente:\n"
        "- Afaste-se de áreas alagadas e encostas.\n"
        "- Não tente atravessar ruas inundadas.\n"
        "- Desligue energia elétrica se perceber risco de inundação.\n"
        "- Acompanhe os alertas da Defesa Civil de Petrópolis.\n"
        "- Mantenha documentos e objetos de valor em local elevado e seguro.\n"
        "- Prepare uma mochila de emergência com água, alimentos, lanternas e remédios.\n"
    )


def exibir_rotas():
    return (
        "\n🗺️ Rotas de Evacuação Sugeridas em Petrópolis:\n"
        "➝ Rua do Imperador ➝ Avenida Ipiranga ➝ Ginásio Dom Pedro II (Ponto de Encontro).\n"
        "➝ Rua Coronel Veiga ➝ Avenida Barão do Rio Branco ➝ Escola Municipal Rosalina Nicolai.\n"
        "➝ Rua Mosela ➝ Rua Teresa ➝ Centro de Convenções da Universidade Católica de Petrópolis (UCP).\n"
    )


def gerar_relatorio(niveis):
    relatorio = "\n📊 Relatório de Monitoramento:\n\n"
    dias_criticos = 0

    for i, nivel in enumerate(niveis):
        status = analisar_nivel(nivel)
        relatorio += f"Dia {i + 1}: Nível = {nivel}m -> {status}\n"
        if nivel > 2.0:
            dias_criticos += 1

    max_nivel = max(niveis)
    min_nivel = min(niveis)
    dia_max = niveis.index(max_nivel) + 1

    relatorio += "\n📈 Dados Resumidos:\n"
    relatorio += f"👉 Nível Máximo: {max_nivel}m (Dia {dia_max})\n"
    relatorio += f"👉 Nível Mínimo: {min_nivel}m\n"
    relatorio += f"👉 Dias com risco de enchente (nível > 2.0m): {dias_criticos} dia(s)\n"

    if dias_criticos > 0:
        relatorio += "🚨 Atenção! Foram detectados dias com risco de enchente.\n"
    else:
        relatorio += "✅ Nenhum risco de enchente detectado.\n"

    relatorio += exibir_dicas()
    relatorio += exibir_rotas()

    return relatorio


# ---------- Programa Principal ----------
root = tk.Tk()
root.withdraw()  # esconde a janela principal do tkinter

exibir_menu()
qtd_dias = 10  # Monitoramento de 10 dias
niveis_medidos = coletar_niveis(qtd_dias)
relatorio_final = gerar_relatorio(niveis_medidos)

messagebox.showinfo("Relatório Final", relatorio_final)
messagebox.showinfo("Aqua Intel", "🌊 Sistema Aqua Intel finalizado. Fique seguro!")