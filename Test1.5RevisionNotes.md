Computer Science Revision for 1.5:

###Syllabus:

- A computer requires an OS in order for the user to interact. Without an OS the user would not be able to create and modify files, run programs, and utilize the hardware of the computer.
- Key tasks carried by an OS:
    - ProgramHW interface: The OS needs a way of **executing** a program on the computer and handle **interrupts**
    - Resource management: each process needs access to the resources provided by the OS: it manages which programs can access which resources, it also resolves conflicts.
    - Memory Management: it avoids a program using the same memory slot as another program, it also optimises memory usage in limited memory size. It also uses Memory Usage Optimisation which prioritises which processes should be in main memory and which ones not.
    - Device Management: each device needs to be managed - **drivers**.
    - File management: file naming, directory structures, FS compatibility, access control mechanisms.
    - Security management: Data Recovery, Prevention of Intrusion, Data integrity, Data Privacy and Data Encryption.
    - Interrupt Handling: OS must interrupt a process and provide logs when an error happens.

Utility Programs:

- Disk Formatter: Removes data from a disk, sets up FS, partitions data. Example: GParted.
- Disk defragmenter: increases access speed on a disk by rearranging files.
- Disk Repair: Disk content analysis by checking for errors on the disk, can be virtual errors on physicals and the attempts to repair these errors. BAD SECTORS.
- Virus checker: carries out regular checks on the system to detect viruses and active scans to detect behavior of viruses.
- File compression: reduces the size of a single file or a number of files by performing compression on the files and packaging the files into a single filed called archive which can be decompressed.
- Backup: enables the system to perform automatic backups when there is a file change.

Library programs:

A Library: a set of compiled code that other programs can use, often in the form of pre-defined subroutines which can be used by importing the library and using its code.

This benefits software developers because they do not need to implement their own code from scratch rather use code from someone else which saves time. 

- Dynamic Linking: routines from a DDL are already loaded into memory, during execution, DDL code is *linked*, this is so routines can be shared.
- Software is often made by using code from libraries

Language Translators:

- **Assembler**: Translates an assembly program into machine code
- **Compiler**: Translates a high level languague into machine code, errors will be shown. Then, the machine code can run without the need of a compiler. Line in, analyzed, error found? Add to logcat, no error ===> intermediate code. Then loop. After, INTERMEDIATE ===> MACHINE CODE, errors? show logcat.

Pros of a compiler:
    - Creates a executable file .exe
    - Just need to translate once
    - FASTER

- Interpreters: execute a high level language as the program runs. RUN TIME. Line analysed individually, !errors, execute. Python.
    - Easier debug
    - Can execute at any given moment
    - Test code before code is finished

- Java: Partially compiled and partially interpreted:
    - Compiler translates source code into a BYTECODE
    - BYTECODE ==> JIT (Just In Time), Machine Code, Interpreted, Executed directly.
    
    E F F I C I E N T L Y - O R A C L E 
