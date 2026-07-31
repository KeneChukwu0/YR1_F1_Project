import fastf1
from nicegui import ui


def seasonschedule(gui):

    if gui == False:
        year = int(input("Select Year \n"))
        schedule = fastf1.get_event_schedule(year, backend='ergast')
        print(schedule.loc[:,['RoundNumber','Country','EventDate']])
    else:
        i = ui.number(label='Year')
        ui.button('Submit', on_click=lambda: outputschedule(i))


def outputschedule(i):
    year = int(i.value)
    print(year)
    schedule = fastf1.get_event_schedule(year, backend='ergast')
    ui.aggrid.from_pandas(schedule.loc[:, ['RoundNumber', 'Country', 'EventDate']]).classes('max-h-100')