# #######################
# LupiDPI ( Windows Edition ) V1.4.1
# by netervezer
# #######################
import locale
import ctypes
import psutil
from os import system
from elevate import elevate
from subprocess import call
from tkinter.messagebox import showerror
from flet import FilledButton, Dropdown, Container, Page, ButtonStyle, RoundedRectangleBorder, Text, \
    FontWeight, dropdown, padding, Column, Row, app

windll = ctypes.windll.kernel32
translations = {
    'ru': {
        'title': 'Lupi DPI',
        'lang': 'Русский',
        'start_button': 'Запустить Обход DPI',
        'install_button': 'Установить Службу',
        'remove_button': 'Удалить Службу',
        'warning': 'Это окно можно закрыть, но не закрывайте открывшийся терминал!',
        'stop_button': 'Остановить Обход',
        'open_folder_button': 'Открыть Папку DPI',
        'open_general_button': 'Открыть Список Адресов',
        'info_button': 'Руководство',
        'alt_start': 'Параметры Запуска',
        'alt1': 'Alt Запуск 1',
        'alt2': 'Alt Запуск 2',
        'alt3': 'Alt Запуск 3',
        'alt4': 'Alt Запуск 4',
        'alt5': 'Alt Запуск 5',
        'iran': 'Стандартный Запуск (Иран)',
        'default': 'Стандартный Запуск',
    },
    'en': {
        'title': 'Lupi DPI',
        'lang': 'English',
        'start_button': 'Start DPI Bypass',
        'install_button': 'Install Service',
        'remove_button': 'Remove Service',
        'warning': 'You can close this window, but do not close the terminal that opened!',
        'stop_button': 'Stop Bypass',
        'open_folder_button': 'Open DPI Folder',
        'open_general_button': 'Open Address List',
        'info_button': 'Guide',
        'alt_start': 'Start Options',
        'alt1': 'Alt Start 1',
        'alt2': 'Alt Start 2',
        'alt3': 'Alt Start 3',
        'alt4': 'Alt Start 4',
        'alt5': 'Alt Start 5',
        'iran': 'Default Start (Iran)',
        'default': 'Default Start',
        'error_t': 'Error',
    },
    'fa': {
        'title': 'Lupi DPI',
        'lang': 'فارسی',
        'start_button': 'شروع دور زدن DPI',
        'install_button': 'نصب سرویس',
        'remove_button': 'حذف سرویس',
        'warning': 'شما می توانید این پنجره را ببندید، اما ترمینال باز شده را نبندید!',
        'stop_button': 'متوقف کردن دور زدن',
        'open_folder_button': 'باز کردن پوشه DPI',
        'open_general_button': 'باز کردن لیست آدرس ها',
        'info_button': 'راهنما',
        'alt_start': 'گزینه های شروع',
        'alt1': 'Alt شروع 1',
        'alt2': 'Alt شروع 2',
        'alt3': 'Alt شروع 3',
        'alt4': 'Alt شروع 4',
        'alt5': 'Alt شروع 5',
        'iran': 'شروع پیش فرض (ایران)',
        'default': 'شروع پیش فرض',
        'error_t': 'خطا',
    }
}


elevate( show_console = False )
def update_text( language ):
    return translations[language]

