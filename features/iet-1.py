from models.a_model import ModelA


def iet_3_func():
    return "iet_3"


def iet_1():

    iet_3_result = iet_3_func()

    a_model = ModelA()

    return "iet_1" + " : " + iet_3_result
