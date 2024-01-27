from src.api.llamacpp_api import LlamaCppApi
from src.api.gigachat_api import GigaChatApi
from src.api.saiga_api import SaigaApi
from src.checker import Checker


if __name__ == "__main__":
    api = GigaChatApi()
    api2 = LlamaCppApi()
    api3 = SaigaApi()

    checker = Checker(api)
    checker2 = Checker(api2)
    checker3 = Checker(api3)

    # checker.run()  # gigachat
    # checker2.run()  # llamacpp
    checker3.run()  # saiga
