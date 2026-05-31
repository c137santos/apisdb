# Treelaw

Sistema de acompanhamento e análise de dados climáticos por região

### Segundo Semestre (2024-1)

O projeto desenvolvido no segundo semestre do curso teve como empresa parceira a própria FATEC São José dos Campos. Os requisitos foram apresentados pela Professora Juliana (M2) e pelo Professor Mineda (P2), que assumiram o papel de clientes finais do projeto.

Nosso cliente dessa API foi a FATEC, representado pela Profª.Juliana.

O problema apresentado consistia na dificuldade de setores dependentes de dados climáticos — como agricultura e planejamento ambiental — em receber, validar e analisar registros provenientes de diferentes estações meteorológicas. Os dados chegavam em formatos variados e frequentemente continham registros suspeitos, como temperaturas fora dos padrões aceitáveis, que precisavam de revisão manual sem qualquer ferramenta de suporte.

Como solução, minha equipe desenvolveu um sistema desktop em Java que recebe arquivos CSV de estações meteorológicas, valida automaticamente os registros, separa os dados suspeitos para revisão manual e gera relatórios de médias de variáveis climáticas por cidade e período, com periodicidade horária.

[Repositório GitHub](https://github.com/c137santos/FATEC-API-2-SEMESTRE)

#### Tecnologias Utilizadas

As seguintes tecnologias foram utilizadas nesse projeto:

* Java - linguagem de programação utilizada tanto no back-end quanto no front-end da aplicação desktop;
* JavaFX - plataforma utilizada para desenvolvimento da interface gráfica do usuário;
* JDBC - utilizado para comunicação direta com o banco de dados relacional;
* PostgreSQL - banco de dados relacional utilizado para armazenamento dos registros climáticos e das configurações de estações.

#### Contribuições Pessoais

Nesse projeto atuei como desenvolvedora. Fui responsável pelo desenvolvimento da funcionalidade de cadastro manual de registros climáticos, criando a interface e a lógica de validação que garantia a existência de tipo de unidade, cidade, hora e estação antes da persistência no banco. Também implementei a tela e a lógica de criação de estações de monitoramento e desenvolvi o relatório de situação com exibição das últimas médias registradas por cidade e suas respectivas unidades de medida.

Além disso, padronizei as conexões com o banco de dados via JDBC ao longo do projeto, abstraindo a lógica de conexão e desconexão em uma classe utilitária, o que reduziu a complexidade e aumentou a consistência nas interações com o banco.

#### Hard Skills

Exercitei as seguintes hard skills durante esse projeto:

* Java - uso com autonomia;
* JavaFX - uso com autonomia;
* JDBC - uso com autonomia;
* PostgreSQL - uso com autonomia.

#### Soft Skills

Nesse projeto desenvolvi minha adaptabilidade ao trabalhar como desenvolvedora fullstack em Java Desktop, plataforma com a qual tinha menor afinidade. Apesar de minha preferência pelo desenvolvimento back-end, entreguei funcionalidades completas de interface e lógica de negócio, o que exigiu aprendizado contínuo ao longo das sprints.

Também exercitei minha comunicação ao perceber que algumas mensagens minhas não eram interpretadas conforme esperado pelos demais membros, gerando pequenos conflitos. A partir dessa percepção, passei a verificar o entendimento compartilhado antes de tomar decisões técnicas, o que contribuiu para um ambiente de trabalho mais alinhado nas sprints seguintes.

## Contribuições Individuais

Como desenvolvedora, atuei em diversas frentes do projeto, contribuindo diretamente para a implementação de funcionalidades essenciais. Fui responsável pelo desenvolvimento do cadastro manual de registros, criação de estações de monitoramento e implementação do relatório de situação com unidades de medida. Também atuei na padronização das conexões com o banco de dados via JDBC, garantindo maior estabilidade e organização do código.

Além disso, realizei correções de bugs em relatórios situacionais, contribuí para a diminuição da complexidade na conexão com o banco de dados e participei ativamente das sprints, colaborando com a entrega de funcionalidades e melhorias contínuas. Essas experiências permitiram aprimorar minhas habilidades técnicas em Java Desktop e modelagem de banco de dados relacional.

#### Dificuldade

Durante o desenvolvimento deste projeto, evoluí consideravelmente no domínio da linguagem Java, no contexto de aplicações desktop e integração com bancos de dados relacionais via JDBC. 

Além dos desafios técnicos, enfrentei dificuldades relacionadas à comunicação com a equipe. Em alguns momentos, acreditei que estava sendo clara e razoável nas discussões, mas percebi posteriormente que nem sempre minha mensagem foi compreendida como eu esperava, o que gerou alguns conflitos.

Outro ponto de dificuldade foi a gestão de repositórios no GitHub. Tive problemas para acessar o repositório da empresa, pois meu usuário já estava vinculado a outra organização, o que impedia minha entrada no grupo e, consequentemente, afetava o funcionamento do Copilot. Essa situação reforçou a importância de entender as configurações de permissões e organizações em plataformas de versionamento, além de lidar com questões técnicas e administrativas.

Por fim, atuei de forma fulltask, contribuindo tanto no backend quanto no frontend do sistema. Apesar de ter mais afinidade e potencial para trabalhar com backend, o desenvolvimento do frontend em Java foi um desafio adicional, pois era uma área mais nova para mim. Essa experiência exigiu adaptação e aprendizado contínuo para entregar soluções completas e integradas ao

#### Aprendizados e ganhos com o projeto

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