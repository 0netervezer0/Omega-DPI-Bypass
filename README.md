# Omega DPI Bypass
## A simple and convenient tool for bypassing DPI on Windows

* [Usage](#Usage)
* [Problems](#Problems-that-may-arise)
* [Build](#Build)
* [Author of binaries](#Author-of-binaries)
* [Support developer](#Support-developer)

#### [Русский (Russian) 🇷🇺](https://github.com/0netervezer0/Omega-DPI-Bypass/blob/main/docs/README_ru.md)  |  [فارسی (Persian) 🇮🇷](https://github.com/0netervezer0/Omega-DPI-Bypass/blob/main/docs/README_fa.md)
It will help you get rid of blocking of YouTube or Discord in such countries as Russia, Iran and other countries where these services are blocked by DPI technology.
> ### [Download](https://github.com/0netervezer0/Omega-DPI-Bypass/releases/tag/2.2.2)

## Usage
The program window contains several buttons and a drop-down list. Before you start the bypass, you need to select a launch option from the drop-down list. One bypass method is offered for Iran and 10 for Russia.

After selecting the option, click the start button and you will see the command line. The program that runs in the command line is the bypass service, if you need to stop the bypass - just close it.
> [!NOTE]
> For the bypass to work, you don't need the main program window, you can close it. The program that runs in the command line is the bypass service.

The "Install Service" button will help you install the bypass service as a background process. It will also be added to startup. This means that you do not have to start the service manually every time. It will work in the background and without the command line. The "Remove Service" button will help you remove the bypass service from background processes and startup.

The remaining buttons are more useful for advanced users. They allow you to view and change the list of addresses and bypass methods, as well as update the binary files if necessary.
> [!WARNING]
> Only change the contents of the DPI folder and the address list if you are sure of what you are doing. This may disable the bypass.

## Problems that may arise
> [!CAUTION]
> #### False positive antivirus
> Since Omega DPI Bypass is rarely downloaded, it may not be listed in many antivirus databases as safe.
> The developer guarantees the safety of installation and use of the program. If you do not trust the file builded by the developer, you can build the program yourself. All source files are provided in the repository.

## Build
> [!WARNING]
> Build requires go and the fyne framework

```bash
cd main
go build -ldflags="-s -w -H=windowsgui" -o Omega_DPI_Bypass.exe
```

## Author of binaries
Huge thanks to [bol-van](https://github.com/bol-van) for winws and other binaries to bypass DPI.
[Link to repository](https://github.com/bol-van/zapret).

## Support developer
0xbeaF7EB73920A2c47388365D2023Fc2120C65D5A - MetaMask (USDT)

0x58B801b727384AA4DE2Ca9B3465727CC51344381 - Phantom (Ethereum)
