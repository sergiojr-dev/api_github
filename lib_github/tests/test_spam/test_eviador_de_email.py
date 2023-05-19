import pytest

from lib_github.spam.eviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['juniors.0006@gmail.com', 'teste@gmail.com'])
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(destinatario,
                                'jrcopy.0006@gmail.com',
                                'Curso DEVPRO',
                                'Aula TDD e Baby Steps')

    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'teste'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'jrcopy.0006@gmail.com',
            'Curso DEVPRO',
            'Aula TDD e Baby Steps')
