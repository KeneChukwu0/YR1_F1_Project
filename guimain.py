from nicegui import app, ui
import getseasonschedule
import getsessionresults
import getsessionresultsadvanced

def main():
    gui = True

    ui.button('Season Schedule', on_click= lambda: getseasonschedule.seasonschedule(gui))
    ui.button('Simple Session Result', on_click= lambda: getsessionresults.sessionresults(gui))
    ui.button('Advanced Session Result',on_click= lambda: getsessionresultsadvanced.advancedsessionresults(gui))

    ui.run()

main()