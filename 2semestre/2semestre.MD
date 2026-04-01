<div align="center">

# Treelaw

## Sistema de acompanhamento de clima por região

</div>


### [Repositório do projeto Treelaw ](https://github.com/c137santos/FATEC-API-2-SEMESTRE)



## Descrição do Projeto

O projeto Treelaw foi desenvolvido com o objetivo de facilitar o acompanhamento e análise do clima por região, atendendo especialmente demandas de setores que dependem de informações climáticas para o planejamento de suas atividades, como a agricultura. Reconhecendo a importância de dados precisos sobre temperatura, umidade e outras variáveis, o sistema foi projetado para receber arquivos CSV provenientes de diferentes estações de monitoramento, validar seu conteúdo e prover relatórios detalhados.

Implementamos funcionalidades para o carregamento e validação de arquivos CSV, tratando automaticamente registros suspeitos (como temperaturas fora de padrões aceitáveis), que são armazenados separadamente para revisão manual. O sistema permite o gerenciamento de estações, cidades e unidades de medida, possibilitando a visualização e edição dessas informações. Também desenvolvemos relatórios de valores médios das variáveis climáticas por cidade e período, com periodicidade horária, além de relatórios de situação que apresentam as últimas médias registradas para cada cidade. O tratamento de registros suspeitos inclui opções para revisão, alteração e integração à base principal ou exclusão definitiva, garantindo a

## 🚀 Tecnologias Utilizadas

- <i class="fas fa-server"></i> **Backend**: Java Desktop com conexão ao banco de dados via JDBC  
- <i class="fas fa-database"></i> **Banco de Dados**: Modelo Relacional  
- <i class="fas fa-code"></i> **Frontend**: Java Desktop  
- <i class="fab fa-git"></i> **Controle de Versão**:

### Equipe


