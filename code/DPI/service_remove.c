#include <windows.h>
#include <shellapi.h>
#include <stdio.h>

int main() {
    char batPath[MAX_PATH] = "service_remove.bat";
    
    // Verify the file exists
    if ( GetFileAttributesA(batPath) == INVALID_FILE_ATTRIBUTES ) {
        printf( "Error: File %s not found!\n", batPath );
        return 1;
    }

    SHELLEXECUTEINFOA sei = { 0 };
    sei.cbSize = sizeof(SHELLEXECUTEINFOA);
    sei.fMask = SEE_MASK_NOCLOSEPROCESS;
    sei.lpVerb = "runas";  // Request admin privileges
    sei.lpFile = batPath;
    sei.nShow = SW_SHOW;

    // Execute the file
    if ( !ShellExecuteExA( &sei )) {
        DWORD err = GetLastError();
        if (err == ERROR_CANCELLED) {
            printf( "Error: User denied admin privileges.\n" );
        } else {
            printf( "Error: Failed to execute file. Error code: %lu\n", err );
        }
        return 1;
    }

    printf( "Success: %s is running with admin privileges.\n", batPath );

    WaitForSingleObject( sei.hProcess, INFINITE );
    CloseHandle( sei.hProcess );

    return 0;
}