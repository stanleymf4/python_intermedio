def ejemplo_args(*args):
    print(f"Argumentos posicionales: {args}")


def ejemplo_kwargs(**kwargs):
    print(f"kwargs {type(kwargs)}")
    print(f"kwargs: {kwargs}")
    print("==================================")


def sumar_numeros(*args):
    return sum(args)
