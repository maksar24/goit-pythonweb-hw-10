from fastapi import APIRouter, Depends
from typing import List

from src.schemas import ContactCreate, ContactUpdate, ContactResponse
from src.database.db import get_db
from src.repository.repository import ContactRepository
from src.services.services import ContactService
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/contacts")

def get_service(session: AsyncSession = Depends(get_db)) -> ContactService:
    repo = ContactRepository(session)
    service = ContactService(repo)
    return service

@router.get("/", response_model=List[ContactResponse])
async def list_contacts(skip: int = 0, limit: int = 10, service: ContactService = Depends(get_service)):
    return await service.list_contacts(skip=skip, limit=limit)

@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: int, service: ContactService = Depends(get_service)):
    return await service.get_contact_by_id(contact_id)

@router.post("/", response_model=ContactResponse, status_code=201)
async def create_contact(contact_data: ContactCreate, service: ContactService = Depends(get_service)):
    return await service.create_contact(contact_data)

@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(contact_id: int, contact_data: ContactUpdate, service: ContactService = Depends(get_service)):
    return await service.update_contact(contact_id, contact_data)

@router.delete("/{contact_id}", status_code=204)
async def delete_contact(contact_id: int, service: ContactService = Depends(get_service)):
    await service.delete_contact(contact_id)
