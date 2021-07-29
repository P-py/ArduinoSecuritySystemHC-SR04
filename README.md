# Sistema de segurança - HC-SR04 + Notificação em e-mail

*Copyright (c) 2021 Pedro Salviano Santos*

*__Note:__ this is the portuguese (pt-BR) version of the DOCS, if you want to read it in english (en-US), please translate it.*

Esse projeto foi inteiramente produzido por Pedro Salviano Santos e todos os direitos são do mesmo, a licença usada aqui é MIT, então caso queira compartilhar é possível, apenas faça isso corretamente, utilizando as métricas de "copyright" da licença.


## Objetivos deste projeto
Este projeto possui como principal foco e intuito a simulação/criação de um sistema de segurança simples e DIY ("Faça-você-mesmo"), com uma *feature* de notificação ao usuário por e-mail.

Uma explicação geral e análise mais profunda do código disponível neste vídeo: [Documentação do Sistema de Segurança - HC-SR04 + notificação por e-mail.](https://youtu.be/MY-hK56yuso)

__É MUITO IMPORTANTE QUE NENHUM OBJETO FIQUE À MENOS DE 80cm DA PARTE FRONTAL DO SENSOR, JÁ QUE ESTÁ É A DISTÂNCIA DE ATIVAÇÃO MÍNIMA PARA O ALARME!__

## Instalação

Os requisitos para rodar os scripts corretamente são:

| Requisito | Propósito |
|--|--|
| Circuito com placa Arduino UNO segundo o código .ino (C++) | Detecção, processamento e comunicação funcionais com o sensor HC-SR04 |
| smtplib (biblioteca python) | Envio dos alertas por e-mail |
| email lib (biblioteca python) | Envio dos alertas por e-mail |
| PySerial (biblioteca python) | Comunicação entre o lado Python com o lado Arduino. |

Caso você não possua uma das bibliotecas python citadas acima basta instalar elas através do `pip`:

```shell
pip install smtplib

pip install email

pip install PySerial
``` 

Após a instalação de todos os requisitos é necessário que você faça download do código, através do `git` ou do aplicativo web/desktop do GitHub:

*Para download através do `git`*:
```shell
git clone https://github.com/P-py/ArduinoSecuritySystemHC-SR04.git
```

*Para download com GitHub web ou desktop:*

Vá para este link: [P-py/ArduinoSecuritySystemHC-SR04](https://github.com/P-py/ArduinoSecuritySystemHC-SR04)-> Clique no botão verde "Code" -> "Download ZIP"

Após baixar o código está na hora de criar uma nova conta gmail que funcione como o bot que envia as mensagens. (*Este processo não será explicado aqui.*)

Quando terminar de criar sua nova conta bot basta acessar https://myaccount.google.com/security e ativar a autentificação de dois fatores e criar uma senha de app do tipo "Outro". (*Este processo não será explicado aqui.*)

Quando terminar isso você estará no último passo, basta acessar a basta com o código que você baixou, abrir o arquivo `emailAlarm.py` e mudar as variáveis seguintes:

```python
[...]

user = "###"
password = "###"
message['from'] = user

[...]
```

O campo `user="###"` deve ser substituído pelo seu endereço de e-mail da conta criada, e o campo `password="###"` pela senha de app criada.

__É MUITO IMPORTANTE QUE NENHUM OBJETO FIQUE À MENOS DE 80cm DA PARTE FRONTAL DO SENSOR, JÁ QUE ESTÁ É A DISTÂNCIA DE ATIVAÇÃO MÍNIMA PARA O ALARME!__

Chegando aqui e concluindos todos os passos, parabéns! Você instalou tudo com sucesso.

## Utilização

*__Nota:__ para a utilização do sistema é necessário e obrigatório seguir os passos da seção "Instalação", anterior à esta.*

A utilização é bem simples, basta montar o circuito e posicionar o sensor, agora abra o console e rode o script python, com isso feito *TODO E QUALQUER OBJETO QUE PASSE À MENOS DE 80CM DO SENSOR SERÁ REPORTADO COMO OBSTÁCULO*, __significando assim que ele detectará uma presença, enviando o alerta e tocando o alarme!__

Este vídeo é uma extensão da documentação e serve como exemplo do funcionamento: [Documentação do Sistema de Segurança - HC-SR04 + notificação por e-mail.](https://youtu.be/MY-hK56yuso)

*Recomendo que assita o vídeo acima!*
