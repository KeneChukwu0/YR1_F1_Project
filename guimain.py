from nicegui import app, ui
import getseasonschedule
import getsessionresults
import getsessionresultsadvanced

def main():
    #gui set so functions run in gui mode
    gui = True

    ui.page_title('F1 Results Lite') #page title
    ui.markdown('''# F1 Results Lite ''')
    #Buttons to choose which option wanted, different button executes different functions
    ui.button('Season Schedule', on_click= lambda: getseasonschedule.seasonschedule(gui))
    ui.button('Simple Session Result', on_click= lambda: getsessionresults.sessionresults(gui))
    ui.button('Advanced Session Result',on_click= lambda: getsessionresultsadvanced.advancedsessionresults(gui))
    #label for instructions
    ui.label('To clear results and reset the program, please refresh the browser page')


    ui.run()

main()