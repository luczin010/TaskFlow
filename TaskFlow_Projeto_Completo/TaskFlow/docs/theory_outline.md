# Parte teórica — TaskFlow

## Descrição e escopo
TaskFlow é uma aplicação web básica de gestão de tarefas pensada para uma startup de logística. O escopo inicial contempla cadastrar tarefas com título e descrição, visualizar tarefas por status, mover tarefas entre colunas e excluir tarefas.

## Metodologia ágil
Foi adotado Kanban, que permite visualizar o fluxo de trabalho em colunas e acompanhar o estado das tarefas. O quadro facilita transparência, identificação de bloqueios e priorização.

## Importância da modelagem
Modelar antes ou durante a implementação ajuda a esclarecer funcionalidades, responsabilidades e relações, reduzindo ambiguidades. Diagramas UML dão uma representação visual do comportamento e da estrutura do sistema e facilitam a comunicação entre participantes.

## Casos de uso (descrição para diagrama)
Ator: Membro da equipe. Casos de uso: cadastrar tarefa, visualizar quadro, atualizar status, excluir tarefa. A feature de prioridade estende o cadastro/visualização de tarefa.

## Classes (descrição para diagrama)
Task: id, title, description, priority, status. Operações sugeridas: create, list, update_status, delete. TaskBoard: tasks, group_by_status, add_task, move_task, remove_task.

## Mudança de escopo
A prioridade (Baixa, Média, Alta) foi adicionada após considerar que a operação logística precisa distinguir demandas críticas. O quadro e o README foram ajustados para exibir e documentar essa prioridade.

## Testes automatizados
Pytest verifica o carregamento da página, cadastro, alteração de status e remoção. Os testes usam um arquivo temporário para evitar alterar dados locais do usuário. O workflow GitHub Actions instala dependências e executa `pytest -q` em pushes e pull requests.

## Limitações atuais
O protótipo usa arquivo JSON local e não implementa autenticação, banco de dados compartilhado, permissões, nem sincronização entre usuários. Esses itens poderiam ser evoluções futuras.

## Qualidade e testes

O TaskFlow utiliza testes automatizados com Pytest para verificar o funcionamento da aplicação. Os testes ajudam a identificar falhas nas funcionalidades, garantindo maior confiabilidade e facilitando futuras alterações no código.