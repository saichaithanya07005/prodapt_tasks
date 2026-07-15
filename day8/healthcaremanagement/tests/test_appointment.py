import unittest
from models.patient import Patient
from models.doctor import Doctor
from services.healthcare_system import HealthcareSystem

class TestAppointmentService(unittest.TestCase):
    def setUp(self):
        self.datastore = {
            "patients": {},
            "doctors": {},
            "appointments": {}
        }
        self.system = HealthcareSystem(self.datastore)
        self.patient = Patient(1, "John Doe", 30, "Flu")
        self.doctor = Doctor(1, "Dr. Alice", 45, "General Medicine")
        self.system.register_patient(self.patient)
        self.system.register_doctor(self.doctor)

    def test_schedule_appointment(self):
        appointment = self.system.schedule_appointment(1, 1, 1, "2026-07-15", "Annual checkup")
        self.assertEqual(appointment.patient_id, 1)
        self.assertEqual(appointment.doctor_id, 1)

        appointment_info = self.system.appointment_service.get_appointment(1)
        self.assertEqual(appointment_info["Patient ID"], 1)
        self.assertEqual(appointment_info["Doctor ID"], 1)

    def test_schedule_missing_patient(self):
        with self.assertRaises(ValueError):
            self.system.schedule_appointment(2, 99, 1)

    def test_schedule_missing_doctor(self):
        with self.assertRaises(ValueError):
            self.system.schedule_appointment(3, 1, 99)

if __name__ == "__main__":
    unittest.main()
