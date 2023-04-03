import qrcode
import PySimpleGUI as sg

layout = [
    [sg.Text('Enter text to encode:')],
    [sg.Input(key='input_text')],
    [sg.Button('Generate QR Code'), sg.Button('Exit')]
]

window = sg.Window('QR Code Generator', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Generate QR Code':
        input_text = values['input_text']
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(input_text)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        filename = sg.popup_get_file('Save QR Code', save_as=True, default_extension='.png')
        if filename:
            img.save(filename)

window.close()
