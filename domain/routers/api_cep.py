from fastapi import APIRouter
#from dotenv import load_dotenv
from domain.regras_cep import analisar_cep

#load_dotenv()

router = APIRouter()


@router.get("/consulta/{cep}")
async def consulta_cep(cep: str):
    return analisar_cep(cep)