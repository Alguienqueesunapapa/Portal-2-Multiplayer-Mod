#ifdef _WIN32
    #include <windows.h>
#elif __linux__

#elif TARGET_OS_MAC

#else
    #error OS not supported.
#endif // _WIN32

#include "cli.hpp"

#include <string>
#include <stdio.h>
#include <iostream>

CCLI cli;

//---------------------------------------------------------------------------------
// Purpose: constructor/destructor
//---------------------------------------------------------------------------------
CCLI::CCLI()
{
#ifdef _WIN32
    m_pszPlatformType = "Windows";
#elif __linux__
    m_pszPlatformType = "Linux";
#elif TARGET_OS_MAC
    m_pszPlatformType = "MacOS";
#endif // _WIN32
}
CCLI::~CCLI() {}

const char* CCLI::GetPlatformName()
{
    // Initialized in constructor
    return m_pszPlatformType;
}

//---------------------------------------------------------------------------------
// Purpose: Run the launcher!!
//---------------------------------------------------------------------------------
int main()
{
    std::cout << std::string("Version: " LAUNCHER_VERSION "\n");

    std::string PlatformName = std::string(cli.GetPlatformName());
    std::cout << std::string("OS: " + PlatformName + "\n");

    // Run platform-specific code here
    if (PlatformName == "Windows")
    {

    }
    else if (PlatformName == "Linux")
    {

    }
    else if (PlatformName == "MacOS")
    {

    }
    else
    {
        //wtf
    }

    return 0;
}
