import requests
import time

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



def get_agent_response_API(prompt: str = 'Qui es-tu ?', last_interactions=[]):
    """
    Envoie une requête GET à l'API FastAPI et traite la réponse.
    Gère les cas où la réponse n'est pas un JSON valide.
    """
    url = "http://localhost:8001/requete" 
    params = {"prompt": prompt}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        try:
            response_json = response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Erreur: La réponse n'est pas un JSON valide: {response.text}")
            return f"Erreur: La réponse n'est pas un JSON valide: {response.text}", last_interactions

        if isinstance(response_json, dict) and "message" in response_json:
            response_assistant = response_json["message"]
            last_interactions += [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": response_assistant}
            ]
            return response_assistant, last_interactions
        else:
            print(f"Erreur: La réponse JSON ne contient pas de clé 'message' ou n'est pas un dictionnaire: {response_json}")
            return f"Erreur: Réponse inattendue de l'API.", last_interactions # Erreur gérée ici

    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête: {e}")
        return f"Erreur lors de la communication avec l'API: {e}", last_interactions
    

def get_agent_response_NGROK(prompt: str = 'Qui es-tu ?', last_interactions=[]):
    """
    Envoie une requête GET à l'API FastAPI et traite la réponse.
    Gère les cas où la réponse n'est pas un JSON valide.
    """
    url = "https://ae59-147-210-91-7.ngrok-free.app/" 
    params = {"prompt": prompt}

    try:
        response = requests.get(url, params=params)
        #response = requests.get(url)
        return response.text,False
    
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête: {e}")
        return f"Erreur lors de la communication avec l'API: {e}", last_interactions
        #try:



def get_agent_response_NGROK_et_time(prompt: str = 'Qui es-tu ?', last_interactions=[]):
    """
    Envoie une requête GET à l'API FastAPI via Ngrok et traite la réponse.
    Mesure le temps de la requête et le renvoie avec la réponse.
    Gère les cas où la réponse n'est pas un JSON valide.
    """
    url = "https://ae59-147-210-91-7.ngrok-free.app/requete"  # Assurez-vous que l'URL est correcte
    params = {"prompt": prompt}

    try:
        start_time = time.time()  # Enregistre le temps de début
        response = requests.get(url, params=params)
        end_time = time.time()  # Enregistre le temps de fin
        elapsed_time = end_time - start_time  # Calcule le temps écoulé en secondes

        return response.text, elapsed_time  # Retourne la réponse et le temps écoulé

    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête: {e}")
        return f"Erreur lors de la communication avec l'API: {e}", 0  # Retourne un temps de 0 en cas d'erreur

    '''
            response_json = response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"Erreur: La réponse n'est pas un JSON valide: {response.text}")
            return f"Erreur: La réponse n'est pas un JSON valide: {response.text}", last_interactions

        if isinstance(response_json, dict) and "message" in response_json:
            response_assistant = response_json["message"]
            last_interactions += [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": response_assistant}
            ]
            return response_assistant, last_interactions
        else:
            print(f"Erreur: La réponse JSON ne contient pas de clé 'message' ou n'est pas un dictionnaire: {response_json}")
            return f"Erreur: Réponse inattendue de l'API.", last_interactions # Erreur gérée ici

    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête: {e}")
        return f"Erreur lors de la communication avec l'API: {e}", last_interactions
        '''
    