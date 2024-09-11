# Personal Trainer Virtual - Assistente de Treino

Este projeto simula um **Assistente Virtual de Treino** utilizando AWS Step Functions e Lambda Functions para orquestrar prompts e gerar planos de treino personalizados com base nas interações do usuário.

## Objetivo

Criar uma experiência personalizada de treino, onde o usuário pode fornecer feedback e o assistente ajusta a rotina de acordo com suas necessidades e progresso.

## Tecnologias Utilizadas

- **AWS Step Functions**: Para coordenar as etapas da interação.
- **Lambda Functions**: Para processar o feedback do usuário e gerar novos prompts.
- **Modelos de Linguagem**: Para gerar respostas personalizadas com base nos inputs do usuário.

## Estrutura do Projeto

|-- PersonalTrainer-Virtual/
|-- prompts/
    |-- prompt_engineering.md # Lógica de criação dos prompts.
|-- lambdas/ 
    |-- handler.py # Função Lambda para orquestração. 
    |-- requirements.txt # Dependências. 
|-- step-functions/ |-- step_functions.json # Definição da Step Function. 
|-- README.md # Documentação principal do projeto.


## Passos para Execução

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu_usuario/PersonalTrainer-Virtual.git
2 **Configurar AWS CLI**:

Configure suas credenciais AWS:

``
aws configure
``

3 **Deploy das Funções Lambda**

No diretório lambdas/, crie um arquivo ZIP para a função Lambda:

    
    zip -r lambda_function.zip handler.py

Faça o deploy da função Lambda:


    aws lambda create-function --function-name personalTrainerFunction --zip-file fileb://lambda_function.zip --handler handler.lambda_handler --runtime python3.8 --role arn:aws:iam::role/execution_role
    
    

4 **No console da AWS, crie uma nova Step Function com base no arquivo step_functions.json.**

5 **Testar a Aplicação:**

Execute a Step Function e verifique o fluxo de interação e ajustes de treino.