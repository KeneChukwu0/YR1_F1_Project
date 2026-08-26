import fastf1
from nicegui import ui


def seasonschedule(gui):

    if gui == False:
        #CLI code

        #Take input
        year = int(input("Select Year \n"))
        #get data from API
        schedule = fastf1.get_event_schedule(year, backend='ergast')
        #Output to CLI
        print(schedule.loc[:,['RoundNumber','Country','EventDate']])
    else:
        #GUI code

        #Take input
        i = ui.number(label='Year')
        #Submit input and call outputschedule func
        ui.button('Submit', on_click=lambda: outputschedule(i))


def outputschedule(i):
    year = int(i.value)
    print(year)
    #get data from API
    schedule = fastf1.get_event_schedule(year, backend='ergast')
    #ouput to GUI
    ui.aggrid.from_pandas(schedule.loc[:, ['RoundNumber', 'Country', 'EventDate']]).classes('max-h-100')