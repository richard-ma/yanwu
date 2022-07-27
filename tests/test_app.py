from yanwu import App


def test_init():
    app = App()
    assert app.counter == 1
    assert app.workingDir is None


if __name__ == "__main__":
    print(dir(App))
