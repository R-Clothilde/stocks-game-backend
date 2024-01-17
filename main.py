from fastapi import FastAPI
import random
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    tableau = []
    print(init)
    if nb_appel%3==0:
        for i in range(len(init)):
            if i == 0:
                tableau.append({"name":"StockA", "ticker":"SA", "mp":round(float(init[i].mp)-(pourcentageA/100*float(init[i].mp)),2)})
            elif i ==1:
                tableau.append({"name":"StockB", "ticker":"SB", "mp":round(float(init[i].mp)-(pourcentageB/100*float(init[i].mp)),2)})
            elif i == 2:
                tableau.append({"name":"StockC", "ticker":"SC", "mp":round(float(init[i].mp)-(pourcentageC/100*float(init[i].mp)),2)})
            else:
                tableau.append({"name":"StockD", "ticker":"SD", "mp":round(float(init[i].mp)-(pourcentageD/100*float(init[i].mp)),2)})
               
    else:
        for i in range(len(init)):
            if i == 0:
                tableau.append({"name":"StockA", "ticker":"SA", "mp":round(float(init[i].mp)+(pourcentageA/100*float(init[i].mp)),2)})
            elif i ==1:
                tableau.append({"name":"StockB", "ticker":"SB", "mp":round(float(init[i].mp)+(pourcentageB/100*float(init[i].mp)),2)})
            elif i == 2:
                tableau.append({"name":"StockC", "ticker":"SC", "mp":round(float(init[i].mp)+(pourcentageC/100*float(init[i].mp)),2)})
            else:
                tableau.append({"name":"StockD", "ticker":"SD", "mp":round(float(init[i].mp)+(pourcentageD/100*float(init[i].mp)),2)})
            
    return tableau