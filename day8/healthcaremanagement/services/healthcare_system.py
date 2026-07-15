from services.patient_service import PatientService
from services.doctor_service import DoctorService
from services.appointment_service import AppointmentService
from models.appointment import Appointment

class HealthcareSystem:
    def __init__(self, datastore):
        self.patient_service = PatientService(datastore)
        self.doctor_service = DoctorService(datastore)
        self.appointment_service = AppointmentService(datastore)

    def register_patient(self, patient):
        self.patient_service.add_patient(patient)

    def register_doctor(self, doctor):
        self.doctor_service.add_doctor(doctor)

    def schedule_appointment(self, appointment_id, patient_id, doctor_id, date=None, reason=None):
        if not self.patient_service.get_patient(patient_id):
            raise ValueError(f"Patient not found: {patient_id}")
        if not self.doctor_service.get_doctor(doctor_id):
            raise ValueError(f"Doctor not found: {doctor_id}")

        appointment = Appointment(appointment_id, patient_id, doctor_id, date, reason)
        self.appointment_service.add_appointment(appointment)
        return appointment
