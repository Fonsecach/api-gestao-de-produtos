from pydantic import BaseModel

class CustomBaseModel(BaseModel):
    def dict(self, *args, **kwargs):
        d = super().dict(*args, **kwargs)
        d = {k: value for k, value in d.items() if value is not None}
        return d
