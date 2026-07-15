import unittest
from models.patient import Patient
from services.patient_service import PatientService

class TestPatientService(unittest.TestCase):
    def setUp(self):
        self.datastore = {
            "patients": {},
            "doctors": {},
            "appointments": {}
        }
        self.service = PatientService(self.datastore)

    def test_add_and_get_patient(self):
        patient = Patient(1, "John Doe", 30, "Flu")
        self.service.add_patient(patient)

        patient_info = self.service.get_patient(1)
        self.assertEqual(patient_info["Name"], "John Doe")
        self.assertEqual(patient_info["Ailment"], "Flu")

    def test_update_patient(self):
        patient = Patient(2, "Jane Smith", 25, "Cold")
        self.service.add_patient(patient)
        self.service.update_patient(2, "Allergy")

        patient_info = self.service.get_patient(2)
        self.assertEqual(patient_info["Ailment"], "Allergy")

    def test_delete_patient(self):
        patient = Patient(3, "Mark Lee", 42, "Infection")
        self.service.add_patient(patient)
        self.service.delete_patient(3)

        self.assertIsNone(self.service.get_patient(3))

if __name__ == "__main__":
    unittest.main()
