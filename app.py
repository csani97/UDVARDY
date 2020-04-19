import flask as Flask
import uuid

app = Flask(__name__)

###########HOSPITAL CLASS###########
class Hospital:
    def __init__(self, id,  name, capacity):
        self.id_ = uuid.uuid1()
        self.name = name
        self.capacity = capacity
        self.staff = []
        self.patient = []

    def occupancy(self):
        return 100 * len(self.patients) / self.capacity

    def admission(self, name, dob):
        x = Patient(name, dob)
        self.patient.append(x)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'capacity': self.capacity,
            'occupancy': self.occupancy(),
        }

###########QUARANTINE CLASS###########
class Quarantine:
    def __init__(self, id, name, capacity):
        self.id_ = uuid.uuid1()
        self.name = name
        self.capacity = capacity
        self.staff = []
        self.patient = []

    def occupancy(self):
        return 100 * len(self.patients) / self.capacity

    def admission(self, id_):
        x = Patient(id_)
        self.patient.append(x)

    def area(self, id_):
        return {
            'capacity': self.capacity,
            'name': self.name,
            'patient': self.patient,
            'staff': self.staff,
            'occupancy': self.occupancy(),
        }

###########PATIENT STATUS CLASS###########
class PatientStatus:
    status = ["discharged", "isolation", "dead"]

###########PATIENT CLASS###########
class Patient:
    def __init__(self, id_, name, dob, status):
        self.id_ = uuid.uuid1()
        self.name = name
        self.dob = dob
        self.status = PatientStatus.status[]

    def admit(self, facility):
        if self.status is PatientStatus.status[2]:
            return("Patient is dead")
        if facility.occupancy >= 100:
            return("Full")
        else:
            facility.patient.append(self)
            facility.status = PatientStatus.status[1]

    def display(self):
        return {
            'name': self.name,
            'status': self.status.value,
        }

    def discharge(self):
        if self.status is PatientStatus.status[2]:
            print("Patient is dead")
        else:
            facility.patient.remove(self)
            self.status = PatientStatus.status[0]

###########STAFF TYPE CLASS###########
class StaffPosition:
    position = ["doctor", "nurse"]

###########STAFF CLASS###########
class Staff:
    def __init__(self, id_, name, dob, position, workplace=None):
        self.id_ = uuid.uuid1()
        self.name = name
        self.dob = dob
        self.position = StaffPosition.position
        self.workplace = workplace

    def display(self):
        return {
            'id': self.id,
            'name': self.name,
            'dob': self.dob,
            'position': [self.position if position != None else None],
            'workplace': self.workplace
        }

    def add_to_workplace(self, facility):
        if self.workplace 1 = None:
            self.workplace.remove(self)
        else:
            facility.staff.append(self)
        self.workplace = facility

###########SYSTEM CLASS###########
class System:
    def __init__(self):
        self.hospitals = {}
        self.quarantines = {}
        self.patient = {}
        self.staff = {}

    def get_hospitals(self):
        return self.hospitals

    def add_hospital(self, name, capacity):
        x = Hospital(name, capacity)
        self.hospitals.append(x)

    def get_hospital_by_id(self, id_):
        for x in self.hospitals:
            if(x.id == id_):
                return x
        return None

    def delete_hospital(self, id_):
        x = self.get_hospital_by_id(id_)
        if(x != None):
            self.hospitals.remove(x)
        return x != None

    def get_quarantines(self):
        return self.quarantines

    def add_quarantine(self, name, capacity):
        x = Quarantine(name, capacity)
        self.quarantines.append(x)

    def get_quarantine_by_id(self, id_):
        for x in self.quarantines:
            if(x.id == id_):
                return x
        return None

    def delete_quarantine(self, id_):
        x = self.get_quaranitne_by_id(id_)
        if(x != None):
            self.quarantine.remove(x)
        return x != None

    def get_staff(self):
        return self.staff

    def get_staff_by_id(self, id_):
        for x in self.staff:
            if(x.id == id_):
                return x
        return None

    def delete_staff(self, id_):
        x = self.get_staff_by_id(id_)
        if(x != None):
            self.staff.remove(x)
        return x != None

    def facility_id(facility_id):
        if facility_id in hospitals:
            return self.get_hospital_by_id(facility_id)
        if facility_id in quarantines:
            return self.get_quarantine_by_id(facility_id)
        else:
            return None

###########HOSPITAL MANAGEMENT###########
@app.route("/hospital", methods=["POST"])
def add_hospital():
    System.add_hospital(request.args.get('name'), request.args.get('capacity'))
    return jsonify(f"Added a new hospital called {request.args.get('name')} with capacity {request.args.get('capacity')}")


@app.route("/hospital/<hospital_id>", methods=["GET"])
def hospital_info(hospital_id):
    x = System.get_hospital_by_id(hospital_id)
    if(x != None):
        return jsonify(Hospital.serialize())
    return jsonify(
            success=False,
            message="Hospital not found")


@app.route("/hospital/<hospital_id>/patient", methods=["POST"])
def admit_patient(hospital_id):
    x = System.get_hospital_by_id(hospital_id)
    if(x != None):
        Hospital.admission(request.args.get(
            'name'), request.args.get('dob'))
    return jsonify(
            success=x != None,
            message="Hospital not found")


