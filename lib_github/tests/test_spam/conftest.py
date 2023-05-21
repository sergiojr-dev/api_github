import pytest

from lib_github.spam.db import Conexao


@pytest.fixture(scope='session')
def conexao():
    conexao_obj = Conexao()
    yield conexao_obj
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    """
        roll_back, ele desfaz todas as sessões do testes
        permitindo que nada fique salvo no banco de dados
    """
    sessao_obj.fechar()
