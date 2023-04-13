class School():
  def __init__(self, level, numberOfStudents):
    self.level = level
    self.numberOfStudents = numberOfStudents

  def getLevel(self):
    return self.level
  def getNumberOfStudents(self):
    return self.numberOfStudents
  def setNumberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents
  def __repr__(self):
    return "A {} with {} students".format(self.level, self.numberOfStudents)

schoolTest = School("Secondary", 1200)
print(schoolTest)

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__("primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy
  def getPickupPolicy(self):
    return self.pickupPolicy
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + " The pickup policy is {pickupPolicy} : ".format(pickupPolicy = self.pickupPolicy)

primarySchoolTest = PrimarySchool("San juanito", 50000, "Pick up is at 6 on clock only by parents")
print(primarySchoolTest)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__("HighSchool", numberOfStudents)
    self.sportsTeams = sportsTeams
  def getSportsTeams(self):
    return self.sportsTeams
  def __repr__(self):
    sports = super().__repr__()
    return "{} The sport teams are: {}".format(sports, self.sportsTeams)

highSchoolTest = HighSchool("Los tiburones de madagascar", 352240, ["Tiburoncines", "Mamahuevitos"])
print(highSchoolTest)