// Template sane hpp file

#ifndef CLI_HPP // This is good practice to ensure each hpp file only gets parsed once (vista does this)
#define CLI_HPP

#define LAUNCHER_VERSION "1.0"

class CCLI
{
public:
    CCLI();
    ~CCLI();

public:
    const char* GetPlatformName();

private: // Private is for variables that can only be changed THROUGH the class methods/functions
    const char* m_pszPlatformType = "(Undefined)";
};

extern CCLI cli; // Create object

// Typically u wanna put the def as a comment like below for any endif
#endif // CLI_HPP