from utils.logger import log

class AppointmentService:
    def __init__(self, datastore):
        self.datastore = datastore

    def add_appointment(self, appointment):
        self.datastore["appointments"][appointment.id] = appointment
        log(f"Scheduled appointment {appointment.id} for patient {appointment.patient_id} with doctor {appointment.doctor_id}")

    def get_appointment(self, appointment_id):
        appointment = self.datastore["appointments"].get(appointment_id)
        return appointment.display_info() if appointment else None

    def update_appointment(self, appointment_id, date=None, reason=None):
        if appointment_id in self.datastore["appointments"]:
            appointment = self.datastore["appointments"][appointment_id]
            if date is not None:
                appointment.date = date
            if reason is not None:
                appointment.reason = reason
            log(f"Updated appointment {appointment_id}")

    def delete_appointment(self, appointment_id):
        if appointment_id in self.datastore["appointments"]:
            del self.datastore["appointments"][appointment_id]
            log(f"Deleted appointment {appointment_id}")
