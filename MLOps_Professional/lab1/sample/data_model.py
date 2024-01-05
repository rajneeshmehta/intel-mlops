from pydantic import BaseModel

class MaintenancePayload(BaseModel):
    temperature: int
    hydrolic_pressure_psi: int

class SupportBotPayload(BaseModel):
    message: str