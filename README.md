📘 Documentação do Projeto
🛰️ Aqua Intel – Sistema de Monitoramento de Enchentes
Cidade alvo: Petrópolis - RJ
Disciplina: Pensamento Computacional com Python
Autores:
•	Enzo de Faria Ferreira / 562448
•	Guilherme Eduardo de Lima / 566045
•	Guilherme de Paula Kuskowski / 562471
______________
📌 Objetivo
O sistema tem como objetivo coletar os níveis de um rio durante um período de 10 dias, classificar os riscos de enchente, gerar um relatório com estatísticas e fornecer dicas de segurança e rotas de evacuação para a população da cidade de Petrópolis - RJ.
______________
📂 Estrutura do Código
1. exibir_menu()
Exibe o cabeçalho inicial do programa com um título estilizado.

<img width="588" height="156" alt="image" src="https://github.com/user-attachments/assets/59194c0e-c936-4181-bd48-9f8ccfc3bbba" />


 

2. coletar_niveis(dias)
Coleta os níveis do rio a cada dia com verificação de entrada:
•	Garante que o valor seja positivo e numérico.
•	Armazena os valores em uma lista.

<img width="886" height="422" alt="image" src="https://github.com/user-attachments/assets/408cce35-1d92-4959-91bb-b0b6faf6d83d" />



3. analisar_nivel(nivel)
Classifica o nível informado:
•	Seguro: abaixo de 1.5m
•	Atenção: entre 1.5m e 2.0m
•	Alerta de enchente: acima de 2.0m
 
<img width="452" height="245" alt="image" src="https://github.com/user-attachments/assets/d1562124-36a2-4478-bf69-a12d49881d25" />



4. exibir_dicas()
Imprime orientações importantes em caso de enchente:
•	Segurança pessoal
•	Cuidados com energia elétrica
•	Organização de itens de emergência
 
<img width="880" height="245" alt="image" src="https://github.com/user-attachments/assets/dc5f6aa7-1aed-4cf4-bc06-7f1e2526d780" />



5. exibir_rotas()
Sugere rotas de evacuação seguras com pontos de encontro específicos da cidade de Petrópolis.
 


<img width="797" height="145" alt="image" src="https://github.com/user-attachments/assets/853e9187-ad44-4dc9-874e-af8cca6a9f5f" />





6. gerar_relatorio(niveis)
Gera o relatório de monitoramento:
•	Exibe o status de cada dia com base na análise do nível.
•	Calcula e imprime:
o	Dia com nível máximo
o	Nível mínimo
o	Número de dias críticos (> 2.0m)
•	Mostra dicas e rotas de evacuação.
 

<img width="709" height="666" alt="image" src="https://github.com/user-attachments/assets/c49538d7-d4cc-4e50-9227-d53342d37d9a" />
 />



▶️ Programa Principal


<img width="522" height="175" alt="image" src="https://github.com/user-attachments/assets/93e41983-6906-49ea-a68f-67c7dd24c993" />



•	Exibe o menu inicial.
•	Coleta os níveis por 10 dias.
•	Gera o relatório completo com base nos dados inseridos.
•	Finaliza com uma mensagem de encerramento.
