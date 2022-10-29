from yanwu import App


def test_init_app():
    app = App()
    assert app.counter == 1
    assert app.workingDir is None
