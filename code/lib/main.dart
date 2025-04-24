import 'package:flutter/material.dart';
import 'package:window_manager/window_manager.dart';
import 'package:url_launcher/url_launcher.dart';
import 'dart:io';


// Main
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await windowManager.ensureInitialized();

  WindowOptions windowOptions = const WindowOptions(
    size: Size( 400, 580 ),
    minimumSize: Size( 400, 580 ),
    maximumSize: Size( 400, 580 ),
    title: 'Omega DPI Bypass',
  );

  await windowManager.setIcon( 'assets/icons/app_icon.ico' );

  await windowManager.waitUntilReadyToShow( windowOptions, () async {
    await windowManager.show();
    await windowManager.focus();
  } );

  runApp( const OmegaDPIApp() );
}


//
class OmegaDPIApp extends StatelessWidget {
  const OmegaDPIApp( { super.key } );

  @override
  Widget build( BuildContext context ) {
    return MaterialApp(
      title: 'Omega DPI Bypass',
      theme: ThemeData.dark(),
      home: const MainScreen(),
    );
  }
}


//
class MainScreen extends StatefulWidget {
  const MainScreen( { super.key } );

  @override
  State<MainScreen> createState() => _MainScreenState();
}


//
class _MainScreenState extends State<MainScreen> {
  final Map<String, Map<String, String>> translations = {
    'ru': {
      'title': 'Omega DPI',
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
      'iran': 'Стандартный (Иран)',
      'default': 'Стандартный (Россия)',
      'error_t': 'Ошибка',
      'admin_required': 'Требуются права администратора',
    },
    'en': {
      'title': 'Omega DPI',
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
      'iran': 'Default (Iran)',
      'default': 'Default (Russia)',
      'error_t': 'Error',
      'admin_required': 'Administrator privileges required',
    },
    'fa': {
      'title': 'Omega DPI',
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
      'iran': 'شروع پیش فرض (ایران)',
      'default': 'شروع پیش فرض',
      'error_t': 'خطا',
      'admin_required': 'نیاز به مجوزهای مدیر سیستم',
    }
  };

  late String selectedLanguage;
  late Map<String, String> text;
  String dropdownValue = 'default';
  bool isRunning = false;

  @override
  void initState() {
    super.initState();
    _detectLanguage();
  }

  void _detectLanguage() {
    final language = Platform.localeName.split( '_' )[0];

    if ( language == 'fa' ) {
      selectedLanguage = 'fa';
    } else if ( language == 'ru' ) {
      selectedLanguage = 'ru';
    } else {
      selectedLanguage = 'en';
    }

    text = translations[selectedLanguage]!;
  }


  // Logic Structure
  void _changeLanguage( String? value ) {
    if ( value == null ) return;
    setState( () {
      selectedLanguage = value;
      text = translations[selectedLanguage]!;
    } );
  }

  Future<void> _startBypass() async {
    try {
      final result = await Process.run( 'tasklist', [] );
      if ( result.stdout.toString().contains( 'winws.exe' )) {
        _showErrorDialog();
        return;
      }

      String command;
      switch ( dropdownValue ) {
        case 'iran': command = 'iran.bat'; break;
        default: command = 'general.bat';
      }

      await Process.run( 'cmd', ['/c', 'cd DPI && start /B $command'] );
    } catch ( e ) {
      debugPrint( 'Error starting bypass: $e' );
    }
  }

  Future<void> _stopBypass() async {
    try {
      await Process.run( 'taskkill', ['/IM', 'winws.exe', '/F'] );
    } catch ( e ) {
      debugPrint( 'Error stopping bypass: $e' );
    }
  }

  Future<void> _openFolder() async {
    await Process.run( 'explorer', ['DPI'] );
  }

  Future<void> _openGeneral() async {
    await Process.run( 'notepad', ['DPI\\list-general.txt'] );
  }

  Future<void> _installService() async {
    await Process.run( 'cmd', ['/c', 'cd DPI && service_install.exe'] );
  }

  Future<void> _removeService() async {
    await Process.run( 'cmd', ['/c', 'cd DPI && service_remove.exe'] );
  }

  Future<void> _openInfo() async {
    try {
      if ( await canLaunchUrl( Uri.file( 'guides/guide.html' ))) {
        await launchUrl( Uri.file( 'guides/guide.html' ));
      } else {
        await Process.run( 'cmd', ['/c', 'start guides/guide.html'] );
      }
    } catch (e) {
      debugPrint( 'Error opening info: $e' );
    }
  }

