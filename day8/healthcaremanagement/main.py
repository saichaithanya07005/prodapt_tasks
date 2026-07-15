from models.patient import Patient
from models.doctor import Doctor
from services.healthcare_system import HealthcareSystem
from data.datastore import datastore

# Initialize the systems
system = HealthcareSystem(datastore)

# Create patients
p1 = Patient(1, "John Doe", 30, "Flu")
p2 = Patient(2, "Jane Smith", 25, "Cold")

# Create doctors
d1 = Doctor(1, "Dr. Alice Green", 45, "General Medicine")
d2 = Doctor(2, "Dr. Sanjay Patel", 39, "Pediatrics")

# Register patients and doctors
system.register_patient(p1)
system.register_patient(p2)

system.register_doctor(d1)
system.register_doctor(d2)

# Schedule an appointment
appointment = system.schedule_appointment(
    appointment_id=1,
    patient_id=p1.id,
    doctor_id=d1.id,
    date="2026-07-15",
    reason="Annual checkup"
)

print("Patient:", system.patient_service.get_patient(p1.id))
print("Doctor:", system.doctor_service.get_doctor(d1.id))
print("Appointment:", system.appointment_service.get_appointment(appointment.id))