import unittest
from models.doctor import Doctor
from services.doctor_service import DoctorService

class TestDoctorService(unittest.TestCase):
    def setUp(self):
        self.datastore = {
            "patients": {},
            "doctors": {},
            "appointments": {}
        }
        self.service = DoctorService(self.datastore)

    def test_add_and_get_doctor(self):
        doctor = Doctor(1, "Dr. Alice", 45, "General Medicine")
        self.service.add_doctor(doctor)

        doctor_info = self.service.get_doctor(1)
        self.assertEqual(doctor_info["Name"], "Dr. Alice")
        self.assertEqual(doctor_info["Specialization"], "General Medicine")

    def test_update_doctor(self):
        doctor = Doctor(2, "Dr. Kumar", 38, "Pediatrics")
        self.service.add_doctor(doctor)
        self.service.update_doctor(2, "Family Medicine")

        doctor_info = self.service.get_doctor(2)
        self.assertEqual(doctor_info["Specialization"], "Family Medicine")

    def test_delete_doctor(self):
        doctor = Doctor(3, "Dr. Rosa", 50, "Surgery")
        self.service.add_doctor(doctor)
        self.service.delete_doctor(3)

        self.assertIsNone(self.service.get_doctor(3))

if __name__ == "__main__":
    unittest.main()
