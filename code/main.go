package main

import (
	"os/exec"
	"syscall"
	"unsafe"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

const (
    MB_OK                = 0x00000000
    MB_OKCANCEL          = 0x00000001
    MB_YESNO             = 0x00000004
    MB_ICONINFORMATION   = 0x00000040
    MB_ICONQUESTION      = 0x00000020
    MB_ICONERROR         = 0x00000010
)

var (
    user32           = syscall.NewLazyDLL( "user32.dll" )
    procMessageBoxW  = user32.NewProc( "MessageBoxW" )
)

func main() {
	APP := app.New()
    APP.Settings().SetTheme( &MinimalDarkTheme{} )
    APP.SetIcon( resourceIconPng )

	Window := APP.NewWindow( "Omega DPI Bypass" )
	Window.Resize( fyne.NewSize( 300, 438 ))
	Window.SetFixedSize( true ) 

	var selected_parameter string

	launch_button := widget.NewButton(
        "Launch DPI Bypass",
        func() { StartBypass( selected_parameter )},
    )
	launch_button.Resize( fyne.NewSize( 260, 46 ))
	launch_button.Move( fyne.NewPos( 20, 20 )) 

	parameter_select := widget.NewSelect(
		[]string {
			"Default (Russia)",
			"Default (Iran)",
		},
		func( selected string ) {
			selected_parameter = selected;
		},
	)
	parameter_select.PlaceHolder = "Launch Parameters"
	parameter_select.Resize( fyne.NewSize( 260, 40 ))
	parameter_select.Move( fyne.NewPos( 20, 72 ))
    
    installS_button := widget.NewButton( "Install Service", InstallService )
    installS_button.Resize( fyne.NewSize( 260, 40 ))
	installS_button.Move( fyne.NewPos( 20, 140 )) 
    
    uninstallS_button := widget.NewButton( "Uninstall Service", UninstallService )
    uninstallS_button.Resize( fyne.NewSize( 260, 40 ))
	uninstallS_button.Move( fyne.NewPos( 20, 186 ))
    
    openFolder_button := widget.NewButton( "Open Binaries Folder", OpenFolder )
    openFolder_button.Resize( fyne.NewSize( 260, 40 ))
	openFolder_button.Move( fyne.NewPos( 20, 254 )) 
    
    openAddressList_button := widget.NewButton( "Open Address List", OpenAddressList )
    openAddressList_button.Resize( fyne.NewSize( 260, 40 ))
	openAddressList_button.Move( fyne.NewPos( 20, 300 ))
    
    openGuide_button := widget.NewButton( "User Guide", OpenGuide )
    openGuide_button.Resize( fyne.NewSize( 260, 40 ))
	openGuide_button.Move( fyne.NewPos( 20, 368 ))
    

	main_container := container.NewWithoutLayout(
		launch_button,
		parameter_select,
        installS_button,
        uninstallS_button,
        openFolder_button,
        openAddressList_button,
        openGuide_button,
	)

	Window.SetContent( main_container )
	Window.ShowAndRun()
}

func MessageBox( parent uintptr, caption, title string, flags uint32 ) int {
    result, _, _ := procMessageBoxW.Call(
        parent,
        uintptr( unsafe.Pointer( syscall.StringToUTF16Ptr( caption ))),
        uintptr( unsafe.Pointer( syscall.StringToUTF16Ptr( title ))),
        uintptr( flags ),
    )
    return int( result )
}
 

func StartBypass( parameter string ) {
    switch parameter {
    case "Default (Russia)":
        cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", "russia.bat" )
        cmd.Run()
    case "Default (Iran)":
        cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", "iran.bat" )
        cmd.Run()
    default:
        MessageBox( 0, "Select Launch Parameters!", "Error", MB_ICONERROR )
    }
}

func InstallService() {
    cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", "start", "", "service_install.bat" )
    cmd.Run()
}

func UninstallService() {
    cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", "start", "", "service_uninstall.bat" )
    cmd.Run()
}

func OpenFolder() {
    cmd := exec.Command( "cmd", "/C", "explorer.exe", "DPI", )
    cmd.Run()
}

func OpenAddressList() {
    cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", "start", "", "notepad", "list-general.txt" )
    cmd.Run()
}

func OpenGuide() {
    cmd := exec.Command( "cmd", "/C", "cd", "guides", "&&", "start", "", "guide.html" )
    cmd.Run()
}