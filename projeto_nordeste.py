import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 
import webbrowser
import os

dados = {
    'Estado': ['Maranhão', 'Piauí', 'Ceará', 'RN', 'Paraíba', 'Pernambuco', 'Alagoas', 'Sergipe', 'Bahia'],
    'Analfabetismo': [12.8, 13.9, 10.6, 9.5, 13.6, 9.5, 14.1, 10.7, 10.9],
    'Renda': [945, 1110, 1373, 1625, 1183, 1314, 1110, 1393, 1139]
}
df = pd.DataFrame(dados)


plt.figure(figsize=(11, 7)) 

plt.scatter(df['Analfabetismo'], df['Renda'], color='#e74c3c', s=150, alpha=0.8, edgecolors='white', linewidth=0.8)


for i, linha in df.iterrows():
    plt.text(
        linha['Analfabetismo'] + 0.1,  
        linha['Renda'] + 10,           
        linha['Estado'],
        fontsize=9,
        fontweight='bold',
        color='#333333'
    )

plt.title('Renda vs Analfabetismo no Nordeste (2023)', fontsize=16, pad=15)
plt.xlabel('Taxa de Analfabetismo (Pessoas com 15+ anos)', fontsize=12)
plt.ylabel('Renda Média Domiciliar per Capita', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6) 


formatter_x = mticker.FormatStrFormatter('%.1f%%') 
plt.gca().xaxis.set_major_formatter(formatter_x)

formatter_y = mticker.FormatStrFormatter('R$ %.0f') 
plt.gca().yaxis.set_major_formatter(formatter_y)

plt.tight_layout() 

nome_imagem = 'grafico_analise.png'
plt.savefig(nome_imagem)

df_ordenado = df.sort_values(by='Analfabetismo', ascending=True)

df_ordenado['Analfabetismo'] = df_ordenado['Analfabetismo'].apply(lambda x: f'{x:.1f}%')
df_ordenado['Renda'] = df_ordenado['Renda'].apply(lambda x: f'R$ {x:,.0f}'.replace(',', '.')) 

tabela_html = df_ordenado.to_html(index=False, classes='tabela', border=0)



conteudo_html = f"""
<html>
<head>
    <meta charset="UTF-8"> 
    <title>Projeto Nordeste - Educação e Renda</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f4; }}
        .container {{ background: white; padding: 30px; border-radius: 10px; max-width: 800px; margin: 0 auto; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; text-align: center; }}
        h3 {{ color: #34495e; margin-top: 30px; }}
        p {{ line-height: 1.6; color: #555; }}
        img {{ max-width: 100%; border: 1px solid #ccc; margin-top: 20px; display: block; margin-left: auto; margin-right: auto; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
        th {{ background-color: #34495e; color: white; }}
        tr:nth-child(even) {{ background-color: #f9f9f9; }} /* Linhas alternadas */
    </style>
</head>
<body>
    <div class="container">
        <h1>Análise: Impacto da Educação na Renda (Nordeste)</h1>
        <p><strong>Fonte dos Dados:</strong> IBGE - PNAD Contínua 2023 (Série Consolidada).</p>
        <p>O gráfico e a tabela abaixo demonstram a correlação entre a taxa de analfabetismo e a renda domiciliar per capita nos estados do Nordeste.</p>
        
        <img src="{nome_imagem}" alt="Gráfico de Dispersão">
        
        <h3>Tabela Detalhada dos Dados (Ordenada por Analfabetismo):</h3>
        {tabela_html}
    </div>
</body>
</html>
"""

nome_site = 'projeto_analise_nordeste.html'

with open(nome_site, 'w', encoding='utf-8') as arquivo:
    arquivo.write(conteudo_html)

webbrowser.open(nome_site)