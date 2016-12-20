import pickle
ThisPatient = PatientRecord()
PatientFile = open("Patients.DAT","rb+")
Address = hash(ThisPatient.PatientID)
PatientFileseek(Address)
pickle.dump(ThisPatient,PatientFile)
PatientFile.close()
PatientFile = open("Patients.DAT","rb")