  void _showErrorDialog() {
    showDialog(
      context: context,
      builder: ( context ) => AlertDialog(
        title: Text( text['error_t']! ),
        content: Text(
          selectedLanguage == 'en'
              ? 'You already have DPI bypass service installed!\nPlease remove it first before starting a new one!'
              : selectedLanguage == 'ru'
              ? 'У вас уже установлена служба обхода DPI!\nСперва удалите её, прежде чем запустить новую!'
              : 'شما قبلاً سرویس بای پس DPI را نصب کرده اید!\nلطفاً قبل از شروع یک مورد جدید، ابتدا آن را حذف کنید!',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop( context ),
            child: Text( text['default']! ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build( BuildContext context ) {
    return Scaffold(
      backgroundColor: const Color( 0xFF33A3AD),
      body: Center(
        child: Container(
          width: 370,
          height: 530,
          decoration: BoxDecoration(
            color: const Color( 0xFF444A4B ),
            borderRadius: BorderRadius.circular( 8 ),
            border: Border.all(
              color: const Color( 0xFF33A3AD ),
              width: 2,
            ),
          ),
          padding: const EdgeInsets.symmetric( horizontal: 55 ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: isRunning ? _runningUI() : _mainUI(),
          ),
        ),
      ),
    );
  }


  // GUI Structure
  List<Widget> _mainUI() {
    return [
      ElevatedButton(
        onPressed: _startBypass,
        style: ElevatedButton.styleFrom(
          backgroundColor: const Color( 0xFF33A3AD),
          foregroundColor: Colors.white,
          minimumSize: const Size( 320, 60 ),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular( 8 ),
          ),
        ),
        child: Text( text['start_button']! ),
      ),
      const SizedBox( height: 16 ),
      DropdownButtonFormField<String>(
        value: dropdownValue,
        decoration: InputDecoration(
          labelText: text['alt_start'],
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(8),
            borderSide: const BorderSide( color: Color( 0xFF33A3AD )),
          ),
          enabledBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(8),
            borderSide: const BorderSide( color: Color( 0xFF33A3AD )),
          ),
        ),
        items: [
          DropdownMenuItem(
            value: 'default',
            child: Text( text['default']! ),
          ),
          DropdownMenuItem(
            value: 'iran',
            child: Text( text['iran']! ),
          )
        ],
        onChanged: (value) {
          setState(() => dropdownValue = value!);
        },
      ),
      const SizedBox( height: 16 ),
      ElevatedButton(
        onPressed: _installService,
        style: ElevatedButton.styleFrom(
          backgroundColor: const Color( 0xFF33A3AD ),
          foregroundColor: Colors.white,
          minimumSize: const Size( 320, 50 ),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular( 8 ),
          ),
        ),
        child: Text( text['install_button']! ),
      ),
      const SizedBox( height: 8 ),
      ElevatedButton(
        onPressed: _removeService,
        style: ElevatedButton.styleFrom(
          backgroundColor: const Color( 0xFF33A3AD ),
          foregroundColor: Colors.white,
          minimumSize: const Size( 320, 50 ),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular( 8 ),
          ),
        ),
        child: Text( text['remove_button']! ),
      ),
      const SizedBox( height: 16 ),
      ElevatedButton(
        onPressed: _openFolder,
        style: ElevatedButton.styleFrom(
          backgroundColor: const Color( 0xFF3e8790 ),
          foregroundColor: Colors.white,
          minimumSize: const Size( 320, 50 ),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular( 8 ),
          ),
        ),
        child: Text( text['open_folder_button']! ),
      ),
      const SizedBox( height: 8 ),
      ElevatedButton(
        onPressed: _openGeneral,
        style: ElevatedButton.styleFrom(
          backgroundColor: const Color( 0xFF3e8790 ),
          foregroundColor: Colors.white,
          minimumSize: const Size( 320, 50 ),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular( 8 ),
          ),
        ),
        child: Text( text['open_general_button']! ),
      ),
      const SizedBox( height: 16 ),
      ElevatedButton(
        onPressed: _openInfo,
        style: ElevatedButton.styleFrom(
          backgroundColor: const Color( 0xFF3e8790 ),
          foregroundColor: Colors.white,
          minimumSize: const Size( 320, 50 ),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular( 8 ),
          ),
        ),
        child: Text( text['info_button']! ),
      ),
      const SizedBox( height: 16 ),
      DropdownButtonFormField<String>(
        value: selectedLanguage,
        decoration: InputDecoration(
          labelText: text['lang'],
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular( 8 ),
            borderSide: const BorderSide( color: Color( 0xFF33A3AD )),
          ),
          enabledBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular( 8 ),
            borderSide: const BorderSide( color: Color( 0xFF33A3AD )),
          ),
        ),
        items: const [
          DropdownMenuItem(
            value: 'en',
            child: Text( 'English' ),
          ),
          DropdownMenuItem(
            value: 'ru',
            child: Text( 'Русский' ),
          ),
          DropdownMenuItem(
            value: 'fa',
            child: Text( 'فارسی' ),
          ),
        ],
        onChanged: _changeLanguage,
      ),
    ];
  }

  List<Widget> _runningUI() {
    return [
      ElevatedButton(
        onPressed: _stopBypass,
        style: ElevatedButton.styleFrom(
          backgroundColor: const Color( 0xFF33A3AD ),
          foregroundColor: Colors.white,
          minimumSize: const Size( 320, 50 ),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular( 8 ),
          ),
        ),
        child: Text( text['stop_button']! ),
      ),
      const SizedBox( height: 16 ),
      Text(
        text['warning']!,
        style: const TextStyle(
          color: Color( 0xFFC6C6C6 ),
          fontWeight: FontWeight.bold,
        ),
      ),
      const SizedBox( height: 16 ),
      ElevatedButton(
        onPressed: _openInfo,
        style: ElevatedButton.styleFrom(
          backgroundColor: const Color( 0xFF3e8790 ),
          foregroundColor: Colors.white,
          minimumSize: const Size( 320, 40 ),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular( 8 ),
          ),
        ),
        child: Text( text['info_button']! ),
      ),
      const SizedBox( height: 16 ),
      DropdownButtonFormField<String>(
        value: selectedLanguage,
        decoration: InputDecoration(
          labelText: text['lang'],
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular( 8 ),
            borderSide: const BorderSide( color: Color( 0xFF33A3AD )),
          ),
          enabledBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular( 8 ),
            borderSide: const BorderSide( color: Color( 0xFF33A3AD )),
          ),
        ),
        items: const [
          DropdownMenuItem(
            value: 'en',
            child: Text( 'English' ),
          ),
          DropdownMenuItem(
            value: 'ru',
            child: Text( 'Русский' ),
          ),
          DropdownMenuItem(
            value: 'fa',
            child: Text( 'فارسی' ),
          ),
        ],
        onChanged: _changeLanguage,
      ),
    ];
  }
}