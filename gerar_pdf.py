import pandas as pd
from fpdf import FPDF

df = pd.read_excel("produtos.xlsx")
df["quantidade"] = df["preço "].apply(lambda x: x*0.1)
df["liquidação "] = df["preço "]*df["quantidade"]

total_gerado = df["liquidação "].sum()
resumo = df.groupby("produtos ")["liquidação "].sum()

# CRIAR PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 12, "Relatorio de Vendas", ln=True, align="C")
pdf.ln(5)

pdf.set_font("Arial", "", 11)
pdf.cell(0, 8, f"Total Gerado: {total_gerado} Kz", ln=True)
pdf.ln(5)

# Tabela resumo
pdf.set_font("Arial", "B", 11)
pdf.cell(90, 10, "Produto", border=1)
pdf.cell(60, 10, "Total Vendido (Kz)", border=1)
pdf.ln()

pdf.set_font("Arial", "", 11)
for produto, valor in resumo.items():
    pdf.cell(90, 10, str(produto), border=1)
    pdf.cell(60, 10, f"{valor} Kz", border=1)
    pdf.ln()

pdf.ln(10)
pdf.set_font("Arial", "I", 9)
pdf.cell(0, 10, "Gerado com Python - Seu Nome | Portfolio GitHub", ln=True)

pdf.output("relatorio_vendas.pdf")
print("PDF GERADO: relatorio_vendas.pdf")
