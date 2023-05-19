from lib_github.spam.eviador_de_email import Enviador
from lib_github.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_email(
        'juniors.0006@gmail.com',
        'Curso DEVPOR',
        'Confira a aula x'
    )