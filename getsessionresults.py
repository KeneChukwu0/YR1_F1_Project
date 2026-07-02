import fastf1

def sessionresults():
    year = int(input("Select Year \n"))
    race = input("Select race \n")
    weekendsession = input("Select session \n")
    session = fastf1.get_session(year, race,weekendsession)
    session.load()
    print(session.results.iloc[0:20].loc[:, ['FullName', 'TeamName','ClassifiedPosition']])