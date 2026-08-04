import fastf1
from nicegui import ui

def advancedsessionresults(gui):

    if gui == False:
        year = int(input("Select Year \n"))
        race = input("Select race \n")
        weekendsession = input("Select session \n")
        session = fastf1.get_session(year, race,weekendsession)
        session.load()
        print(session.results.iloc[0:20].loc[:,  ['FullName', 'TeamName', 'ClassifiedPosition','GridPosition','Status','Points','Laps']])
    else:
        i = ui.number(label='Year')
        j = ui.input(label='Race').props('clearable')
        k = ui.input(label='Session').props('clearable')
        ui.button('Submit', on_click=lambda: outputresult(i,j,k))

def outputresult(i,j,k):
    year = int(i.value)
    race = str(j.value)
    weekendsession = str(k.value)
    session = fastf1.get_session(year, race, weekendsession)
    session.load()
    ui.aggrid.from_pandas(session.results.iloc[0:20].loc[:, ['FullName', 'TeamName', 'ClassifiedPosition','GridPosition','Status','Points','Laps']])

#advancedsessionresults(gui=False)