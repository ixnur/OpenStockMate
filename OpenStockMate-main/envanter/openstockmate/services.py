from django.db import transaction
from .models import Location, Component, ComponentDocumentLink, Log ,DocumentType,  Document ,Component, ComponentDocumentLink, StockAlert, Log ,DocumentType, Document

@transaction.atomic
def StockAlert(data):
    return StockAlert.objects.create(**data)


@transaction.atomic#dokumantasyontypeeee
def create_document_type(data):
    return DocumentType.objects.create(**data)
    
def get_all_document_types():
    return DocumentType.objects.all()
    
def get_document_type_by_name(name):
    return DocumentType.objects.get(name=name)

@transaction.atomic#lokasyon
def create_location(data):
    return Location.objects.create(**data)

def get_all_locations():
    return Location.objects.all()

def get_location_by_name(name):
    return Location.objects.get(name=name)

def get_location_by_parent_id(parent_id):
    return Location.objects.get(pk=parent_id)

def get_location_type(location):
    return Component.objects.get(pk=location.parent_id)

@transaction.atomic#komponentdokumantasyonlink 
def create_component_document_link(data):
    return ComponentDocumentLink.objects.create(**data)

def get_all_component_document_links():
    return ComponentDocumentLink.objects.all()
    
def get_component_document_link_by_id(component_document_link_id):
    return ComponentDocumentLink.objects.get(pk=component_document_link_id)

@transaction.atomic#dokumantasyonn 
def create_document(data):
    return Document.objects.create(**data)

def get_all_documents():
    return Document.objects.all()

def get_document_by_name(name):
    return Document.objects.get(name=name)

@transaction.atomic#kategori
def create_category(data):
    return data.objects.create(**data)

@transaction.atomic
def create_component(data):
    return Component.objects.create(**data)

def get_all_components():
    return Component.objects.all()

def get_component_by_id(component_id):
    return Component.objects.get(pk=component_id)

@transaction.atomic
def update_component(component, data):
    for key, value in data.items():
        setattr(component, key, value)
    component.save()

@transaction.atomic
def delete_component(component):
    component.delete()

@transaction.atomic
def log_to_database(message):
    Log.objects.create(message=message)
