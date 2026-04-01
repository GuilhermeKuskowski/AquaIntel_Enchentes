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

<img width="588" height="156" alt="image" src="https://github.com/user-attachments/assets/5303be82-d0b1-4e18-81e8-9f1350f0f81a" />

 

2. coletar_niveis(dias)
Coleta os níveis do rio a cada dia com verificação de entrada:
•	Garante que o valor seja positivo e numérico.
•	Armazena os valores em uma lista.

 <img width="886" height="422" alt="image" src="https://github.com/user-attachments/assets/8015e4cd-0c7d-4482-9bec-c87a10cf60a7" />


3. analisar_nivel(nivel)
Classifica o nível informado:
•	Seguro: abaixo de 1.5m
•	Atenção: entre 1.5m e 2.0m
•	Alerta de enchente: acima de 2.0m
 
<img width="452" height="245" alt="image" src="https://github.com/user-attachments/assets/3541b05e-af82-4e45-9ec0-2a2bc8c18c1f" />


4. exibir_dicas()
Imprime orientações importantes em caso de enchente:
•	Segurança pessoal
•	Cuidados com energia elétrica
•	Organização de itens de emergência
 
<img width="880" height="245" alt="image" src="https://github.com/user-attachments/assets/df1f688c-f238-4da0-82d0-21b7a9ba3676" />


5. exibir_rotas()
Sugere rotas de evacuação seguras com pontos de encontro específicos da cidade de Petrópolis.
 


<img width="797" height="145" alt="image" src="https://github.com/user-attachments/assets/c9fd0d64-38f9-4568-84c1-02a47a677426" />




6. gerar_relatorio(niveis)
Gera o relatório de monitoramento:
•	Exibe o status de cada dia com base na análise do nível.
•	Calcula e imprime:
o	Dia com nível máximo
o	Nível mínimo
o	Número de dias críticos (> 2.0m)
•	Mostra dicas e rotas de evacuação.
 

<img width="709" height="666" alt="image" src="https://github.com/user-attachments/assets/ae90c9c9-26ac-4f63-96b7-35e1f2bcfb85" />



▶️ Programa Principal

 <img width="522" height="175" alt="image" src="https://github.com/user-attachments/assets/a0857a10-9969-445f-9292-fa301362d751" />


•	Exibe o menu inicial.
•	Coleta os níveis por 10 dias.
•	Gera o relatório completo com base nos dados inseridos.
•	Finaliza com uma mensagem de encerramento.
