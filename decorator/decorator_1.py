def decorated(func):
    print('I am decorated')
    func()


@decorated
def ordinary():
    print('I am ordinary')




