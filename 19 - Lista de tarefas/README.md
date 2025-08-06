
# 🧠 Lista de Tarefas

Este projeto consiste em **duas implementações** de um gerenciador de tarefas com suporte a comandos interativos, histórico de ações, persistência em JSON e lógica para desfazer/refazer. As duas versões compartilham as mesmas funcionalidades principais, mas diferem na maneira como os comandos são tratados e como o fluxo do programa é estruturado.

---

## ✨ Funcionalidades Comuns

- ✅ Adicionar tarefas manualmente
- 📋 Listar tarefas
- 🔄 Desfazer última tarefa adicionada
- ⏩ Refazer tarefa desfeita
- 🧼 Limpar terminal (Windows)
- 💾 Salvar tarefas automaticamente em arquivo `.json`
- 📁 Recuperar tarefas salvas ao iniciar

---

## Versão 1 — COM IFS

### Descrição

Esta versão utiliza uma estrutura de controle `if/elif` para identificar e executar comandos digitados pelo usuário.

## Versão 2 — SEM IFS

### Descrição

Essa abordagem substitui a estrutura condicional por um **dicionário de comandos**, onde cada chave representa um comando e o valor correspondente é uma função `lambda`.