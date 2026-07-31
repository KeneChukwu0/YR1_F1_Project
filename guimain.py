from nicegui import app, ui
import getseasonschedule
import getsessionfastestlap
import getsessionresults

def main():
    gui = True

    ui.button('Season Schedule', on_click= lambda: getseasonschedule.seasonschedule(gui))
    ui.button('Session Result', on_click= lambda: getsessionresults.sessionresults(gui))

    ui.button('Clear',on_click= lambda: clear())

    ui.run()

def clear():
    main()

main()