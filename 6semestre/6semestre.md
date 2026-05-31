# Thunderstone

Sistema de análise de mercado e criticidade para redes elétricas de distribuição

### Sexto Semestre (2026-1)

O projeto desenvolvido no sexto semestre do curso teve como empresa parceira a Tecsys, empresa especializada em soluções de sensoriamento e telemetria para redes elétricas de distribuição.

O problema apresentado consistia na necessidade de dimensionar o potencial de mercado para instalação de sensores de falta em redes de média e alta tensão no Brasil. A Tecsys precisava de um sistema capaz de processar dados regulatórios da ANEEL — como indicadores de continuidade (DEC e FEC), perdas e dados geoespaciais de distribuidoras — e transformá-los em análises de mercado que identificassem as regiões com maior criticidade e maior potencial de adoção de sua solução de sensoriamento.

Como solução, minha equipe desenvolveu o Thunderstone, uma plataforma de análise que ingere dados abertos da ANEEL (arquivos Geodatabase da BDGD e CSVs de DEC/FEC), processa as camadas geoespaciais e regulatórias via pipeline ETL assíncrono com Celery e Redis, e persiste os dados processados no MongoDB. A plataforma calcula índices de criticidade por conjunto elétrico, dimensiona a extensão de média tensão (TAM), classifica os conjuntos pelo índice SAM — que cruza extensão de rede, criticidade e presença de religadores — e exibe dashboards analíticos e mapa de calor georreferenciado para suporte à decisão comercial da Tecsys.

[Repositório GitHub](https://github.com/c137santos/FATEC-API-6-SEMESTRE)

#### Tecnologias Utilizadas

As seguintes tecnologias foram utilizadas nesse projeto:

* Python com FastAPI - linguagem e framework utilizados no back-end para construção dos endpoints REST da API de ingestão de dados;
* Celery com Redis - utilizados para processamento assíncrono e distribuído das tarefas de ETL, como download, descompactação e processamento em paralelo dos arquivos GDB;
* MongoDB - banco de dados NoSQL utilizado para persistência dos dados regulatórios processados da ANEEL (BDGD, DEC e FEC);
* PostgreSQL - banco de dados relacional utilizado para armazenamento de usuários, credenciais e dados de autenticação;
* Fiona, Shapely e pyproj - bibliotecas Python utilizadas para leitura de arquivos Geodatabase, processamento de geometrias e reprojeção de coordenadas para o padrão EPSG:4326;
* Vue.js - framework JavaScript utilizado no front-end para construção dos dashboards e visualizações analíticas;
* Docker e Docker Compose - utilizados para containerização e orquestração dos serviços da aplicação;
* Google Colab / Jupyter - utilizados para prototipagem e validação dos cálculos analíticos (Score de Criticidade, SAM, TAM e análise de DEC/FEC).

#### Contribuições Pessoais

Nesse projeto atuei como desenvolvedora, com foco principal na construção do pipeline ETL assíncrono de ingestão dos dados da ANEEL.

Implementei o endpoint `/etl/download-gdb`, responsável por receber a URL de um arquivo Geodatabase da BDGD e enfileirar a task Celery `task_download_gdb`. Essa task realiza o download via streaming com httpx, valida se o arquivo baixado é um ZIP válido, e encadeia automaticamente a próxima etapa do pipeline via assinatura Celery, aplicando backoff exponencial nas retentativas em caso de falha de rede.

A etapa seguinte — `task_descompact_gdb` — descompacta o ZIP, localiza o `.gdb` interno, valida o schema de todas as camadas obrigatórias (CTMT, CONJ e SSDMT) e dispara um `chord` Celery com as tasks de processamento em paralelo. A camada SSDMT, por ser a de maior volume de geometrias, suporta paralelismo por chunks configurável via variável de ambiente, permitindo processar arquivos de distribuidoras de grande porte sem comprometer a memória dos workers.

Desenvolvi as tasks `task_processar_ctmt` e `task_processar_conj`, responsáveis pela limpeza, validação e estruturação dos registros de conjuntos elétricos (com dados de energia mensal e perdas por classe tarifária) e sua persistência no MongoDB. Também implementei o endpoint `/etl/load-dec-fec` e as tasks `task_load_dec_fec_realizado` e `task_load_dec_fec_limite`, que fazem o download de CSVs da ANEEL em codificação latin-1, processam os dados em chunks de 10.000 registros e realizam bulk upsert no MongoDB — garantindo idempotência nas execuções repetidas.

#### Hard Skills

Exercitei as seguintes hard skills durante esse projeto:

* Python - uso com autonomia;
* FastAPI - uso com autonomia;
* Celery - uso com autonomia;
* Redis - uso com autonomia;
* MongoDB - uso com autonomia;
* Fiona / Shapely / pyproj - uso com autonomia;
* Docker - uso com autonomia.

#### Soft Skills

Nesse projeto exercitei minha capacidade de decomposição de problemas complexos ao projetar o pipeline ETL em etapas encadeadas e distribuídas. Os arquivos GDB da BDGD podem ter gigabytes e camadas com dezenas de milhares de geometrias, o que exigiu pensar a solução em partes independentes e combináveis — download, validação, extração e processamento paralelo por layer — em vez de um processo monolítico. Essa decomposição resultou na implementação do `chord` Celery, que permitiu processar as camadas CTMT, CONJ e SSDMT em paralelo e agregar os resultados de forma confiável.

Também exercitei atenção à resiliência e observabilidade ao construir cada task com logging estruturado, backoff exponencial para falhas de rede e validação de schema antecipada — decisões que evitam que um arquivo mal-formado da ANEEL quebre silenciosamente o pipeline e facilitam o diagnóstico de falhas em produção.
