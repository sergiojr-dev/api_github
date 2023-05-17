import requests


def avatar(usuario):
    """
    Busca o avatar (imagem) do usuário no github
    :param usuario: str que irá passar o nome do usuário do github
    :return: str com o link do avatar (imagem)
    """

    url = f'https://api.github.com/users/{usuario}'
    resposta = requests.get(url)
    return resposta.json()['avatar_url']


if __name__ == '__main__':
    print(avatar('sergiojr-dev'))
