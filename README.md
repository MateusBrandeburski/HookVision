# HookVision

HookVision é um visualizador de pagamentos recebidos via webhooks, desenvolvido como parte de um portfólio de projetos. Este sistema captura e organiza eventos de pagamento recebidos por diferentes plataformas, apresentando uma visão centralizada e acessível desses dados. 

O projeto foi construído usando o framework Flask para backend e frontend e é orquestrado em contêineres Docker para maior escalabilidade e flexibilidade. A aplicação roda em um servidor pessoal, o que proporciona controle total sobre o ambiente e o desempenho.

## Funcionalidades

- **Recepção de Webhooks**: Captura e processa dados de pagamento recebidos de múltiplas plataformas em tempo real.
- **Visualização Detalhada**: Interface simples e eficiente para visualização de informações essenciais sobre cada pagamento recebido.
- **Armazenamento Seguro**: Utiliza PostgreSQL para armazenar de forma confiável os dados de pagamentos.
- **Serviços de API com Lumen**: Integrado com um serviço Lumen adicional, possibilitando a extensão das funcionalidades através de APIs.

## Arquitetura e Tecnologias

HookVision foi projetado para rodar como uma aplicação de contêineres, proporcionando portabilidade e facilidade de implementação:

- **Flask**: Framework principal, usado para o backend e frontend da aplicação.
- **PostgreSQL**: Base de dados confiável para armazenar os dados de pagamento de maneira segura.
- **Lumen**: Microframework que possibilita a integração com APIs adicionais.
- **Docker & Docker Compose**: Usados para criar um ambiente isolado e escalável para os diferentes serviços que compõem o HookVision.

## Estrutura de Serviços

A aplicação é composta por três contêineres principais:

1. **Banco de Dados (PostgreSQL)**: Contêiner responsável por armazenar os dados de pagamento de forma estruturada.
2. **Backend e Frontend (Flask)**: Contêiner principal, onde o processamento dos dados recebidos e a interface de visualização são gerenciados.
3. **API Adicional (Lumen)**: Oferece uma interface extensível para integração com outros serviços.

## Motivação e Desafios

A criação do HookVision foi motivada pela necessidade de monitorar pagamentos recebidos de forma confiável e acessível, através de uma solução própria e flexível. Desenvolver uma arquitetura de webhooks envolveu o desafio de lidar com a recepção de dados em tempo real, além de projetar uma estrutura escalável e de fácil manutenção.

Este projeto também serviu como uma oportunidade para aprofundar conhecimentos em Docker e otimizar a comunicação entre contêineres, essencial para ambientes complexos e multi-serviço.

## Conclusão

HookVision é um exemplo de como estruturar uma aplicação completa para recepção e visualização de pagamentos via webhook, demonstrando uma arquitetura sólida e conhecimentos em tecnologias modernas como Flask, Docker e PostgreSQL.

---

**Nota**: Este projeto é parte de um portfólio pessoal e está em execução em um ambiente de servidor controlado. Para mais detalhes ou dúvidas, sinta-se à vontade para entrar em contato.
