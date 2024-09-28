"""Módulo contendo os schemas usados na documentação do Mobile"""
from typing import List
from datetime import datetime
from pydantic import BaseModel
from model.mobile import Mobile

class MobileSchema(BaseModel):
    """ Define como um novo celular a ser inserido deve ser representado
    """
    battery_power: int = 1810
    blue: bool = True
    clock_speed: float = 1.4
    dual_sim: bool = False
    fc: int = 1
    four_g: bool = True
    int_memory: int = 16
    m_dep: float = 0.69
    manufacturer: str = 'Apple'
    mobile_wt: int = 129
    model: str = 'iPhone 6'
    n_cores: int = 2
    pc: int = 8
    price_range_predicted: int = 1
    price_final: int = 700
    px_height: int = 1334
    px_width: int = 750
    ram: int = 1024
    sc_h: int = 10
    sc_w: int = 6
    talk_time: int = 14
    three_g: bool = True
    touch_screen: bool = True
    wifi: bool = True

class MobileViewSchema(BaseModel):
    """Define como um celular será retornado
    """
    id: int = 1
    date_insert: datetime = '01/01/1900'
    battery_power: int = 1810
    blue: bool = True
    clock_speed: float = 1.4
    dual_sim: bool = False
    fc: int = 1
    four_g: bool = True
    int_memory: int = 16
    m_dep: float = 0.69
    manufacturer: str = 'Apple'
    mobile_wt: int = 129
    model: str = 'iPhone 6'
    n_cores: int = 2
    pc: int = 8
    price_range_predicted: int = 1
    price_final: int = 700
    px_height: int = 1334
    px_width: int = 750
    ram: int = 1024
    sc_h: int = 10
    sc_w: int = 6
    talk_time: int = 14
    three_g: bool = True
    touch_screen: bool = True
    wifi: bool = True

class MobileBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do celular.
    """
    model: str = "iPhone 6"

class ListaMobileSchema(BaseModel):
    """Define como uma lista de celulares será representada
    """
    mobiles: List[MobileSchema]

class MobileDelSchema(BaseModel):
    """Define como um celular para deleção será representado
    """
    name: str = "iPhone 6"

class MobilePriceRangeSchema(BaseModel):
    """Define como deve ser a estrutura para o retorno do price_range.
    """
    battery_power: int = 1810
    blue: bool = True
    clock_speed: float = 1.4
    dual_sim: bool = False
    fc: int = 1
    four_g: bool = True
    int_memory: int = 16
    m_dep: float = 0.69
    mobile_wt: int = 129
    n_cores: int = 2
    pc: int = 8
    px_height: int = 1334
    px_width: int = 750
    ram: int = 1024
    sc_h: int = 10
    sc_w: int = 6
    talk_time: int = 14
    three_g: bool = True
    touch_screen: bool = True
    wifi: bool = True

# Apresenta apenas os dados de um celular
def apresenta_mobile(mobile: Mobile):
    """ Retorna uma representação do celular seguindo o schema definido em
        MobileViewSchema.
    """
    return {
        "id": mobile.id,
        "battery_power": mobile.battery_power,
        "blue": mobile.blue,
        "clock_speed": mobile.clock_speed,
        "date_insert": mobile.date_insert,
        "dual_sim": mobile.dual_sim,
        "fc": mobile.fc,
        "four_g": mobile.four_g,
        "int_memory": mobile.int_memory,
        "m_dep": mobile.m_dep,
        "manufacturer": mobile.manufacturer,
        "mobile_wt": mobile.mobile_wt,
        "model": mobile.model,
        "n_cores": mobile.n_cores,
        "pc": mobile.pc,
        "price_range_predicted": mobile.price_range_predicted,
        "price_final": mobile.price_final,
        "px_height": mobile.px_height,
        "px_width": mobile.px_width,
        "ram": mobile.ram,
        "sc_h": mobile.sc_h,
        "sc_w": mobile.sc_w,
        "talk_time": mobile.talk_time,
        "three_g": mobile.three_g,
        "touch_screen": mobile.touch_screen,
        "wifi": mobile.wifi
    }

# Apresenta uma lista de celulares
def apresenta_mobiles(mobiles: List[Mobile]):
    """ Retorna uma representação dos celulares seguindo o schema definido em
        MobileViewSchema.
    """
    result = []
    for mobile in mobiles:
        result.append({
            "id": mobile.id,
            "battery_power": mobile.battery_power,
            "blue": mobile.blue,
            "clock_speed": mobile.clock_speed,
            "date_insert": mobile.date_insert,
            "dual_sim": mobile.dual_sim,
            "fc": mobile.fc,
            "four_g": mobile.four_g,
            "int_memory": mobile.int_memory,
            "m_dep": mobile.m_dep,
            "manufacturer": mobile.manufacturer,
            "mobile_wt": mobile.mobile_wt,
            "model": mobile.model,
            "n_cores": mobile.n_cores,
            "pc": mobile.pc,
            "price_range_predicted": mobile.price_range_predicted,
            "price_final": mobile.price_final,
            "px_height": mobile.px_height,
            "px_width": mobile.px_width,
            "ram": mobile.ram,
            "sc_h": mobile.sc_h,
            "sc_w": mobile.sc_w,
            "talk_time": mobile.talk_time,
            "three_g": mobile.three_g,
            "touch_screen": mobile.touch_screen,
            "wifi": mobile.wifi
        })

    return {"mobiles": result}

def retorna_price_range(predicted: int):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "price_range_predicted": predicted,
        "price_range_description": return_description_range(predicted)
    }

def return_description_range(value):
    """Retorna a descrição do price_range
    """
    description_range = {
        0: "Low Cost",
        1: "Medium Cost",
        2: "High Cost",
        3: "Very High Cost"
    }
    return description_range.get(value, "Price_range inválido")
