# #######################
# LupiDPI ( Windows Edition ) V1.3
# by netervezer
# #######################

from os import system
from elevate import elevate
from subprocess import call
from flet import FilledButton, Dropdown, Container, Page, ButtonStyle, RoundedRectangleBorder, Text, \
    FontWeight, dropdown, padding, Column, Row, app

elevate( show_console = False )
def main( page: Page ):

    page.window.resizable = False
    page.window.width = 400
    page.window.height = 540
    page.title = 'Lupi DPI'
    page.window.icon = 'icon.ico'

    def OpenInfo( e = None ):
        call( 'info.html', shell = True )

    def OpenF( e = None ):
        call( 'explorer.exe DPI', shell = True )

    def Start( e = None ):
        if AltStarts.value == 'Alt Запуск 1':
            system('cd DPI & general (ALT1).bat')
        elif AltStarts.value == 'Alt Запуск 2':
            system('cd DPI & general (ALT2).bat')
        elif AltStarts.value == 'Alt Запуск 3':
            system('cd DPI & general (ALT3).bat')
        elif AltStarts.value == 'Alt Запуск 4':
            system('cd DPI & general (ALT4).bat')
        elif AltStarts.value == 'Alt Запуск 5':
            system('cd DPI & general (ALT5).bat')
        else:
            system('cd DPI & general.bat')
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
        contentContainer.content.controls.append( StopBTN )
        contentContainer.content.controls.append( WarningLabel )
        contentContainer.content.controls.append( empty1 )
        contentContainer.content.controls.append( InfoBTN )
        page.update()

    def Stop( e = None ):
        system( 'taskkill /IM winws.exe /F' )
        contentContainer.content.controls.remove( StopBTN )
        contentContainer.content.controls.remove( empty1 )
        contentContainer.content.controls.remove( WarningLabel )
        contentContainer.content.controls.remove( InfoBTN )
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
        page.update()

    def OpenGeneral( e = None ):
        pass
        system( 'cd DPI & list-general.txt' )

    def Install( e = None ):
        pass
        system( 'cd DPI & start service_install.bat' )

    def Remove( e = None ):
        pass
        system( 'cd DPI & start service_remove.bat' )

    empty1 = Container( height = 16 )
    empty2 = Container( height = 16 )
    empty3 = Container( height = 16 )


    # buttons
    StartBTN = FilledButton(
        text = 'Запустить DPI',
        width = 300,
        height = 50,
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
        color = '#C6C6C6',
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

    AltStarts = Dropdown(
        border_color = '#33A3AD',
        border_radius = 10,
        label = 'Параметры Запуска',
        width = 300,
        height = 50,
        options = [
            dropdown.Option( 'Стандартный Запуск' ),
            dropdown.Option( 'Alt Запуск 1' ),
            dropdown.Option( 'Alt Запуск 2' ),
            dropdown.Option( 'Alt Запуск 3' ),
            dropdown.Option( 'Alt Запуск 4' ),
            dropdown.Option( 'Alt Запуск 5' ),
        ]
    )

    # container for content
    contentContainer = Container(
        width = 375,
        height = 540,
        padding = padding.only( left = 75, right = 75 ),
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
    app( target = main )