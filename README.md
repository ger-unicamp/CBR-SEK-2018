# SEK 2018 - GER (Grupo de Estudos em Robótica)

Código do Projeto SEK para o desafio 2017/2018 da Competição Brasileira de Robótica.

## Sobre o Projeto

A IEEE Standard Educational Kit (SEK) é uma categoria da Competição Brasileira de Robótica que busca o desenvolvimento de robôs autônomos por alunos de graduação através de kits educacionais LEGO.

### Pré-requisitos

Os códigos e testes foram realizados com um kit LEGO Mindstorms EV3 e a plataforma Robotc.

### Objetivo

O objetivo é construir um robô capaz de recolher bonecos em determinados pontos pré-designados dentro de um labirinto e devolvê-los em um local designado (plaza).
A "cidade", como é chamado de forma lúdica o circuito em que o robô deverá passar, tem intersecções e ruas sem saída. Cada intersecção tem uma cor, que se relaciona com a direção que deverá ser seguida para evitar os pontos mortos (que são de cor preta). 

### Regras da Competição

* O robô deve ser capaz de pegar até no máximo quatro bonecos
* O robô não deve exceder 30cm de largura e 30cm de comprimento, porém não há limite para sua altura
* Cada equipe começa com 0 pontos.
* Cada boneco ‘bem entregue’: +100 pontos
* Para cada boneco que não está na praça ou uma parada sem tocar no robô, por mais de 10
segundos:-50 pontos
* Para cada reinicio:-100 pontos
* Para cada modelo de boneco tocando o robô na reinicialização:-50 pontos
* Para cada 30 segundos adicionais (t_max – t_conclusão/completion):+25
* Depois de ter percorrido um cruzamento na direção certa:
    * +50 pontos por ter navegado na direção certa (apenas na primeira vez)
    * Para cada direção incorreta tomada:-25
* Tempo máximo por round 10 minutos, este tempo conta com os reinícios
* Uma pessoa pode ser considerada bem entregue , se está tocando o círculo preto no centro da praça e não há nenhuma peça do robô tocando a pessoa/boneco. Somente neste caso a pessoa pode ser recuperada da praça e os pontos podem ser concedidos
* É considerado quando o robô está em uma rua, quando duas de suas rodas estão tocando a rua

### Estrutura do Código

O código foi estruturado através de uma máquina de estados, de acordo com as regras e objetivos da competição.

```
Estados:

* Andar Reto
* Intersecção
* Capturar Bonecos
* Rampa Ida
* Plaza
* Rampa Volta

Sensores:

* Ultrassônico 
* Cor 

```

## Links úteis

* [Robotc for LEGO Mindstorms 4.X Users Manual](http://help.robotc.net/WebHelpMindstorms/index.htm)
* [IEEE Standart Educational Kit (SEK)](http://www.cbrobotica.org/?page_id=64&amp;lang=pt)
* [GIT - Guia Prático](http://rogerdudler.github.io/git-guide/index.pt_BR.html)
* [Comandos Git: Aprenda Git do básico ao avançado](http://comandosgit.github.io/)
* [Terminal Básico - Linux](https://www.linux.ime.usp.br/~lucasmmg/livecd/documentacao/documentos/terminal/Terminal_basico.html)
* [C Reference](http://www.cplusplus.com/reference/)
* [Finite-State Machines: Theory and Implementation](https://gamedevelopment.tutsplus.com/tutorials/finite-state-machines-theory-and-implementation--gamedev-11867)
* [Máquina de estado - Embarcados](https://www.embarcados.com.br/maquina-de-estado/)
* [GER - Grupo de Estudos em Robótica](http://www.gerunicamp.com.br/)

## Participantes
* Thais Araujo Bispo
* Émerson Kazuhiro Takematsu 
* Maria Júlia Cristofoletti de Souza
* Tiago Eidi Hatta
* Wesna Simone Bulla de Araujo
* Natan Rodrigues de Oliveira
* Luis Felipe Brentegani
