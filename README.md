# Sistema de segurança - HC-SR04 + Notificação em e-mail

*Copyright (c) 2021 Pedro Salviano Santos*

*__Note:__ this is the portuguese (pt-BR) version of the DOCS, if you want to read it in english (en-US), please translate it.*

Esse projeto foi inteiramente produzido por Pedro Salviano Santos e todos os direitos são do mesmo, a licença usada aqui é MIT, então caso queira compartilhar é possível, apenas faça isso corretamente, utilizando as métricas de "copyright" da licença.


## Objetivos deste projeto
Este projeto possui como principal foco e intuito a simulação/criação de um sistema de segurança simples e DIY ("Faça-você-mesmo"), com uma *feature* de notificação ao usuário por e-mail.

Uma explicação geral e análise mais profunda do código disponível neste vídeo: [Documentação do Sistema de Segurança - HC-SR04 + notificação por e-mail.]()

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
git clone  
```