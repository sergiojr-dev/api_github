import requests


def avatar(usuario):
    """
    Busca o avatar (imagem) do usuário no github
    :param usuario: str que irá passar o nome do usuário do github
    :return: str com o link do avatar (imagem)
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']



