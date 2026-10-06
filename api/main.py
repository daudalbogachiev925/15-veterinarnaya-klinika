from fastapi import FastAPI
from routes import owners, pets, services, vets, visits, vaccines, reports

app = FastAPI(title="Vet Clinic API")
app.include_router(owners.router, prefix="/owners", tags=["owners"])
app.include_router(pets.router, prefix="/pets", tags=["pets"])
app.include_router(services.router, prefix="/services", tags=["services"])
app.include_router(vets.router, prefix="/vets", tags=["vets"])
app.include_router(visits.router, prefix="/visits", tags=["visits"])
app.include_router(vaccines.router, prefix="/vaccines", tags=["vaccines"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])

@app.get("/health")
def health(): return {"status": "ok"}
