# TaskFlow — Gerenciamento Ágil de Tarefas

Projeto acadêmico de Engenharia de Software: aplicação web simples para organizar tarefas de uma equipe de logística.

## Objetivo
Permitir que a equipe registre tarefas, defina prioridade e acompanhe o fluxo em um quadro Kanban com as colunas **A Fazer**, **Em Progresso** e **Concluído**.

## Escopo inicial
- Criar tarefa (título, descrição e prioridade)
- Visualizar tarefas agrupadas por status
- Mover tarefas entre status
- Excluir tarefas

## Metodologia
Kanban: o trabalho é visualizado em colunas, facilitando identificar tarefas pendentes, em execução e concluídas. O quadro limita a dispersão e melhora a comunicação.

## Requisitos
Python 3.10+.

## Como executar localmente
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python -m src.app
```
Abra http://127.0.0.1:5000.

## Testes
```bash
pytest -q
```

## Mudança de escopo simulada
**Feature adicional:** campo de prioridade (Baixa, Média, Alta). A mudança foi incluída porque o cliente logístico precisa destacar entregas críticas. O Kanban foi atualizado para incluir tarefas com prioridade visual, sem alterar as três colunas principais.

## Estrutura
- `src/`: aplicação Flask e arquivos estáticos/templates
- `tests/`: testes automatizados
- `.github/workflows/`: integração contínua
- `docs/`: documentação e diagramas UML

## Backlog Kanban (10 cards sugeridos)
1. Criar estrutura do projeto — Done
2. Configurar Flask — Done
3. Criar tela Kanban — Done
4. Criar formulário de tarefa — Done
5. Implementar listagem — Done
6. Implementar mudança de status — Done
7. Implementar exclusão — Done
8. Adicionar prioridades — Done (mudança de escopo)
9. Criar testes automatizados — Done
10. Configurar GitHub Actions — Done

## Plano de commits (realize estes commits ao longo da publicação; não são commits já feitos)
1. `chore: create project structure`
2. `docs: add initial README`
3. `feat: add Flask application`
4. `feat: render Kanban task board`
5. `feat: create task form`
6. `feat: move tasks between columns`
7. `feat: delete tasks`
8. `feat: add task priority feature`
9. `test: add automated application tests`
10. `ci: configure GitHub Actions`

## Capturas necessárias para a entrega
Depois de publicar o repositório, tire capturas reais de: Kanban Projects com 10 cards, commits, workflow Actions com testes verdes e aplicação rodando. Não use imagens simuladas como evidência.

## Projeto acadêmico
TechFlow Solutions — cenário fictício de sistema de gestão de tarefas para startup de logística.

### Funcionalidades

- Criar tarefas
- Listar tarefas cadastradas
- Editar tarefas
- Excluir tarefas
- Definir prioridades (baixa, média e alta)
- Organizar tarefas por status

## Tecnologias utilizadas

- Python
- Flask
- HTML e CSS
- Pytest
- Git e GitHub
- GitHub Actions

## Qualidade de software

O projeto utiliza testes automatizados para verificar funcionalidades e reduzir erros. A integração contínua permite automatizar a execução dos testes sempre que alterações são enviadas ao repositório.