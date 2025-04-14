<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Newfy</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
    </head>

<div align="center">

# Newfy 

Ferramenta de captura e armazenamento de notícias estratégicas e dados relevantes publicados em API oficiais associados ao tema. Projeto voltado ao treino de  CRUD Web, Requisitos não funcionais (Linguagem OO, BD Relacional)

### [Repositório do projeto NewFy ](https://github.com/c137santos/FATEC-API-3-SEMESTRE/tree/main)

</div>

## Descrição do projeto

Ferramenta de captura e armazenamento de notícias estratégicas e dados relevantes publicados em API oficiais associados ao tema. O desafio foi criar macânismo para o mapeamento de portais de notícias cadastradas pelo cliente, para a captura do conteúdo veiculado, com um armazenamento desses, formando assim um banco de dados histórico das publicações. 

Além disso, também foi necessário a captura e armazenamento de dados estratégios provindos de API oficiais para fins de comparações futuras. Exemplo, captura de dados relacionados a agricultura, e dados da API de dados climaticos do INPE, por exemplo, uma aferição de se as notícias veiculadas no dia X sobre possível seca correspondia as previsões do INPE daquela data. 

A empresa parceira foi a [GSW Sofware](https://pitsjc.org.br/empresas/gsw/?__cf_chl_tk=Oadw5xOIX8N3p9N3zMLQaaPAovMKruknHwLsSBh0faQ-1744635957-1.0.1.1-yYGVjlGCNsyG42toG2oO76EmA8jZF8RUiam24O2XQ_M). 


## 🚀 Tecnologias Utilizadas

- <i class="fas fa-server"></i> **Backend**: Java com framework Spring Boot  
- <i class="fas fa-database"></i> **Banco de Dados**: PostgreSQL  
- <i class="fas fa-exchange-alt"></i> **ORM**: Hibernate e flyway 
- <i class="fas fa-code"></i> **Frontend**: JavaScript com framework Vue.js  
- <i class="fab fa-docker"></i> **Containerização**: Docker e DevContainer  


## Equipe

Nossa equipe foi batizada de Cerberus, e nesse time assumi o cargo de Scrum Master, e colaborei com os seguites membros:

| Integrante                                                                                                                             | LinkedIn                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clara Santos ![Static Badge](https://img.shields.io/badge/Scrum_master-pink) ![Static Badge](https://img.shields.io/badge/Dev-black)   | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/c137santos/)                  |
| Marília Borgo ![Static Badge](https://img.shields.io/badge/Product_owner-blue) ![Static Badge](https://img.shields.io/badge/Dev-black) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mariliaborgo/)                |
| Matheus Marciano ![Static Badge](https://img.shields.io/badge/Dev-black)                                                               | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matheus-marciano-leite/)      |
| Guilherme Bezerra Junqueira ![Static Badge](https://img.shields.io/badge/Dev-black)                                                    | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-bezerra-a01035170/) |
| Pedro Henrique Lopes de Souza ![Static Badge](https://img.shields.io/badge/Dev-black)                                                  | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pelopes7/)                    |
| Yan Costa Yamim ![Static Badge](https://img.shields.io/badge/Dev-black)                                                                | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yan-yamim-185220278/)         |
| Eduardo da Silva Lima ![Static Badge](https://img.shields.io/badge/Dev-black)                                                          | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/edu-datamarketing/)           |

## Contribuições Individuais

Atuei como dev pontualmente. Nesse projeto, foquei mais na organização da equipe e na comunicação entre os membros. Além disso, também fui responsável por retirar os impedimento que surgiu no caminho, manter o burdown evoluindo e ser TechLead dos integrantes. Ou seja, direcionava para onde as soluções tecnicas deveriam caminhar. 

Por isso, minha primeira tarefa foi desenhar, discutir e implementar o banco de dados. Que foi ponto inicial do desenho do nosso produto. 

Organizei também as documentações do projeto, exemplo do Manual do usuário, documentação dos campos do banco de dados, kanbam na ferramenta do github project, criando cards a partir das userStores, issues, organização de PR e de fluxo de CR.

Foram 78 cards entregues de 17 userStores.

Além disso, aprendi o fechamento de versão por tags e publicação do release.

## Aprendizados e ganhos com o projeto.

O maior aprendizado foi relativo a construção do banco de dados em java spring-boot, usando hibernate e flyway. A configuração de ambos parecia conflitar, por isso tive que entender qual era o escopo de cada um, e como eles se comunicavam.

No `application.properties` direcionei o hibernate para ser um validador das entidades, retirando a responsabilidade de migração automática dele por meio do `spring.jpa.hibernate.ddl-auto=validate`. Este também ficou responsável por ser o `ORM` do projeto, por isso precisei identificar ao hibernate o tipo de banco que o projeto estava utilizando, o `PostgreSQL`, e a URL de conexão com o banco, além do usuário e senha.

```properties
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
```

O flyway ficou responsável por auxiliar nas migrações do banco de dados e guardar os scripts de migração. Para isso, precisei configurar o `application.properties` com as informações do banco de dados, como a URL, usuário e senha. Além disso, também configurei o `flyway.schemas` para indicar qual era o schema que o flyway deveria utilizar.


Além disso, me aprofundei mais nos conhecimentos de docker e o devcontainer, que facilitou muito a configuração do ambiente de desenvolvimento.

O devcontainer não era requisito para essa API, porém, membros do grupo tinham máquinas. Dois membros do grupo tinham windows em máquina própria, outro membro não tinha computador, e usava o da FATEC, ou seja, ele precisava baixar e configurar a máquina inteira toda vez que precisava usar. Outro membro do grupo tinha uma máquina do trabalho, muito fraca, portanto, não podia instalar nada.
O devcontainer foi uma solução para todos esses problemas. Ele é um container docker que tem todas as dependências necessárias para o projeto, e pode ser aberto em qualquer máquina, independente do sistema operacional.

Porém, houve muita resistência de inicio ao uso. Até que os membros perceberam que era mais complexo configurar uma máquina windows do zero, do que abrir o devcontainer.

Durante o desenvolvimento do projeto, o maior aprendizado foi relacionado à construção do banco de dados utilizando Java Spring Boot, Hibernate e Flyway. Inicialmente, houve conflitos na configuração dessas ferramentas, o que exigiu um entendimento detalhado sobre o escopo de cada uma e como elas se comunicam. No arquivo `application.properties`, configurei o Hibernate para atuar como validador das entidades, desativando a migração automática com a propriedade `spring.jpa.hibernate.ddl-auto=validate`. Além disso, defini o Hibernate como o ORM do projeto, especificando o tipo de banco de dados utilizado (PostgreSQL), a URL de conexão, o usuário e a senha. 

O Flyway foi configurado para gerenciar as migrações do banco de dados e armazenar os scripts de migração. Para isso, adicionei as informações do banco no `application.properties` e configurei o `flyway.schemas` para indicar o schema a ser utilizado. Essa abordagem garantiu uma separação clara entre as responsabilidades do Hibernate e do Flyway, evitando conflitos.

Outro aprendizado significativo foi o uso de Docker e DevContainer para facilitar a configuração do ambiente de desenvolvimento. Essa solução foi essencial para superar desafios enfrentados pela equipe, como a diversidade de sistemas operacionais e limitações de hardware. O DevContainer permitiu que todos os membros trabalhassem em um ambiente padronizado, independente do sistema operacional ou das restrições das máquinas utilizadas.

Por fim, o maior ganho técnico foi o desenvolvimento do crawler, que se tornou o núcleo do projeto. Ele foi projetado para buscar portais e URLs no banco de dados, navegar pelas páginas utilizando a biblioteca Crawler4J, salvar os HTMLs coletados em uma pasta específica e processar as notícias com as validações necessárias. O campo `noti_text` foi alterado para o tipo `TEXT` no PostgreSQL, permitindo o armazenamento de textos sem limite de caracteres. O crawler foi configurado para ser executado automaticamente ao iniciar o projeto, com a adição de uma validação de gatilho para controlar sua execução.