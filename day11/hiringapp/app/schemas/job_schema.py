from pydantic import BaseModel, ConfigDict

class JobBase(BaseModel):
    title: str
    description: str
    salary: float
    company: str
    
class JobCreate(JobBase):
    pass

class JobUpdate(JobBase):
    title:str | None = None
    description:str | None = None
    salary:float | None = None
    company:str | None = None
    
class JobResponse(JobBase):
    id:int
    model_config = ConfigDict(form_attributes = True)
