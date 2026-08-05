import fastf1

def sessionfastestlap():
    year = int(input("Select Year \n"))
    race = input("Select race \n")
    weekendsession = input("Select session \n")

    session = fastf1.get_session(2025, 'Monza', 'R')
    session.load(telemetry=True, laps=True, weather=False)

    # Pick the overall fastest lap
    fastest = session.laps.pick_fastest()

    print(f"Driver: {fastest['Driver']}")
    print(f"Lap Time: {fastest['LapTime']}")

#sessionfastestlap()