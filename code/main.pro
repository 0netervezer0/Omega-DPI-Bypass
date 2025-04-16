CONFIG += static
QT += widgets
QMAKE_LFLAGS += -static -static-libgcc -static-libstdc++

TARGET = LupiDPI
TEMPLATE = app

SOURCES += main.cpp
RC_FILE = app.rc