| Integrante | LinkedIn |
|------|----------|
| Vinícius Augusto da Silva Monteiro ![Static Badge](https://img.shields.io/badge/Dev-black) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/viniciusvasm/) |
| Ricardo Campos ![Static Badge](https://img.shields.io/badge/Product_owner-blue) ![Static Badge](https://img.shields.io/badge/Dev-black) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ricardo-campos-ba56091b5/) |
| Elbert Jean ![Static Badge](https://img.shields.io/badge/Dev-black) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/elbert-jean-1757b017b/) |
| Isaque Souza ![Static Badge](https://img.shields.io/badge/Dev-black) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/isaque-souza-6760b8270/) |
| Maria Clara ![Static Badge](https://img.shields.io/badge/Dev-black) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/c137santos/) |
| Marília Borgo ![Static Badge](https://img.shields.io/badge/Scrum_master-pink) ![Static Badge](https://img.shields.io/badge/Dev-black) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mariliaborgo/) |
| Paloma Soares ![Static Badge](https://img.shields.io/badge/Dev-black) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/paloma-soares-83a949208/) |

## Contribuições Individuais

Como desenvolvedora, atuei em diversas frentes do projeto, contribuindo diretamente para a implementação de funcionalidades essenciais. Fui responsável pelo desenvolvimento do cadastro manual de registros, criação de estações de monitoramento e implementação do relatório de situação com unidades de medida. Também atuei na padronização das conexões com o banco de dados via JDBC, garantindo maior estabilidade e organização do código.

Além disso, realizei correções de bugs em relatórios situacionais, contribuí para a diminuição da complexidade na conexão com o banco de dados e participei ativamente das sprints, colaborando com a entrega de funcionalidades e melhorias contínuas. Essas experiências permitiram aprimorar minhas habilidades técnicas em Java Desktop e modelagem de banco de dados relacional.


## Dificuldade

Durante o desenvolvimento deste projeto, evoluí consideravelmente no domínio da linguagem Java, no contexto de aplicações desktop e integração com bancos de dados relacionais via JDBC. 

Além dos desafios técnicos, enfrentei dificuldades relacionadas à comunicação com a equipe. Em alguns momentos, acreditei que estava sendo clara e razoável nas discussões, mas percebi posteriormente que nem sempre minha mensagem foi compreendida como eu esperava, o que gerou alguns conflitos.

Outro ponto de dificuldade foi a gestão de repositórios no GitHub. Tive problemas para acessar o repositório da empresa, pois meu usuário já estava vinculado a outra organização, o que impedia minha entrada no grupo e, consequentemente, afetava o funcionamento do Copilot. Essa situação reforçou a importância de entender as configurações de permissões e organizações em plataformas de versionamento, além de lidar com questões técnicas e administrativas.

Por fim, atuei de forma fulltask, contribuindo tanto no backend quanto no frontend do sistema. Apesar de ter mais afinidade e potencial para trabalhar com backend, o desenvolvimento do frontend em Java foi um desafio adicional, pois era uma área mais nova para mim. Essa experiência exigiu adaptação e aprendizado contínuo para entregar soluções completas e integradas ao

## Aprendizados e ganhos com o projeto

Ao longo do projeto, evoluí significativamente no domínio da linguagem Java, especialmente no desenvolvimento de aplicações desktop e na integração com bancos de dados relacionais utilizando JDBC. Esse processo de aprendizado prático me proporcionou maior segurança para lidar com desafios técnicos e implementar soluções mais eficientes.

Outro ponto importante foi o contato mais direto com os conceitos de Programação Orientada a Objetos (POO), já que o Java é uma linguagem fortemente baseada nesse paradigma. Trabalhar com POO me permitiu estruturar melhor o código, organizar as funcionalidades em classes e métodos, e compreender a importância de princípios como encapsulamento, herança e polimorfismo no desenvolvimento de sistemas mais robustos e manuteníveis.

Para inserção de registro manual inspirado em POO, a função precisava garantir a existência de tipo de unidade, cidade, hora e estação.

```
public class InsertData {

    ObservableList<String> hours = FXCollections.observableArrayList();

    String sql;

    @FXML
    private DatePicker datePickerInitial;

    @FXML
    private TextField valueResp;

    @FXML
    private ComboBox<String> cbDataType;

    @FXML
    private ComboBox<String> unitData;

    @FXML
    private ComboBox<String> cityData;

    @FXML
    private ComboBox<String> hourData;

    @FXML
    private ComboBox<String> stationData;

    @FXML
    private Button btRegister;

    @FXML
    private void initialize() {
        Metrics metrics = new Metrics();
        metrics.loadMetrics();
        cbDataType.setItems(metrics.getMetrics());
        Units units = new Units();
        units.loadUnits();
        unitData.setItems(units.getUnitsNames());
        Cities cities = new Cities();
        cityData.setItems(cities.getAllNamesCities());
        loadHoursComboBox();
        hourData.setItems(hours);

        datePickerInitial.setValue(LocalDate.now());
        cbDataType.setValue("Temperatura");
        unitData.setValue("ºC");
        hourData.setValue("00");
    }


    @FXML
    private void insertStationByCities(ActionEvent event) {
        Stations st = new Stations();
        List<String> stations = st.getAllCodStations(cityData.getValue());
        ObservableList<String> stationList = FXCollections.observableArrayList(stations);
        stationData.setItems(stationList);
    }

    @FXML
    public void btRegisterData(ActionEvent event) {

        if (cbDataType.getValue() == null || unitData.getValue() == null || cityData.getValue() == null || stationData.getValue() == null || datePickerInitial.getValue() == null || hourData.getValue() == null || valueResp.getText() == null){
            return;
        }

        formatSqlInsert();
        saveSqlInsert();

        }

    public void formatSqlInsert() {

        LocalDate data = datePickerInitial.getValue();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        String dataFormatada = data.format(formatter);

        String hourFormat = hourData.getValue() + "00";

        DataMeasurement dm = new DataMeasurement(cbDataType.getValue(), unitData.getValue(), dataFormatada, hourFormat, valueResp.getText(), 0);

        Cities cities = new Cities();
        City city = cities.searchCity(cityData.getValue());

        Stations st = new Stations();
        Station station = st.searchStation(stationData.getValue(), city.getIdCidade());

        Metrics metrics = new Metrics();
        metrics.loadMetrics();

        sql = dm.toInsertSql(station.getIdEstacao(), metrics);

    }

    public void saveSqlInsert() {
        DbConnection db = new DbConnection();
        db.executeNotReturn(sql);
        db.Desconnect();
        Stage stage = (Stage) cityData.getScene().getWindow();
        stage.close();
    }

    private void loadHoursComboBox() {
        hours.add("00");
        for (int i = 1; i < 24; i++) {
            hours.add(Integer.toString(i));
        }
    }

}
```

Além do crescimento técnico, também desenvolvi habilidades interpessoais, aprimorando minha comunicação com a equipe. Passei a me expressar de forma mais clara e a buscar sempre o alinhamento entre todos os envolvidos, o que contribuiu para um ambiente de trabalho mais colaborativo e produtivo. Esses aprendizados foram fundamentais para meu desenvolvimento como profissional e para o sucesso do