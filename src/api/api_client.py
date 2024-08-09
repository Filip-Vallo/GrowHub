# GrowHub | https://github.com/Filip-Vallo/GrowHub/ | /src/api/ | Python 3.9.19

# Codebase imports
from exceptions_api import get_exception


class APIClient:
    @staticmethod
    def get_exception(exception_name):
        return get_exception(exception_name)