@app.route("/hospital/<hospital_id>", methods=["DELETE"])
def delete_hospital(hospital_id):
    result = System.delete_hospital(hospital_id)
    if(result):
        message = f"Hospital with id{hospital_id} was deleted"
    else:
        message = "Hospital not found"
    return jsonify(
            success=result,
            message=message)


@app.route("/hospitals", methods=["GET"])
def all_hospitals():
    return jsonify(hospitals=[Hospital.serialize() for x in System.get_hospitals()])

###########QUARANTINE MANAGEMENT###########
@app.route("/quarantine", methods=["POST"])
def add_quarantine():
    System.add_quarantine(request.args.get(
        'name'), request.args.get('capacity'))
    return jsonify(f"Added a new quarantin called {request.args.get('name')} with capacity {request.args.get('capacity')}")


@app.route("/quarantine/<quarantine_id>", methods=["GET"])
def quarantine_info(quarantine_id):
    x = System.get_quarantine_by_id(quarantine_id)
    if(x != None):
        return jsonify(Quarantine.area(x))
    return jsonify(
            success=False,
            message="Quarantine not found")


@app.route("/quarantine/<quarantine_id>/patient_id", methods=["POST"])
def admit_patient(quarantine_id, patient_id):
    x = QUARANTINES[quarantine_id]
    y = PATIENTS[patient_id]
    Patient.admit(x)
    if(x, y != None):
        return jsonify(Patient.display)
    else:
        return jsonify(
            success=x, y != None,
            message="Quarantine or patient not found or full or patient is dead")


@app.route("/quarantine/<quarantine_id>", methods=["DELETE"])
def delete_quarantine(quarantine_id):
    result = System.delete_hospital(hospital_id)
    if Quarantine.occupancy == 0:
        return System.delete_hospital(hospital_id)
        KEEEELLLLL VALAMI
    else:
        message = "Hospital not found"
    return jsonify(
            success=result,
            message=message)


@app.route("/quarantines", methods=["GET"])
def all_quarantines():
    return jsonify(quarantines=[Quarantine.area() for x in System.get_quarantines()])

###########STAFF MANAGEMENT###########
@app.route('/staff', methods=['POST'])
def add_new_staff():
        name, dob = request.args.get('name'), request.arg('dob'))
        x=Staff(name, dob)
        System.staff.append(x)
        return jsonify("Patient added")

@app.route("/staff", methods = ["GET"])
def staff_info():
    return jsonify(staff = [Staff.display() for x in System.get_staff()])

@app.route("/patient/<staff_id>", methods = ['PUT'])
def assign_staff(staff_id):
    x=request.args['facility_id']
    y=System.facility_id(x)
    if staff_id not in staff or facility_id is None:
        return None
    else:
        Staff.add_to_workplace(y)

@app.route("/staff/<staff_id>", methods = ["DELETE"])
def delete_staff(staff_id):
    result=System.delete_staff(staff_id)
    if(result):
        message=f"Staff with id{staff_id} was deleted"
    else:
        message="Staff not found"
    return jsonify(
            success = result,
            message = message)

###########PATIENT MANAGEMENT###########
@app.route('/patient', methods = ['POST'])
def add_new_patient():
        name, dob=request.args.get('name'), request.arg('dob'))
        x=Patient(name, dob)
        System.patient.append(x)
        return jsonify("Patient added")

@app.route('/patient/<patient_id>/admit/<facility_id>', methods=['PUT'])
def admit_patient(patient_id, facility_id):
    x=facility_id(facility_id)
    if x is None:
        return "No such a facility"
    if patient_id in patients:
        y=patients[patient_id]
        y.admit(x)

@app.route('/patient/<patient_id>/discharge/<facility_id>', methods=['PUT'])
def discharge_patient(patient_id, facility_id):
    x=facility_id(facility_id)
    if x is None:
        return "No such a facility"
    if patient_id in patients:
        y=patients[patient_id]
        y.discharge(x)

@app.route('/patient/<patient_id>/diagnosis', methods=['POST'])
def diagnose(patient_id):
    if patient_id in patients:
        x=patients[patient_id]
    else:
        print('No such patietn')
    if random.random() * 100 <= 10:
        x.admit(quarantine)
        return jsonify("Admitted")

@app.route('/patient/<patient_id>/diagnosis', methods=['POST'])
def diagnose(patient_id):
    if patient_id in patients:
        x=patients[patient_id]
    else:
        print('No such patietn')
    if random.random() * 100 <= 97:
        x.discharge(quarantine)
        return jsonify("Discharged")

###########STATS###########
@app.route("/stats", methods=["GET"])
def statistics():
    capacity_count=Hospital.capacity + Quarantine.capacity
    patient_count=Quarantine.patient + Hospital.patient
    patient_infected=0
    if PatientStatus.status[1]
        x=patient_infected += PatientStatus.status[1]
    else:
        x=0
    patient_mixture=(patient_infected / patient_count) * 100

if __name__ == "__main__":
    app.run(debug=True)
