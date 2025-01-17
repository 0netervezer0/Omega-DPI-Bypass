# #######################
# LupiDPI ( Windows Edition ) V1.2.1
# by netervezer
# #######################

import flet
import os
from elevate import elevate
from flet import *
from pygments.styles.gh_dark import GRAY_3

elevate( show_console = False )
def main( page: Page ):

    page.window.resizable = False
    page.window.width = 400
    page.window.height = 520
    page.title = 'Lupi DPI Launcher'
    page.window.icon = 'icon.ico'

    def OpenInfo( e = None ):
        os.system( 'info.html' )

    def OpenF( e = None ):
        os.system( 'explorer.exe DPI' )

    def Start( e = None ):
        os.system( 'cd DPI & general.bat' )
        contentContainer.content.controls.remove( StartBTN )
        contentContainer.content.controls.remove( empty1 )
        contentContainer.content.controls.remove( empty2 )
        contentContainer.content.controls.remove( InstallBTN )
        contentContainer.content.controls.remove( RemoveBTN )
        contentContainer.content.controls.remove( empty3 )
        contentContainer.content.controls.remove( OpenBTN )
        contentContainer.content.controls.remove( ChangeGeneralBTN )
        contentContainer.content.controls.remove( InfoBTN )
        contentContainer.content.controls.append( StopBTN )
        contentContainer.content.controls.append( WarningLabel )
        contentContainer.content.controls.append( empty1 )
        contentContainer.content.controls.append( InfoBTN )
        page.update()

    def Stop( e = None ):
        os.system( 'taskkill /IM winws.exe /F' )
        contentContainer.content.controls.remove( StopBTN )
        contentContainer.content.controls.remove( empty1 )
        contentContainer.content.controls.remove( WarningLabel )
        contentContainer.content.controls.remove( InfoBTN )
        contentContainer.content.controls.append( StartBTN )
        contentContainer.content.controls.append( empty1 )
        contentContainer.content.controls.append( InstallBTN )
        contentContainer.content.controls.append( RemoveBTN )
        contentContainer.content.controls.append( empty2 )
        contentContainer.content.controls.append( OpenBTN )
        contentContainer.content.controls.append( ChangeGeneralBTN )
        contentContainer.content.controls.append( empty3 )
        contentContainer.content.controls.append( InfoBTN )
        page.update()

    def OpenGeneral( e = None ):
        os.system( 'cd DPI & list-general.txt' )

    def Install( e = None ):
        os.system( 'cd DPI & start service_install.bat' )

    def Remove( e = None ):
        os.system('cd DPI & start service_remove.bat')

    empty1 = Container( height = 16 )
    empty2 = Container( height = 16 )
    empty3 = Container( height = 16 )


    # buttons
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

    InstallBTN = FilledButton(
        text = 'Установить Службу DPI',
        width = 300,
        height = 40,
        style = ButtonStyle(
            bgcolor = '#33A3AD',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: Install()
    )

    RemoveBTN = FilledButton(
        text = 'Удалить Службу DPI',
        width = 300,
        height = 40,
        style = ButtonStyle(
            bgcolor = '#33A3AD',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: Remove()
    )

    WarningLabel = Text(
        "Это окно можно закрыть, не закрывайте открывшийся терминал!",
        color = GRAY_3,
        weight = FontWeight.BOLD
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

    InfoBTN = FilledButton(
        text = 'Руководство',
        width = 300,
        height = 35,
        style = ButtonStyle(
            bgcolor = '#3e8790',
            shape = RoundedRectangleBorder( radius = 10 )
        ),
        on_click = lambda e: OpenInfo()
    )

    # container for content
    contentContainer = Container(
        width = 390,
        height = 520,
        padding = padding.only( left = 75, right = 75 ),
        bgcolor = '#444A4B',
        border_radius = 10,
        content = Column( alignment = 'center',
                   controls = [
                       StartBTN,
                       empty1,
                       InstallBTN,
                       RemoveBTN,
                       empty2,
                       OpenBTN,
                       ChangeGeneralBTN,
                       empty3,
                       InfoBTN
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

    pass


if __name__ == '__main__':
    flet.app( target = main )