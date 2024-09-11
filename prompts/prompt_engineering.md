# Engenharia de Prompts - Personal Trainer Virtual

Este documento descreve a lógica por trás da criação de prompts para o assistente virtual de treino.

## Objetivo

O objetivo é guiar o modelo de linguagem em uma conversa interativa com o usuário, ajudando-o a definir metas de treino, ajustar sua rotina com base no feedback e acompanhar seu progresso.

### Prompts

#### 1. Prompt Inicial - Objetivo e Avaliação

Neste primeiro prompt, o assistente pede ao usuário para fornecer informações sobre seus objetivos de treino e possíveis limitações físicas. A ideia é personalizar o plano de treino de acordo com o perfil do usuário.

```json
{
  "prompt_one": "Olá! Qual é o seu objetivo de treino? Ganho de massa muscular, perda de peso ou melhora de resistência? Tem alguma restrição física ou preferência?"
}
{
  "prompt_two": "Com base nas suas informações, aqui está um plano de treino. Como você se sentiu após o treino?"
}
{
  "prompt_three": "Você atingiu seu objetivo anterior? Qual área do corpo gostaria de focar no próximo treino?"
}
{
  "prompt.$": "States.Format('{}\n{}', $.convo_one.convo_one, $.feedback)"
}