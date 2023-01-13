import yaml
import json

from fastapi import APIRouter

from models.yml import Yml
from schemas import yml_schema

router = APIRouter(
    prefix="/yml"
)


@router.get("/init_yml/")
async def init_yml():
    if Yml.objects.get():
        return
    with open("./app/docker-compose.yml") as file:
        yml_data = yaml.safe_load(file)
        compose = Yml(**yml_data)
        compose.save()
        compose.reload()
        return json.loads(compose.to_json())


@router.get("/")
async def read_master():
    yml = Yml.objects.get()
    # 계층을 이루어서 조회 하려면 EmbeddedDocumentField로 정의 해야합니다.
    return {"ports": yml.services.master.ports, "json": json.loads(yml.to_json())}


@router.post("/")
async def recreate_yml():
    yml = Yml.objects.get()
    yml_json = json.loads(yml.to_json())
    del yml_json['_id']
    with open("./app/docker-compose.yml", "w", encoding="utf-8") as file:
        yaml.dump(yml_json, file)


@router.put("/")
async def update_yml(
        data_list: list[yml_schema.UpdateYml, ...]
):
    yml = Yml.objects.get()
    for update_data in data_list:
        if update_data.is_str:
            value = update_data.data
            exec(f"""yml.{update_data.path} = "{value}" """)
        else:
            value = update_data.data
            exec(f"yml.{update_data.path} = {value}")
    yml.save()
    return json.loads(yml.to_json())
