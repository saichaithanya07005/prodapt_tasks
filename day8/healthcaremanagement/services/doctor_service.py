from utils.logger import log

class DoctorService:
    def __init__(self, datastore):
        self.datastore = datastore

    def add_doctor(self, doctor):
        self.datastore["doctors"][doctor.id] = doctor
        log(f"Added doctor {doctor.id}: {doctor.name}")

    def get_doctor(self, doctor_id):
        doctor = self.datastore["doctors"].get(doctor_id)
        return doctor.display_info() if doctor else None

    def update_doctor(self, doctor_id, specialization):
        if doctor_id in self.datastore["doctors"]:
            self.datastore["doctors"][doctor_id].specialization = specialization
            log(f"Updated doctor {doctor_id} specialization to {specialization}")

    def delete_doctor(self, doctor_id):
        if doctor_id in self.datastore["doctors"]:
            del self.datastore["doctors"][doctor_id]
            log(f"Deleted doctor {doctor_id}")
