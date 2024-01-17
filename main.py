from fastapi import FastAPI
import random
from pydantic import BaseModel

app = FastAPI()

class CurrentPrices(BaseModel):
    name: str
    ticker: str
    mp: float

@app.post("/tableau")
async def tableau(nb_appel: int, init: list[CurrentPrices]):
    pourcentageA = random.randint(1, 5)
    pourcentageB = random.randint(1, 5)
    pourcentageC = random.randint(1, 5)
    pourcentageD = random.randint(1, 5)
    tableau = {"SA":0, "SB":0, "SC":0, "SD":0}
    print(init)
    if nb_appel%3==0:
        for i in range(len(init)):
            if i == 0:
                tableau["SA"] = round(float(init[i].mp)-(pourcentageA/100*float(init[i].mp)),2)
            elif i ==1:
                tableau["SB"] = round(float(init[i].mp)-(pourcentageB/100*float(init[i].mp)),2)
            elif i == 2:
                tableau["SC"] = round(float(init[i].mp)-(pourcentageC/100*float(init[i].mp)),2)
            else:
                tableau["SD"] = round(float(init[i].mp)-(pourcentageD/100*float(init[i].mp)),2)
               
    else:
        for i in range(len(init)):
            if i == 0:
                tableau["SA"] = round(float(init[i].mp)+(pourcentageA/100*float(init[i].mp)),2)
            elif i ==1:
                tableau["SB"] = round(float(init[i].mp)+(pourcentageB/100*float(init[i].mp)),2)
            elif i == 2:
                tableau["SC"] = round(float(init[i].mp)+(pourcentageC/100*float(init[i].mp)),2)
            else:
                tableau["SD"] = round(float(init[i].mp)+(pourcentageD/100*float(init[i].mp)),2)
            
    return tableau