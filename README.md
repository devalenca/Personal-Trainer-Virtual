# Personal Trainer Virtual - Assistente de Treino

Este projeto é um assistente virtual de treino personalizado, que ajusta rotinas de exercícios com base no feedback do usuário. A aplicação utiliza **AWS Step Functions** para coordenar diferentes interações com o modelo de linguagem, criando uma experiência fluida e contínua.

## Visão Geral

O **Personal Trainer Virtual** é um sistema inteligente que cria, ajusta e personaliza planos de treino de acordo com os objetivos e o progresso do usuário. Ele usa **engenharia de prompts** para guiar o fluxo de interação, garantindo respostas consistentes e ajustadas.

### Arquitetura

- **AWS Step Functions**: Coordena o fluxo de interação.
- **AWS Lambda**: Processa as interações e executa a lógica de treino.
- **Amazon Bedrock**: Integração com modelos de linguagem para respostas inteligentes.

### Fluxo de Conversação

1. O usuário fornece seus objetivos de treino e preferências.
2. O assistente cria um plano de treino inicial.
3. Após o treino, o usuário dá feedback e o assistente ajusta a intensidade.
4. O sistema acompanha o progresso e ajusta os treinos periodicamente.

### Configuração do Projeto

#### Passos:

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/seu_usuario/PersonalTrainer-Virtual.git
   cd PersonalTrainer-Virtual
