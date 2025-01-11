import flet
import os.path
import psutil
from elevate import elevate
from time import sleep
from flet import *
from tkinter.messagebox import showerror, showinfo


elevate( show_console = False )
def main( page: Page ):

    page.window.resizable = False
    page.window.width = 400
    page.window.height = 420
    page.title = 'Lupi DPI Launcher'
    page.window.icon = 'icon.ico'

    def OpenF( e = None ):
        os.system( 'explorer.exe DPI' )

    def Start( e = None ):
        os.system( 'cd DPI & general.bat' )
        contentContainer.content.controls.remove( StartBTN )
        contentContainer.content.controls.remove( empty1 )
        contentContainer.content.controls.remove( OpenBTN )
        contentContainer.content.controls.remove( empty2 )
        contentContainer.content.controls.remove( ChangeGeneralBTN )
        contentContainer.content.controls.append( StopBTN )
        page.update()

    def Stop( e = None ):
        os.system( 'taskkill /IM winws.exe /F' )
        contentContainer.content.controls.remove( StopBTN )
        contentContainer.content.controls.append( StartBTN )
        contentContainer.content.controls.append( empty1 )
        contentContainer.content.controls.append( empty2 )
        contentContainer.content.controls.append( OpenBTN )
        contentContainer.content.controls.append( ChangeGeneralBTN )
        page.update()

    def OpenGeneral( e = None ):
        os.system( 'cd DPI & list-general.txt' )

    empty1 = Container( height = 16 )
    empty2 = Container( height = 16 )

    StartBTN = FilledButton(
        text = 'Запустить DPI',
        width = 300,
        height = 40,
        style = ButtonStyle(
            bgcolor = '#33A3AD',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: Start()
    )

    StopBTN = FilledButton(
        text = 'Остановить DPI',
        width = 300,
        height = 40,
        style = ButtonStyle(
            bgcolor = '#33A3AD',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: Stop()
    )

    OpenBTN = FilledButton(
        text = 'Открыть Папку DPI',
        width = 300,
        height = 35,
        style = ButtonStyle(
            bgcolor = '#3e8790',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: OpenF()
    )

    ChangeGeneralBTN = FilledButton(
        text = 'Открыть Список Адресов',
        width = 300,
        height = 35,
        style = ButtonStyle(
            bgcolor = '#3e8790',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: OpenGeneral()
    )

    # container for content
    contentContainer = Container(
        width = 375,
        height = 420,
        padding = padding.only( left = 75, right = 75 ),
        bgcolor = '#444A4B',
        border_radius = 10,
        content = Column( alignment = 'center',
                   controls = [
                       StartBTN,
                       empty1,
                       empty2,
                       OpenBTN,
                       ChangeGeneralBTN]
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

    pass


if __name__ == '__main__':
    flet.app( target = main )