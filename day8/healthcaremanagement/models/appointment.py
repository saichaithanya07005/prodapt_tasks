class Appointment:
    def __init__(self, id, patient_id, doctor_id, date=None, reason=None):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.reason = reason

    def display_info(self):
        details = {
            "ID": self.id,
            "Patient ID": self.patient_id,
            "Doctor ID": self.doctor_id,
        }
        if self.date is not None:
            details["Date"] = self.date
        if self.reason is not None:
            details["Reason"] = self.reason
        return details
