
import json

def lambda_handler(event, context):
    """
    Função Lambda para processar o feedback do usuário e orquestrar o próximo prompt.
    """
    # Input do evento da Step Function
    current_prompt = event.get('prompt')
    feedback = event.get('feedback')
    
    # Lógica para ajustar o próximo prompt com base no feedback
    if current_prompt == "prompt_one":
        if feedback == "ganho de massa muscular":
            next_prompt = "Vamos focar em treinos de força. Pronto para começar?"
        elif feedback == "perda de peso":
            next_prompt = "Vamos começar com um treino cardiovascular leve."
        elif feedback == "melhora de resistência":
            next_prompt = "Iniciaremos com circuitos para aumentar sua resistência."
        else:
            next_prompt = "Que tal um treino balanceado para começar?"
    
    elif current_prompt == "prompt_two":
        if feedback == "fácil":
            next_prompt = "Ótimo! Vou aumentar a intensidade para o próximo treino."
        elif feedback == "difícil":
            next_prompt = "Sem problemas! Vou reduzir a intensidade para o próximo treino."
        else:
            next_prompt = "Vou ajustar o treino para um nível intermediário."
    
    elif current_prompt == "prompt_three":
        next_prompt = f"Baseado no seu progresso, ajustei a rotina para focar em {feedback}. Pronto para o próximo desafio?"

    # Retornar resposta para a Step Function
    return {
        'statusCode': 200,
        'body': json.dumps({
            'next_prompt': next_prompt
        })
    }
