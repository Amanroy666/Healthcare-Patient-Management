"""Database models"""
from sqlalchemy import Column, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    
    patient_id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    ssn_encrypted = Column(Text)
    phone_encrypted = Column(Text)
    email_encrypted = Column(Text)
    address_encrypted = Column(Text)
    
class MedicalRecord(Base):
    __tablename__ = 'medical_records'
    
    record_id = Column(String, primary_key=True)
    patient_id = Column(String)
    diagnosis = Column(Text)
    treatment = Column(Text)
    notes_encrypted = Column(Text)
