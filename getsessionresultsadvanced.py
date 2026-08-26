import fastf1
from nicegui import ui

def advancedsessionresults(gui):

    if gui == False:
        #CLI code

        #Take input
        year = int(input("Select Year \n"))
        race = input("Select race \n")
        weekendsession = input("Select session \n")
        #get data from API
        session = fastf1.get_session(year, race,weekendsession)
        session.load()
        #Output to CLI
        print(session.results.iloc[0:20].loc[:,  ['FullName', 'TeamName', 'ClassifiedPosition','GridPosition','Status','Points','Laps']])
    else:
        #GUI code

        #Take input
        i = ui.number(label='Year')
        j = ui.input(label='Race').props('clearable')
        k = ui.input(label='Session').props('clearable')
        #Submit button that calls outputresult func
        ui.button('Submit', on_click=lambda: outputresult(i,j,k))

def outputresult(i,j,k):
    year = int(i.value)
    race = str(j.value)
    #get data from API
    weekendsession = str(k.value)
    session = fastf1.get_session(year, race, weekendsession)
    session.load()
    #Output to GUI
    ui.aggrid.from_pandas(session.results.iloc[0:20].loc[:, ['FullName', 'TeamName', 'ClassifiedPosition','GridPosition','Status','Points','Laps']])

#advancedsessionresults(gui=False)