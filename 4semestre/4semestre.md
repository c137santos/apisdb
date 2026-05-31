# TerraVision

Sistema web para manipulação e gerenciamento de dados espaciais em fazendas

### Quarto Semestre (2025-1)

O projeto desenvolvido no quarto semestre do curso teve como empresa parceira a Visiona Espacial, empresa especializada em inteligência geoespacial e sensoriamento remoto aplicados à agricultura de precisão.

O problema apresentado consistia na limitação dos modelos de inteligência artificial utilizados pela Visiona para mapeamento de evidências em lavouras (soja, milho, citros, cana-de-açúcar, algodão, entre outras). Esses modelos apresentavam deficiências diretamente relacionadas à falta de amostras de treinamento eficientes. Sem uma ferramenta que permitisse a especialistas visualizar, editar e validar os dados geoespaciais produzidos pela IA, não havia como gerar dados de benchmark de qualidade para retroalimentar e melhorar a performance dos modelos.

Como solução, minha equipe desenvolveu um sistema web com três perfis de usuário — administrador, analista e consultor — para viabilizar a revisão colaborativa de dados geoespaciais de talhões agrícolas. O analista acessa listas de talhões com informações geoespaciais e alfanuméricas, visualiza mapas de problemas evidenciados pela IA via protocolo OGC e pode aprovar, rejeitar ou editar vetorialmente as geometrias diretamente no sistema. O consultor realiza o cadastro de áreas via upload de arquivo GeoJSON, informando cultura, produtividade, tipo de solo e localização, e acompanha dashboards com indicadores quantitativos e qualitativos da evolução das análises. O administrador acumula todas as funções mais o cadastro de usuários.

[Repositório GitHub](https://github.com/c137santos/FATEC-API-4-SEMESTRE-PARENT)

#### Tecnologias Utilizadas

As seguintes tecnologias foram utilizadas nesse projeto:

* Java com Spring Boot - framework utilizado no back-end para construção dos endpoints REST e implementação da lógica de negócio;
* Spring Security - utilizado para implementação de autenticação e controle de autorização por perfil de usuário (administrador, analista e consultor);
* PostgreSQL com PostGIS - banco de dados relacional com extensão geoespacial utilizado para armazenamento e manipulação de geometrias MultiPolygon;
* Hibernate e Flyway - ORM e controle de migrações do banco de dados;
* JTS (Java Topology Suite) - biblioteca Java utilizada para processamento de geometrias GeoJSON e conversão para o tipo MultiPolygon persistido no PostGIS;
* Vue.js - framework JavaScript utilizado no front-end para construção dos componentes de cadastro e visualização de dados;
* Leaflet - biblioteca JavaScript utilizada no front-end para renderização de mapas interativos e visualização das geometrias geoespaciais dos talhões;
* Docker e DevContainer - utilizados para padronização do ambiente de desenvolvimento da equipe.

#### Contribuições Pessoais

Nesse projeto atuei como desenvolvedora, com foco principal no back-end. Fui responsável pela criação e manutenção de endpoints REST para cadastro, consulta e listagem de talhões, fazendas e resultados de análises. Implementei a lógica de cálculo da porcentagem de edição entre resultados de IA e intervenções do QA, além de participar do refatoramento do banco de dados para maior eficiência e organização das informações.

Também desenvolvi um serviço para processamento e persistência de geometrias MultiPolygon: o serviço recebe dados em formato GeoJSON, processa a geometria utilizando a biblioteca JTS e persiste as informações no banco com suporte PostGIS, convertendo as entidades salvas em DTOs para retorno à aplicação. No front-end, desenvolvi o componente de formulário e a view para cadastro de talhões, bem como a interface de cadastro de resultados de AI enhancement.

#### Hard Skills

Exercitei as seguintes hard skills durante esse projeto:

* Java - uso com autonomia;
* Spring Boot - uso com autonomia;
* PostgreSQL / PostGIS - uso com autonomia;
* JTS (Java Topology Suite) - uso com autonomia;
* Vue.js - uso com autonomia;
* Docker - uso com autonomia.

#### Soft Skills

Nesse projeto exercitei meu aprendizado rápido ao trabalhar pela primeira vez com dados geoespaciais e geometrias complexas como MultiPolygon. Sem experiência prévia em geoprocessamento, pesquisei de forma independente sobre sistemas de referência de coordenadas (CRS), a biblioteca JTS e a extensão PostGIS para implementar corretamente o serviço de persistência de geometrias, o que me permitiu entregar a funcionalidade dentro do prazo da sprint.

Também utilizei organização e atenção a detalhes ao estruturar o repositório no padrão "parent" com submódulos separados para frontend e backend. Essa abordagem, incomum em relação aos semestres anteriores, exigiu cuidado extra na configuração de versionamento e integração entre os módulos para garantir que toda a equipe conseguisse trabalhar no projeto sem problemas de ambiente.

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
