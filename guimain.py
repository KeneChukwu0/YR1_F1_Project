from nicegui import app, ui
import getseasonschedule
import getsessionresults
import getsessionresultsadvanced

def main():
    gui = True

    ui.page_title('F1 Results Lite')
    ui.markdown('''# F1 Results Lite ''')
    ui.button('Season Schedule', on_click= lambda: getseasonschedule.seasonschedule(gui))
    ui.button('Simple Session Result', on_click= lambda: getsessionresults.sessionresults(gui))
    ui.button('Advanced Session Result',on_click= lambda: getsessionresultsadvanced.advancedsessionresults(gui))
    ui.label('To clear results and reset the program, please refresh the browser page')


    ui.run()

main()