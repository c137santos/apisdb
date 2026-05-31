# Jibóia

Sistema ETL para consolidação e análise de dados de projetos do Jira

### Quinto Semestre (2025-2)

O projeto desenvolvido no quinto semestre do curso teve como empresa parceira a Necto Systems, empresa brasileira especializada em soluções de software para gestão empresarial.

O problema apresentado consistia na dificuldade de gestores e líderes de equipe em obter uma visão consolidada do andamento de seus projetos gerenciados pelo Jira. Embora o Jira armazene dados detalhados sobre issues, horas trabalhadas e membros envolvidos, a plataforma não oferece nativamente dashboards analíticos que cruzem métricas entre projetos, calculem custos por desenvolvedor ou exibam indicadores de performance como taxa de conclusão e tempo médio de resolução — o que exigia esforço manual constante para extrair e interpretar esses dados.

Como solução, minha equipe desenvolveu o Jibóia, um sistema de ETL que consome dados diretamente da API do Jira, os transforma e os consolida em um data warehouse com modelagem dimensional no esquema Snowflake. A plataforma oferece dashboards com indicadores de esforço por projeto e desenvolvedor, custo total de horas, movimentação de issues e burndown, com controle de acesso por perfil (administrador, gerente, líder e membro de equipe).

[Repositório GitHub](https://github.com/c137santos/FATEC-API-5-SEMESTRE)

#### Tecnologias Utilizadas

As seguintes tecnologias foram utilizadas nesse projeto:

* Python com Django - linguagem e framework utilizados no back-end para construção da API REST, serviços de ETL e agendamento de cron jobs de integração com o Jira;
* PostgreSQL - banco de dados relacional utilizado como data warehouse para armazenamento do modelo dimensional;
* Django ORM - utilizado para mapeamento das entidades e operações de persistência no data warehouse;
* Vue.js 3 com TypeScript - framework e linguagem utilizados no front-end para construção dos dashboards e componentes de visualização;
* Vuetify 3 - biblioteca de componentes UI utilizada no front-end;
* Chart.js / vue-chartjs - utilizados para renderização dos gráficos e dashboards analíticos;
* Docker e Docker Compose - utilizados para containerização e orquestração dos serviços em desenvolvimento e produção;
* GitHub Actions - utilizado para automação do pipeline de CI/CD, incluindo testes automatizados e análise de qualidade de código;
* SonarCloud - utilizado para monitoramento contínuo de qualidade de código, cobertura de testes e detecção de code smells;
* pytest e pytest-cov - utilizados para execução e cobertura dos testes automatizados do back-end;
* AWS - utilizado para deploy da aplicação em ambiente de produção.

#### Contribuições Pessoais

Nesse projeto atuei como desenvolvedora, com responsabilidade sobre a área de DevOps/testes e a modelagem dimensional do data warehouse.

Na parte de DevOps, configurei o pipeline de CI/CD com GitHub Actions com três workflows: integração contínua do back-end em Python (`python-app-ci.yml`), deploy automatizado (`deploy.yml`) e coleta de estatísticas de pull requests (`pr-stats.yml`). Integrei o SonarCloud ao repositório para monitoramento contínuo de qualidade, cobertura de testes e detecção de vulnerabilidades, definindo quality gates mínimos para aprovação de PRs. Também criei a documentação do padrão de testes do back-end para padronizar a escrita de testes pela equipe.

Na modelagem dimensional, projetei o data warehouse no esquema Snowflake com duas tabelas fato: `FatoIssue`, responsável por armazenar métricas consolidadas de issues (total, esforço em horas, tempo médio de resolução) com chaves para as dimensões `DimProjeto`, `DimIssueType`, `DimStatus` e `DimTempo`; e `FatoSnapshotProjeto`, que captura o estado do projeto ao longo do tempo para análises históricas. Essa modelagem foi o maior desafio técnico do projeto, pois exigiu definir corretamente a granularidade dos fatos e as relações entre dimensões para que as queries analíticas dos dashboards funcionassem com eficiência.

#### Hard Skills

Exercitei as seguintes hard skills durante esse projeto:

* Python - uso com autonomia;
* Django - uso com autonomia;
* PostgreSQL - uso com autonomia;
* Vue.js - uso com autonomia;
* Docker - uso com autonomia;
* GitHub Actions - uso com autonomia;
* SonarCloud / SonarQube - uso com autonomia;
* Modelagem dimensional (Snowflake schema) - uso com autonomia.

#### Soft Skills

Nesse projeto exercitei minha capacidade de aprendizado autônomo ao assumir a responsabilidade pela modelagem dimensional, área que ia além do escopo técnico do meu dia a dia profissional. Para projetar o esquema Snowflake com as tabelas fato e dimensões corretas, precisei estudar de forma independente os padrões de data warehouse, entender a diferença entre granularidade de fato transacional e snapshot, e validar as decisões de modelagem com o restante da equipe antes da implementação — o que exigiu tanto pesquisa técnica quanto clareza na comunicação das escolhas feitas.

Também utilizei minha proatividade e senso de responsabilidade ao estruturar os padrões de qualidade do projeto desde a Sprint 1: defini os quality gates no SonarCloud, documentei o padrão de testes e configurei os pipelines de CI antes que o time começasse a desenvolver as funcionalidades principais, evitando o acúmulo de dívida técnica ao longo das sprints.
