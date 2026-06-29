import fastf1

year = int(input("Select Year \n"))
race = input("Select race \n")
weekendsession = input("Select session \n")
session = fastf1.get_session(year, race,weekendsession)
session.load()
session.laps
fastest_lap = session.laps.pick_fastest()
print(fastest_lap)