def main( page: Page ):

    page.window.resizable = False
    page.window.width = 400
    page.window.height = 580
    page.title = 'Lupi DPI Bypass'

    if locale.windows_locale[ windll.GetUserDefaultUILanguage() ][:2] == 'fa':
        selected_language = 'fa'
    elif locale.windows_locale[ windll.GetUserDefaultUILanguage() ][:2] == 'ru':
        selected_language = 'ru'
    else:
        selected_language = 'en'
    text = update_text( selected_language )

    def change_language( e ):
        nonlocal selected_language
        selected_language = e.control.value
        text = update_text( selected_language )

        StartBTN.text = text[ 'start_button' ]
        InstallBTN.text = text[ 'install_button' ]
        RemoveBTN.text = text[ 'remove_button' ]
        WarningLabel.text = text[ 'warning' ]
        StopBTN.text = text[ 'stop_button' ]
        OpenBTN.text = text[ 'open_folder_button' ]
        ChangeGeneralBTN.text = text[ 'open_general_button' ]
        InfoBTN.text = text[ 'info_button' ]
        LanguageDropdown.label = text[ 'lang' ]
        AltStarts.label = text[ 'alt_start' ]
        AltStarts.options = [
            dropdown.Option( key = 'default', text = text[ 'default' ] ),
            dropdown.Option( key = 'iran', text = text[ 'iran' ] ),
            dropdown.Option( key = 'alt1', text = text[ 'alt1' ] ),
            dropdown.Option( key = 'alt2', text = text[ 'alt2' ] ),
            dropdown.Option( key = 'alt3', text = text[ 'alt3' ] ),
            dropdown.Option( key = 'alt4', text = text[ 'alt4' ] ),
            dropdown.Option( key = 'alt5', text = text[ 'alt5' ] ),
        ]
        page.update()

    def OpenInfo( e = None ):
        call( 'info.html', shell = True )

    def OpenF( e = None ):
        call( 'explorer.exe DPI', shell = True )

    def Start( e = None ):
        A = []
        for proc in psutil.process_iter():
            name = proc.name()
            A.append( name )
        if 'winws.exe' in A:
            if selected_language == 'en':
                showerror( title = 'Error',
                           message = 'You already have DPI bypass service installed!\nPlease remove it first before starting a new one!' )
            elif selected_language == 'ru':
                showerror( title = 'Ошибка',
                          message = 'У вас уже установлена служба обхода DPI!\nСперва удалите её, прежде чем запустить новую!' )
            else:
                showerror( title = 'خطا',
                          message = 'شما قبلاً سرویس بای پس DPI را نصب کرده اید!\n' 'لطفاً قبل از شروع یک مورد جدید، ابتدا آن را حذف کنید!' )
        else:
            if AltStarts.value == 'alt1':
                system( 'cd DPI & alt1.bat' )
            elif AltStarts.value == 'alt2':
                system( 'cd DPI & alt2.bat' )
            elif AltStarts.value == 'alt3':
                system( 'cd DPI & alt3.bat' )
            elif AltStarts.value == 'alt4':
                system( 'cd DPI & alt4.bat' )
            elif AltStarts.value == 'alt5':
                system( 'cd DPI & alt5.bat' )
            elif AltStarts.value == 'iran':
                system( 'cd DPI & iran.bat' )
            else:
                system( 'cd DPI & general.bat' )
            contentContainer.content.controls.remove( StartBTN )
            contentContainer.content.controls.remove( empty1 )
            contentContainer.content.controls.remove( empty2 )
            contentContainer.content.controls.remove( AltStarts )
            contentContainer.content.controls.remove( InstallBTN )
            contentContainer.content.controls.remove( RemoveBTN )
            contentContainer.content.controls.remove( empty3 )
            contentContainer.content.controls.remove( OpenBTN )
            contentContainer.content.controls.remove( ChangeGeneralBTN )
            contentContainer.content.controls.remove( InfoBTN )
            contentContainer.content.controls.remove( LanguageDropdown )
            contentContainer.content.controls.append( StopBTN )
            contentContainer.content.controls.append( WarningLabel )
            contentContainer.content.controls.append( empty1 )
            contentContainer.content.controls.append( InfoBTN )
            contentContainer.content.controls.append( LanguageDropdown )
            page.update()

    def Stop( e = None ):
        try:
            system( 'taskkill /IM winws.exe /F' )
        except:
            pass
        contentContainer.content.controls.remove( StopBTN )
        contentContainer.content.controls.remove( empty1 )
        contentContainer.content.controls.remove( WarningLabel )
        contentContainer.content.controls.remove( InfoBTN )
        contentContainer.content.controls.remove( LanguageDropdown )
        contentContainer.content.controls.append( StartBTN )
        contentContainer.content.controls.append( AltStarts )
        contentContainer.content.controls.append( empty1 )
        contentContainer.content.controls.append( InstallBTN )
        contentContainer.content.controls.append( RemoveBTN )
        contentContainer.content.controls.append( empty2 )
        contentContainer.content.controls.append( OpenBTN )
        contentContainer.content.controls.append( ChangeGeneralBTN )
        contentContainer.content.controls.append( empty3 )
        contentContainer.content.controls.append( InfoBTN )
        contentContainer.content.controls.append( LanguageDropdown )
        page.update()

    def OpenGeneral( e = None ):
        system( 'cd DPI & list-general.txt' )

    def Install( e = None ):
        system( 'cd DPI & start service_install.bat' )

    def Remove( e = None ):
        system( 'cd DPI & start service_remove.bat' )

    empty1 = Container( height = 16 )
    empty2 = Container( height = 16 )
    empty3 = Container( height = 16 )

    LanguageDropdown = Dropdown(
        label = text[ 'lang' ],
        border_color = '#33A3AD',
        border_radius = 10,
        width = 300,
        height = 50,
        options = [
            dropdown.Option( key = 'en', text = 'English' ),
            dropdown.Option( key = 'ru', text = 'Русский' ),
            dropdown.Option( key = 'fa', text = 'فارسی' ),
        ],
        on_change = change_language
    )

    StartBTN = FilledButton(
        text = text[ 'start_button' ],
        width = 300,
        height = 50,
        style = ButtonStyle(
            bgcolor = '#33A3AD',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: Start()
    )

    InstallBTN = FilledButton(
        text = text[ 'install_button' ],
        width = 300,
        height = 40,
        style = ButtonStyle(
            bgcolor = '#33A3AD',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: Install()
    )

    RemoveBTN = FilledButton(
        text = text[ 'remove_button' ],
        width = 300,
        height = 40,
        style = ButtonStyle(
            bgcolor = '#33A3AD',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: Remove()
    )

    WarningLabel = Text(
        text[ 'warning' ],
        color = '#C6C6C6',
        weight = FontWeight.BOLD
    )

    StopBTN = FilledButton(
        text = text[ 'stop_button' ],
        width = 300,
        height = 40,
        style = ButtonStyle(
            bgcolor = '#33A3AD',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: Stop()
    )

    OpenBTN = FilledButton(
        text = text[ 'open_folder_button' ],
        width = 300,
        height = 35,
        style = ButtonStyle(
            bgcolor = '#3e8790',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: OpenF()
    )

    ChangeGeneralBTN = FilledButton(
        text = text[ 'open_general_button' ],
        width = 300,
        height = 35,
        style = ButtonStyle(
            bgcolor = '#3e8790',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: OpenGeneral()
    )

    InfoBTN = FilledButton(
        text = text[ 'info_button' ],
        width = 300,
        height = 35,
        style = ButtonStyle(
            bgcolor = '#3e8790',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: OpenInfo()
    )

    AltStarts = Dropdown(
        border_color = '#33A3AD',
        border_radius = 10,
        label = text[ 'alt_start' ],
        width = 300,
        height = 50,
        options = [
            dropdown.Option( key = 'default', text = text['default'] ),
            dropdown.Option( key = 'iran', text = text['iran'] ),
            dropdown.Option( key = 'alt1', text = text['alt1'] ),
            dropdown.Option( key = 'alt2', text = text['alt2'] ),
            dropdown.Option( key = 'alt3', text = text['alt3'] ),
            dropdown.Option( key = 'alt4', text = text['alt4'] ),
            dropdown.Option( key = 'alt5', text = text['alt5'] ),
        ],
    )

    # container for content
    contentContainer = Container(
        width = 375,
        height = 580,
        padding = padding.only( left = 55, right = 55 ),
        bgcolor = '#444A4B',
        border_radius = 10,
        content = Column( alignment = 'center',
                   controls = [
                       StartBTN,
                       AltStarts,
                       empty1,
                       InstallBTN,
                       RemoveBTN,
                       empty2,
                       OpenBTN,
                       ChangeGeneralBTN,
                       empty3,
                       InfoBTN,
                       LanguageDropdown
                   ]
                )
    )

    # main container ( main window )
    mainContainer = Container(
        expand = True,
        margin = -10,
        padding = 5,
        bgcolor = '#33A3AD',
        content = Row(
            controls = [
                contentContainer
            ]
        )
    )

    ###
    page.add( mainContainer )
    page.update()


if __name__ == '__main__':
    app( target = main )
