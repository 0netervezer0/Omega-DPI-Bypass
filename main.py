import os, sys, locale, psutil, shutil, subprocess
from pathlib import Path
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QComboBox,
    QFrame,
    QSystemTrayIcon,
    QMenu
)

# windows constants
CREATE_NO_WINDOW = 0x08000000


# language detection
lang = locale.getlocale()[0]
print( lang )

# winws constants
REPO_URL = "https://github.com/Flowseal/zapret-discord-youtube"
PROC_NAME = 'winws.exe'
BYPASS_RUNNING = False

app = QApplication( sys.argv )
app.setQuitOnLastWindowClosed( False )

# loading styles
style_path = Path( __file__ ).parent / 'style.qss'
if style_path.exists():
    with open( style_path, 'r', encoding = 'utf-8' ) as f:
        app.setStyleSheet( f.read() )


#bypass start/stop functions
def is_proc_running() -> bool:
    for proc in psutil.process_iter( ['name'] ):
        try:
            if proc.info['name'] and proc.info['name'].lower() == PROC_NAME:
                return True
        except ( psutil.NoSuchProcess, psutil.AccessDenied ):
            pass

    return False

def stop_proc() -> None:
    for proc in psutil.process_iter( ['name'] ):
        try:
            if proc.info['name'] and proc.info['name'].lower() == PROC_NAME:
                proc.terminate()
        except ( psutil.NoSuchProcess, psutil.AccessDenied ):
            pass

def update_ui() -> None:
    running = is_proc_running()
    if running:
        main_window.btn_start.setText( "Stop the Bypass" )
        main_window.btn_start.setEnabled( True )
        tray.start_action.setText( "Stop the Bypass" )
        tray.start_action.setEnabled( True )
        tray.stat_label.setText( "Bypass is ON" )

    else:
        main_window.btn_start.setText( "Start the Bypass" )
        tray.start_action.setText( "Start the Bypass" )
        tray.stat_label.setText( "Bypass is OFF" )


