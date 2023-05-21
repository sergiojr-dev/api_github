from unittest.mock import Mock

import pytest

from lib_github.spam.eviador_de_email import Enviador
from lib_github.spam.main import EnviadorDeSpam
from lib_github.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Sergio', email='juniors.0006@gmail.com'),
            Usuario(nome='Ricardo', email='juniors.0006@gmail.com')
        ],
        [
            Usuario(nome='Sergio', email='juniors.0006@gmail.com')
        ]
    ]
)
def test_quantidade_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'juniors.0006@gmail.com',
        'Curso DEVPOR',
        'Confira a aula x'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Sergio', email='juniors.0006@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'jrcopy.0006@gmail.com',
        'Curso DEVPOR',
        'Confira a aula x'
    )
    enviador.enviar.assert_called_once_with(
        'jrcopy.0006@gmail.com',
        'juniors.0006@gmail.com',
        'Curso DEVPOR',
        'Confira a aula x'
    )