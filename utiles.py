
from time import sleep


def get_simple_response(prompt: str = 'Qui es-tu ?', last_interactions=[]):
    """
    Fonction simplifiée qui retourne "message reçu" sans appeler l'API.

    Args:
        prompt (str): Le message de l'utilisateur.
        last_interactions (list): L'historique des interactions (non utilisé ici).

    Returns:
        str: La réponse fixe "message reçu".
        list: L'historique mis à jour avec le nouveau message.
    """
    response_assistant = f"Vous avez écrit : {prompt}"

    # Historique des interactions
    last_interactions += [
        {'role': 'user', 'content': prompt},
        {'role': 'assistant', 'content': response_assistant}
    ]

    return response_assistant, last_interactions


