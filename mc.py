import PySimpleGUI as sg

layout = [
    [sg.Text('Magic Chess Tracker', size=(30, 1), justification='center', font=('Helvetica', 20))],
    [sg.Text('Masukkan Nama Lawan:', size=(20, 1)), sg.InputText(key='opponent')],
    [sg.Text('Pilih Lawan Ke:', size=(20, 1)), sg.Listbox(values=[str(i) for i in range(1, 8)], size=(5, 7), key='round_num')],
    [sg.Text('Hasil Pertarungan:', size=(20, 1)), sg.Combo(['Menang', 'Kalah'], key='result')],
    [sg.Button('Catat Pertarungan', size=(20, 1))],
    [sg.Text('Daftar Pertemuan Lawan:', size=(30, 1))],
    [sg.Listbox(values=[], size=(40, 10), key='history')],
    [sg.Button('Reset'), sg.Button('Keluar')]
]


window = sg.Window('Magic Chess Tracker', layout)

# Menyimpan hasil pertemuan
match_history = []

# Loop untuk event
while True:
    event, values = window.read()
    
    
    if event == sg.WINDOW_CLOSED or event == 'Keluar':
        break
    
    #Catat Pertarungan
    if event == 'Catat Pertarungan':
        opponent = values['opponent']
        round_num = values['round_num'][0] if values['round_num'] else None
        result = values['result']
        
        if opponent and round_num and result:
            #Menyimpan hasil ke match history
            match_history.append(f"Lawan Ke-{round_num}: {opponent}, Hasil: {result}")
            window['history'].update(match_history)
        else:
            sg.popup('Masukkan Nama Lawan, Pilih Nomor, dan Hasil Pertarungan!', title='Error')

    
    if event == 'Reset':
        match_history.clear()
        window['history'].update(match_history)


window.close()
