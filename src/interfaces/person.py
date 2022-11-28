'''
Person Object that is parsed from each website
'''
class Person:
  def __init__(self, name, link, state, status, license, source, speciality):
    self.name = name
    self.link = link
    self.state = state
    self.status = status
    self.license = license
    self.source = source
    self.speciality = speciality
    self.checked = False