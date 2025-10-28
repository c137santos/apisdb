<div align="center">

# PBLTex 

Sistema educacional de gestão e acompanhamento de scores de alunos

### [Repositório do projeto PBLTex](https://github.com/c137santos/FATEC-API-1-SEMESTRE?tab=readme-ov-file)

</div>


## Descrição do Projeto

O objetivo deste projeto foi desenvolver uma solução computacional para gestão educacional voltado ao acompanhamento de scores de alunos.

No que diz respeito aos requisitos funcionais, implementamos o controle de turmas, grupos de alunos e cadastro de alunos, além de permitir a importação de dados desses alunos.

Também desenvolvemos funcionalidades para gerenciar os ciclos de entrega, importar scores parciais relacionados a cada ciclo, configurar parâmetros globais do sistema e exportar dados consolidados, métricas e resultados computados. Buscamos garantir que o sistema oferecesse visibilidade clara para o acompanhamento dos cursos gerenciados pela PBLTeX.

## 🚀 Tecnologias Utilizadas

- <i class="fas fa-server"></i> **Backend**: Python puro  
- <i class="fas fa-database"></i> **Banco de Dados**: Arquivo JSON  
- <i class="fas fa-code"></i> **Frontend**: JavaScript com framework HTML e CSS puro  

### Equipe

| Integrantes | Redes Sociais |
|-------|--------|
|Caio Augusto Palma ![Static Badge](https://img.shields.io/badge/Dev-black)|<a href="https://github.com/caiopalma" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Maria Clara Freitas Santos ![Static Badge](https://img.shields.io/badge/Scrum_master-pink)![Static Badge](https://img.shields.io/badge/Dev-black)|<a href="https://github.com/ClaraSantosmf" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Danielle Mayumi Tamazato Santos ![Static Badge](https://img.shields.io/badge/Product_owner-blue)![Static Badge](https://img.shields.io/badge/Dev-black) |<a href="https://github.com/danitamazato" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Eruano Rubens de ALmeida ![Static Badge](https://img.shields.io/badge/Dev-black)|<a href="www.github.com" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Marília Borgo de Moraes ![Static Badge](https://img.shields.io/badge/Dev-black)|<a href="https://github.com/marilia-borgo" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Mateus Soares ![Static Badge](https://img.shields.io/badge/Dev-black) |<a href="https://github.com/MateusMSoares" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Ruth da Silva Mira ![Static Badge](https://img.shields.io/badge/Dev-black) |<a href="https://github.com/RuthMira" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Sara Robert Nara ![Static Badge](https://img.shields.io/badge/Dev-black) |<a href="https://github.com/sararobertnahra" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|William Gomes de Freitas ![Static Badge](https://img.shields.io/badge/Dev-black) |<a href="https://github.com/willigfreitas" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|

## Contribuições Individuais

Atuei como scrum master e bastante como dev também. Sendo o primeiro projeto e a mais experiente da equipe, diversas vezes precisei dar suporte a equipe e direcionar as decisões relacionadas as tecnologias.

Implementei o processo de desenvolvimento do git com fork e PR autorizados apenas com um CR de aprovação. 

Estabaleci arquitetura MVC,com frontend se conectando por meio de WSGI desenvolvido por mim. 

Para auxiliar com as dificuldades profunda dos alunos envolvidos em github e sistema de WSGI, foi contruído, junto com a SM, uma documentação explicativa das tecnologias utilizadas e um roadmap [nessa página](https://c137santos.github.io/FATEC-API-1S-DOCUMENTS/)

## Dificuldade

A principal dificuldade esteve na falta de alinhamento entre as expectativas dos professores, os critérios de avaliação e o entendimento dos alunos sobre o resultado esperado. Essa falta de clareza gerou discussões e ruídos de comunicação, evidenciando a necessidade de documentos mais detalhados e objetivos sobre os pontos que seriam avaliados e o que era esperado em cada entrega. Como resultado, tornou-se obrigatório nas turmas seguintes receber documentos descritivos para garantir maior transparência e entendimento entre todos os envolvidos.

Além disso, a inexperiência natural dos alunos do 1º semestre, aliada ao uso indiscriminado de ferramentas como o ChatGPT sem o devido embasamento teórico, resultou em códigos que, por vezes, não atendiam aos requisitos do projeto.

Esse cenário evidenciou a importância de um acompanhamento mais próximo e de orientações claras sobre o uso adequado dessas ferramentas, reforçando a necessidade de desenvolver uma base sólida de conhecimentos antes de recorrer a soluções automatizadas. Que por muitas vezes tem uma posição pasiva dos  professore, achando que os alunos saberão perguntar. 

![alt text](image-1.png)

Além de uma dificuldade considerável dos alunos com os github. Que foi agravado ao trabalhar com o fork e pr. Ex:

![alt text](image.png)

Para sanar essa dúvida, como SM fiz uma documentação para explicar como poderia ser trabalhado nesse formato. Pode ser consultado [nessa página](https://c137santos.github.io/FATEC-API-1S-DOCUMENTS/biblioteca/#depois-de-ter-branch-s-01-criada)

## Aprendizados e ganhos com o projeto.

Estudo aprofundado sobre o desenvolvimento do WGSI e a compreensão do ciclo de vida de uma requisão HTTP. UM protocolo para comunicação com servidor proposto pela [PEP333](https://peps.python.org/pep-0333/).

Aprendemos a criar e manipular objetos HTTPRequest, entendendo como acessar informações essenciais da solicitação, como método, cabeçalhos, URL e parâmetros. Também assimilamos como mapear URLs para funções (views) responsáveis por gerar as respostas, além de estruturar o retorno ao servidor, incluindo o uso correto dos códigos de status e cabeçalhos HTTP. Esse entendimento foi fundamental para garantir que as respostas fossem entregues de forma adequada ao navegador, permitindo a comunicação eficiente entre frontend e backend.

O trecho a seguir utiliza esse WGSI para subir o servidor e deixa-lo disponível a requisições. 

```
def retorna_response(environ, start_response):
    from urls import url_match
    """
    Essa é a função desenhada no padrão WSGI. Recebe request do navegador e gera response adequado.
    Args:
        environ (dict): Conteúdo preenchido pelo servidor. 
        Como o método HTTP, cabeçalhos, URL, parâmetros de consulta e outras informações relacionadas à solicitação.
        start_response (str): callback enviado pelo servidor para acionar a requisição
        """
    request = HTTPRequest(environ)
    view = url_match(request.path)
    response = view(request)
    start_response(response.status, list(response.headers.items()))
    return response

if __name__ == '__main__':
    print(f"🚀 Servidor HTTP rodando! 🚀 \n Acesse o servidor em: localhost:8080")
    server = make_server("127.0.0.1", 8080, retorna_response)
    server.serve_forever()

```

Isso permitiu que fosse possível realizar solicitações do frontend para backend.

</div>