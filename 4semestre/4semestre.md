<div align="center">

# TerraVision 

Sistema WEB para manipulação e gerenciamento de dados espaciais em Fazendas

### [Repositório do projeto TerraVision ](https://github.com/c137santos/FATEC-API-4-SEMESTRE-PARENT/tree/main)

</div>

## Descrição do projeto

## Descrição do projeto

O TerraVision é um sistema web desenvolvido para manipulação, gerenciamento e análise de dados espaciais, com foco em aplicações agrícolas e ambientais. O objetivo principal do projeto foi criar uma plataforma capaz de visualização, edição e análise de dados em tempo real dos dados geoespeciais.

A aplicação foi desenhada para atender diferentes perfis de usuários: administradores, analistas e consultores. O que nos forçou a trabalhar com permissionamento por usuário e feature.

O TerraVision utiliza Java com Spring Boot no backend, PostgreSQL como banco de dados relacional, Hibernate e Flyway para ORM e migração, e Vue.js no frontend. A infraestrutura foi padronizada com Docker e DevContainer, não exigidos, mas implementados. O sistema também conta com documentação completa, incluindo manual do usuário, guia de instalação, documentação da API e modelagem do banco de dados.

A empresa parceira foi a [GSW Sofware](https://pitsjc.org.br/empresas/gsw/?__cf_chl_tk=Oadw5xOIX8N3p9N3zMLQaaPAovMKruknHwLsSBh0faQ-1744635957-1.0.1.1-yYGVjlGCNsyG42toG2oO76EmA8jZF8RUiam24O2XQ_M). 


## 🚀 Tecnologias Utilizadas

- <i class="fas fa-server"></i> **Backend**: Java com Spring Boot  
- <i class="fas fa-database"></i> **Banco de Dados**: PostgreSQL  
- <i class="fas fa-exchange-alt"></i> **ORM/Migração**: Hibernate e Flyway  
- <i class="fas fa-code"></i> **Frontend**: Vue.js (JavaScript)  
- <i class="fab fa-docker"></i> **Containerização/Ambiente**:

## Equipe

Nossa equipe foi batizada de Cerberus, e nesse time assumi o cargo de Scrum Master, e colaborei com os seguites membros:

| Integrante                                                                                                                             | LinkedIn                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Yan Yamim ![Static Badge](https://img.shields.io/badge/Product_owner-blue) ![Static Badge](https://img.shields.io/badge/Dev-black)   | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yan-yamim-185220278/)                  |
| Matheus Marciano ![Static Badge](https://img.shields.io/badge/Scrum_master-pink) ![Static Badge](https://img.shields.io/badge/Dev-black) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matheus-marciano-leite/)                |
| Maria Clara Santos ![Static Badge](https://img.shields.io/badge/Dev-black)                                                    | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/c137santos/) |
| Pedro Henrique Lopes de Souza ![Static Badge](https://img.shields.io/badge/Dev-black)                                                  | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pelopes7/)                    |
| Marília Borgo ![Static Badge](https://img.shields.io/badge/Dev-black)                                                          | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mariliaborgo/)           |
   |

## Contribuições Individuais


## Síntese das Contribuições Individuais

Contribui principalmente no backend. Responsável pela criação e manutenção de endpoints REST para cadastro, consulta e listagem de talhões, fazendas e resultados de análises, além de implementar lógicas específicas como o cálculo de porcentagem de edição entre resultados de IA e QA. 

Também participei do refatoramento do banco de dados para garantir maior eficiência e organização das informações, bem como na integração das funcionalidades backend com o restante da aplicação. Essas atividades exigiram domínio de Java, Spring Boot, modelagem relacional e boas práticas de desenvolvimento de APIs.

Além do backend, também contribuí no frontend do sistema, desenvolvendo o componente de formulário e a view para cadastro de talhões, bem como a interface para cadastro de resultados de AI enhancement. Essas entregas ajudaram a integrar as funcionalidades do backend à experiência do usuário, garantindo um fluxo completo de cadastro e visualização de dados na aplicação.


### Dificuldade

Minhas principais dificuldades no projeto TerraVision estiveram relacionadas à exigência de estruturar o repositório no GitHub utilizando o padrão "parent", separando os projetos de frontend e backend em submódulos distintos. Essa abordagem, embora traga benefícios para a organização e manutenção do código, demandou um esforço adicional para configurar corretamente os ambientes, garantir o versionamento adequado e integrar as diferentes partes do sistema.

Outro desafio significativo foi o cadastro e manipulação de dados geoespaciais, especialmente ao lidar com resultados no formato MultiPolygon geometry. O processamento de dados geográficos exige a definição de parâmetros específicos, como o sistema de referência de coordenadas (CRS), que nem sempre são triviais de identificar ou configurar corretamente. Essas questões técnicas exigiram pesquisa adicional e testes para garantir a integridade e a precisão dos dados de geoprocessamento no sistema.

## Aprendizados e ganhos com o projeto

Durante o desenvolvimento do TerraVision, aprofundei meus conhecimentos na configuração e utilização do PostgreSQL com a extensão PostGIS, fundamental para o armazenamento e manipulação de dados geográficos. Exigindo exigiam o processamento de geometrias complexas, como MultiPolygons, para registrar áreas de ocorrência de daninhas a partir das marcações feitas pelo QA.

Um exemplo prático desse aprendizado foi a implementação da lógica para salvar essas marcações no banco de dados. Desenvolvi um serviço responsável por receber os dados em formato GeoJSON, processar a geometria MultiPolygon utilizando a biblioteca JTS (Java Topology Suite) e persistir as informações no banco relacional com suporte geoespacial. O serviço também converte as entidades salvas em DTOs adequados para retorno à aplicação, garantindo a integridade e a precisão dos dados geográficos.

Esse processo me permitiu compreender melhor os desafios do geoprocessamento, como a necessidade de definir corretamente o sistema de referência de coordenadas (CRS) e a importância de validar a estrutura dos dados recebidos. Além disso, o contato direto com a integração entre backend Java, PostGIS e manipulação de GeoJSON ampliou minha visão sobre soluções para sistemas que dependem


```
@Service
public class DaninhasService {

    @Autowired
    private DaninhaRepository daninhaRepository;

    @Autowired
    private GeoJsonProcessor geoJsonProcessor;

    public List<DaninhaDTO> registerDaninhas(JsonNode features, Resultado resultado) throws org.locationtech.jts.io.ParseException{
        List<DaninhaDTO> daninhas = new ArrayList<>();
        if (features != null && features.isArray()) {
            for (JsonNode feature : features) {
                JsonNode geometryNode = feature.get("geometry");
                if (geometryNode != null && "MultiPolygon".equals(geometryNode.get("type").asText())) {
                    String geometryJson = geometryNode.toString();
                    MultiPolygon geometry = geoJsonProcessor.processGeometry(geometryJson);
                    Daninha daninhaDaVez = new Daninha(null, geometry, resultado);
                    daninhaRepository.save(daninhaDaVez);
                    DaninhaDTO daninhaDTO = this.convertToGeoDTO(daninhaDaVez);
                    daninhas.add(daninhaDTO);
                }
            }
        }
        return daninhas;
    }
    private DaninhaDTO convertToGeoDTO(Daninha daninha) {
        ArrayNode geoJson = geoJsonProcessor.extractCoordinates(daninha.getGeom());
        return new DaninhaDTO(geoJson);
    }
}

```

Como esta exposto nesse exemplo de função acima. 


</div>