# Transição Energética e Estrutura Produtiva do Transporte Terrestre no Brasil  
### Uma Análise Insumo-Produto

Este repositório contém os códigos, bases de dados e resultados utilizados na dissertação de mestrado em **Economia Aplicada** desenvolvida na **Universidade Federal de Viçosa (UFV)**.

---

## 📘 Informações Acadêmicas

- **Curso:** Mestrado em Economia Aplicada  
- **Instituição:** Universidade Federal de Viçosa (UFV)  
- **Período:** 2024 – 2026  
- **Título da Dissertação:**  
  *Transição Energética e Estrutura Produtiva do Transporte Terrestre no Brasil: Uma Análise Insumo-Produto*  
- **Fomento:** Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES)

---

## 🎯 Objetivo do Projeto

O objetivo deste projeto é analisar os impactos econômicos da **transição energética no transporte terrestre brasileiro**, utilizando um **modelo insumo-produto (MIP)**, com foco em:

- Estrutura produtiva do setor de transporte terrestre  
- Encadeamentos intersetoriais  
- Multiplicadores econômicos (produção, renda e emprego)  
- Simulação de cenários de transição energética a partir de matrizes ajustadas

---

## 🧠 Metodologia

- Modelo **Insumo-Produto** aplicado à economia brasileira  
- Base matricial fornecida pela **Empresa de Pesquisa Energética (EPE)**  
- Construção e ajuste de matrizes técnicas  
- Cálculo de multiplicadores tipo I  
- Simulação de cenários contrafactuais de transição energética  
- Implementação em **Python**, com uso intensivo de notebooks Jupyter

---

## 📁 Estrutura do Repositório

```text
mip-energia/
│
├── app/                    # Notebooks principais do projeto
│   ├── main.ipynb           # Notebook principal (versão atual)
│   ├── diagrama.ipynb       # Diagramas e visualizações auxiliares
│   └── *_main.ipynb         # Versões intermediárias e backups
│
├── data/                   # Bases de dados
│   ├── mips/               # Matrizes insumo-produto
│   │   ├── mip-original.xlsx
│   │   ├── mip-epe.xlsx
│   │   ├── cenarios/       # Arquivos e mapas dos cenários simulados
│   │   └── backup/         # Versões anteriores das MIPs
│   │
│   ├── multiplicadores/    # Resultados de multiplicadores
│   │   ├── multiplicadores_producao.xlsx
│   │   ├── multiplicadores_renda.xlsx
│   │   ├── multiplicadores_emprego.xlsx
│   │   └── old/            # Versões anteriores
│   │
│   ├── va_pib.xlsx
│   ├── variaveis.xlsx
│   └── x.xlsx
│
├── functions/              # Funções auxiliares
│   └── function.py
│
├── .gitignore
└── README.md
