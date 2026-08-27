# Sistema de Gerenciamento de Estacionamento em Python

Aplicação em linha de comando desenvolvida em Python para controle de vagas, registro de entradas e saídas de veículos e geração de relatórios de faturamento.

---

## Sobre o Projeto

O objetivo deste projeto é aplicar conceitos essenciais de programação em Python, incluindo:
* Estruturas de repetição e condição (`while`, `if/elif/else`)
* Dicionários e listas para estruturação e armazenamento de dados
* Tratamento de exceções (`try/except`) para validação de entradas do usuário

---

## Funcionalidades

* **1. Entrada de Veículo:** Cadastra placa, proprietário, modelo, tipo de veículo (carro ou moto) e horário de entrada. Garante a validação de vagas disponíveis e impede duplicidade de placas.
* **2. Saída de Veículo:** Calcula o tempo de permanência, o valor devido com base na tarifa horária e registra a forma de pagamento.
* **3. Listagem de Veículos:** Exibe todos os veículos atualmente estacionados.
* **4. Consulta de Vagas:** Informa a quantidade de vagas disponíveis no momento.
* **5. Histórico:** Lista todos os atendimentos já concluídos no sistema.
* **6. Relatório Diário:** Apresenta o total de veículos atendidos, ocupação atual e faturamento bruto acumulado.
* **7. Encerramento:** Finaliza a execução do programa.

---

## Tabela de Tarifas

| Tipo de Veículo | Valor por Hora |
| :--- | :--- |
| Carro | R$ 5,00 / hora |
| Moto | R$ 3,00 / hora |

