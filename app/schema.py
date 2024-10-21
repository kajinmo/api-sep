from pydantic import BaseModel, PositiveFloat

class ProdutosSchema(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: PositiveFloat
