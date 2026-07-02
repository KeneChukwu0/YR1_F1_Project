import fastf1

def seasonschedule():
    year = int(input("Select Year \n"))
    schedule = fastf1.get_event_schedule(year,backend='ergast')

    print(schedule.loc[:,['RoundNumber','Country','EventDate']])