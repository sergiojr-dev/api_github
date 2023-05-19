from lib_github.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome ='Sergio', email='juniors.0006@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Sergio', email='juniors.0006@gmail.com'),
        Usuario(nome='Ricardo', email='juniors.0006@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()