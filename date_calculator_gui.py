import PySimpleGUI as sg
import re
from date_calculator import date_calculator

if __name__ == "__main__":
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('[ Date Calculator ]', font=('Helvetica', 20))],
                [sg.Input(key='date', size=(10,1)), sg.CalendarButton('Select Start Date',  target='date', format='%d/%m/%Y', default_date_m_d_y=(1,None,2023))],
                [sg.Text('Years'), sg.InputText(key="years", size=(5,1), default_text=None)],
                [sg.Text('Months'), sg.InputText(key="months", size=(5,1))],
                [sg.Text('Weeks'), sg.InputText(key="weeks", size=(5,1))],
                [sg.Text('Days'), sg.InputText(key="days", size=(5,1))],
                [sg.Text(key='report', font=('Helvetica', 10) , visible=False)],
                [sg.Text(key='result', font=('Helvetica', 18) , visible=False)],
                [sg.Button('Calculate'), sg.Button('Cancel'), sg.Button('Exit')],
            ]
    # Create the Window
    window = sg.Window('Date Calculator', layout, finalize=True, element_justification="c")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
            break
        if event == "Cancel":
            window["result"].update(visible=False)
            window["report"].update(visible=False)
            for key in values.keys():
                if key != "Select Start Date":
                    window[key].update("")
                    values[key] = ""
        if event == "Calculate":
            date = values["date"]
            years = values["years"]
            months = values["months"]
            weeks = values["weeks"]
            days = values["days"]
            report = "Is the date"
            for key, value in values.items():
                if key == "date" or key == "Select Start Date":
                    continue
                elif value and not value.isdigit():
                    sg.popup("The entry should be a number!")
            if not date or not re.compile(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$").match(date):
                sg.popup("Invalid date")
            else:
                new_date, report, day_of_week = date_calculator(date, years, months, weeks, days)
                window["report"].update(f"{report} after {date}", visible=True)
                window["result"].update(f"{new_date}, {day_of_week}", visible=True)
    window.close()