# window class
class MainWindow( QMainWindow ):
    def __init__( self ):
        super().__init__()
        self.setWindowTitle( "Omega DPI Bypass" )
        self.setWindowIcon( QIcon( 'sources/icon.png' ))
        self.setFixedSize( 360, 300 )

        central = QWidget()
        self.setCentralWidget( central )

        main_layout = QVBoxLayout()
        central.setLayout( main_layout )

        # separators
        self.line = QFrame()
        self.line.setFrameShape( QFrame.HLine )
        self.line.setFrameShadow( QFrame.Sunken )
        self.line_ = QFrame()
        self.line_.setFrameShape( QFrame.HLine )
        self.line_.setFrameShadow( QFrame.Sunken )

        # layout for list and update button
        combo_layout = QHBoxLayout()
        main_layout.addLayout(combo_layout)

        # combo box
        self.combo = QComboBox()
        self.combo.setFixedHeight( 40 )
        combo_layout.addWidget( self.combo )

        # update list button
        self.refresh_btn = QPushButton( "⟳" )
        self.refresh_btn.setIcon( QIcon( "sources/refresh.png" ))
        self.refresh_btn.setText( '' )
        self.refresh_btn.setFixedWidth( 28 )
        self.refresh_btn.setToolTip( "Update List" )
        combo_layout.addWidget( self.refresh_btn )

        # main buttons
        self.btn_start = QPushButton( "Start the Bypass" )
        self.btn_check_updates = QPushButton( 'Check for Updates' )
        self.btn_service = QPushButton( 'Install/Remove Service' )
        self.btn_manual = QPushButton( 'Manual' )
        self.btn_repo = QPushButton( 'Visit a Repository' )

        main_layout.addWidget( self.btn_start )
        main_layout.addWidget( self.line )
        main_layout.addWidget( self.btn_check_updates )
        main_layout.addWidget( self.btn_service )
        main_layout.addWidget( self.line_ )
        main_layout.addWidget( self.btn_manual )
        main_layout.addWidget( self.btn_repo )

        # actions
        self.btn_start.clicked.connect( self.start_bypass )
        self.refresh_btn.clicked.connect( self.load_bat_files )
        self.btn_check_updates.clicked.connect( self.check_updates )
        self.btn_service.clicked.connect( self.service )
        self.btn_manual.clicked.connect( self.open_manual )
        self.btn_repo.clicked.connect( self. open_repo )

        # on start load
        self.load_bat_files()

    def get_selected_file( self ) -> Path:
        return self.combo.currentData()

    def start_bypass( self ) -> None:
        """Launching selected .bat file with no console"""
        if is_proc_running():
            stop_proc()
            return

        file = self.get_selected_file()
        if not file:
            return

        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

            subprocess.Popen(
                str( file ),
                cwd = str( file.parent ),
                startupinfo = startupinfo,
                creationflags = CREATE_NO_WINDOW,
                shell = True
            )

        except Exception as e:
            print( "Error starting bypass:", e )

    def load_bat_files( self ) -> None:
        """Looking for all .bat files in the bypass folder"""
        current_selection = self.combo.currentText()
        self.combo.clear()

        base_dir = Path.cwd() / "zapret-discord-youtube"
        bat_files = list( base_dir.glob( "*.bat" ))
        if bat_files:
            for file in bat_files:
                if file.stem != 'service':
                    self.combo.addItem( file.stem, file )

            index = self.combo.findText( current_selection )
            if index >= 0:
                self.combo.setCurrentIndex( index )

        else:
            self.combo.addItem( "No ways to bypass, try to check for updates...", None )

    def check_updates( self ) -> None:
        """Getting the uptodate binaries from git repository"""
        repo_dir = Path.cwd() / "zapret-discord-youtube"

        try:
            if repo_dir.exists():
                shutil.rmtree( repo_dir )

            result = subprocess.run(
                ["git", "clone", REPO_URL],
                capture_output = True,
                text = True,
                creationflags = CREATE_NO_WINDOW,
            )

            if result.returncode == 0:
                QMessageBox.information(
                    self,
                    "Success",
                    "Update completed successfully."
                )

                self.load_bat_files()
            else:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Git clone failed:\n{ result.stderr }"
                )

        except:
            QMessageBox.critical(
                self,
                "Error",
                f"Maybe git is not installed. Install it at https://git-scm.com/install/windows."
            )

    def service( self ) -> None:
        try:
            os.system( 'cd /zapret-discord-youtube/ && start service.bat' )
        except:
            QMessageBox.critical(
                self,
                "Error",
                f"Maybe there is no binary files. Try to check for updates."
            )

    def open_manual( self ) -> None:
        return

    def open_repo( self ) -> None:
        return

main_window = MainWindow()


# tray class
class Tray( QSystemTrayIcon ):
    def __init__( self, parent = None ):
        super().__init__( parent )
        self.setIcon( QIcon( 'sources/icon.png' ))

        self.menu = QMenu()

        self.show_action  = QAction( 'Open' )
        self.start_action = QAction( 'Start the Bypass' )
        self.stat_label   = QAction( f'Bypass is OFF' )
        self.quit_action  = QAction( 'Exit' )

        self.stat_label.setEnabled( False )
        self.menu.addAction( self.show_action )
        self.menu.addSeparator()
        self.menu.addAction( self.stat_label )
        self.menu.addAction( self.start_action )
        self.menu.addSeparator()
        self.menu.addAction( self.quit_action )

        self.setContextMenu( self.menu )

        self.start_action.triggered.connect( main_window.start_bypass )
        self.show_action.triggered.connect( main_window.show )
        self.quit_action.triggered.connect( app.quit )

tray = Tray()


# timer to update
timer = QTimer()
timer.timeout.connect( update_ui )
timer.start( 1000 )
update_ui()

tray.show()
sys.exit( app.exec() )
