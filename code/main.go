package main

import (
	"os/exec"
	"syscall"
	"unsafe"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
	"golang.org/x/sys/windows"
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

type LocaleStrings struct {
    WindowTitle       string
    LaunchButton      string
    ParameterSelect   string
    InstallService    string
    UninstallService  string
    OpenFolder        string
    OpenAddressList   string
    OpenGuide         string
    Parameters        []string
    ErrorSelectParam  string
}

var (
    currentLocale *LocaleStrings
    russianLocale = &LocaleStrings{
        WindowTitle:      "Omega DPI Bypass",
        LaunchButton:     "Запустить DPI Bypass",
        ParameterSelect:  "Параметры Запуска",
        InstallService:   "Установить Службу",
        UninstallService: "Удалить Службу",
        OpenFolder:       "Открыть BIN Папку",
        OpenAddressList:  "Открыть Список Адресов",
        OpenGuide:        "Руководство Пользователя",
        Parameters:       []string{ "Стандартный (Россия)", "Стандартный (Иран)", "Альтернативный РФ 1", "Альтернативный РФ 2", 
                            "Альтернативный РФ 3", "Альтернативный РФ 4", "Альтернативный РФ 5", "Альтернативный РФ 6", 
                            "Ru Fake TLS", "Ru Fake TLS ALT", "Ru TLS Auto" },
        ErrorSelectParam: "Выберите Параметры Запуска!",
    }
    persianLocale = &LocaleStrings{
        WindowTitle:      "Omega DPI Bypass",
        LaunchButton:     "اجرای DPI Bypass",
        ParameterSelect:  "پارامترهای اجرا",
        InstallService:   "نصب سرویس",
        UninstallService: "حذف سرویس",
        OpenFolder:       "باز کردن پوشه فایل ها",
        OpenAddressList:  "باز کردن لیست آدرس ها",
        OpenGuide:        "راهنمای کاربر",
        Parameters:       []string{ "پیش فرض (روسیه)", "پیش فرض (ایران)", "Alt Russia 1", "Alt Russia 2", 
                            "Alt Russia 3", "Alt Russia 4", "Alt Russia 5", "Alt Russia 6", 
                            "Ru Fake TLS", "Ru Fake TLS ALT", "Ru TLS Auto" },
        ErrorSelectParam: "پارامترهای اجرا را انتخاب کنید!",
    }
    englishLocale = &LocaleStrings{
        WindowTitle:      "Omega DPI Bypass",
        LaunchButton:     "Launch DPI Bypass",
        ParameterSelect:  "Launch Parameters",
        InstallService:   "Install Service",
        UninstallService: "Uninstall Service",
        OpenFolder:       "Open Binaries Folder",
        OpenAddressList:  "Open Address List",
        OpenGuide:        "User Guide",
        Parameters:       []string{ "Default (Russia)", "Default (Iran)", "Alt Russia 1", "Alt Russia 2", 
                            "Alt Russia 3", "Alt Russia 4", "Alt Russia 5", "Alt Russia 6", 
                            "Ru Fake TLS", "Ru Fake TLS ALT", "Ru TLS Auto" },
        ErrorSelectParam: "Select Launch Parameters!",
    }
)

func getSystemLanguage() *LocaleStrings {
    kernel32 := windows.NewLazySystemDLL( "kernel32.dll" )
    getUserDefaultLocaleName := kernel32.NewProc( "GetUserDefaultLocaleName" )
    
    var localeName [85]uint16
    ret, _, _ := getUserDefaultLocaleName.Call(
        uintptr( unsafe.Pointer( &localeName[0] )),
        uintptr( len( localeName )),
    )
    
    if ret == 0 {
        return englishLocale
    }
    
    locale := syscall.UTF16ToString( localeName[:] )
    switch {
    case locale == "ru-RU" || locale == "ru":
        return russianLocale
    case locale == "fa-IR" || locale == "fa":
        return persianLocale
    default:
        return englishLocale
    }
}

func main() {
    currentLocale = getSystemLanguage()
    
	APP := app.New()
    APP.Settings().SetTheme( &MinimalDarkTheme{} )
    APP.SetIcon( resourceIconPng )

	Window := APP.NewWindow( currentLocale.WindowTitle )
	Window.Resize( fyne.NewSize( 300, 438 )) 
	Window.SetFixedSize( true ) 

	var selected_parameter string

	launch_button := widget.NewButton(
        currentLocale.LaunchButton,
        func() { StartBypass( selected_parameter )},
    )
	launch_button.Resize( fyne.NewSize( 260, 46 )) 
	launch_button.Move( fyne.NewPos( 20, 20 )) 

	parameter_select := widget.NewSelect(
		currentLocale.Parameters,
		func( selected string ) {
			selected_parameter = selected;
		},
	)
	parameter_select.PlaceHolder = currentLocale.ParameterSelect
	parameter_select.Resize( fyne.NewSize( 260, 40 )) 
	parameter_select.Move( fyne.NewPos( 20, 72 )) 
    
    installS_button := widget.NewButton( currentLocale.InstallService, InstallService )
    installS_button.Resize( fyne.NewSize( 260, 40 )) 
	installS_button.Move( fyne.NewPos( 20, 140 )) 
    
    uninstallS_button := widget.NewButton( currentLocale.UninstallService, UninstallService )
    uninstallS_button.Resize( fyne.NewSize( 260, 40 )) 
	uninstallS_button.Move( fyne.NewPos( 20, 186 )) 
    
    openFolder_button := widget.NewButton( currentLocale.OpenFolder, OpenFolder )
    openFolder_button.Resize( fyne.NewSize( 260, 40 )) 
	openFolder_button.Move( fyne.NewPos( 20, 254 )) 
    
    openAddressList_button := widget.NewButton( currentLocale.OpenAddressList, OpenAddressList )
    openAddressList_button.Resize( fyne.NewSize( 260, 40 )) 
	openAddressList_button.Move( fyne.NewPos( 20, 300 )) 
    
    openGuide_button := widget.NewButton( currentLocale.OpenGuide, OpenGuide )
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
    case "Default (Russia)", "Стандартный (Россия)", "پیش فرض (روسیه)":
        cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", "general.bat" )
        cmd.Run()
    case "Default (Iran)", "Стандартный (Иран)", "پیش فرض (ایران)":
        cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", "iran.bat" )
        cmd.Run()
    case "Alt Russia 1", "Альтернативный РФ 1":
        cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", "\"general (ALT1).bat\"" )
        cmd.Run()
    case "Alt Russia 2", "Альтернативный РФ 2":
        cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", "\"general (ALT2).bat\"" )
        cmd.Run()
    case "Alt Russia 3", "Альтернативный РФ 3":
        cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", "\"general (ALT3).bat\"" )
        cmd.Run()
    case "Alt Russia 4", "Альтернативный РФ 4":
        cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", "\"general (ALT4).bat\"" )
        cmd.Run()
    case "Alt Russia 5", "Альтернативный РФ 5":
        cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", "\"general (ALT5).bat\"" )
        cmd.Run()
    case "Alt Russia 6", "Альтернативный РФ 6":
        cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", "\"general (ALT6).bat\"" )
        cmd.Run()
    case "Ru Fake TLS":
        cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&",
                             "\"general (FAKE TLS).bat\"" )
        cmd.Run()
    case "Ru Fake TLS ALT":
        cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&", 
                             "\"general (FAKE TLS ALT).bat\"" )
        cmd.Run()
    case "Ru TLS Auto":
        cmd := exec.Command( "cmd", "/C", "cd", "DPI", "&&",
                             "\"general (FAKE TLS AUTO).bat\"" )
        cmd.Run()
    default:
        MessageBox( 0, currentLocale.ErrorSelectParam, "Error", MB_ICONERROR )
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
    cmd := exec.Command( "cmd", "/C", "cd", "DPI/lists", "&&", "start", "", "notepad", "list-general.txt" )
    cmd.Run()
}

func OpenGuide() {
    cmd := exec.Command( "cmd", "/C", "cd", "guides", "&&", "start", "", "guide.html" )
    cmd.Run()
}
