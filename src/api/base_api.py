class BaseApi:
    def completions(self, *args, **kwargs) -> str:
        raise NotImplementedError
