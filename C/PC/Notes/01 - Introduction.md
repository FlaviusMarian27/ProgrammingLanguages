
## ✅ Terminal & Command Basics

- Linux commands are **executables** (not requiring `.exe`)
- **Case-sensitive** file system (`File.txt` ≠ `file.txt`)
- Commands run via the **Terminal** (Console)

### 🔹 Prompt format:
username@hostname:~/directory$

```bash
- username – current logged-in user
- hostname – name of the machine
- ~ – user’s home directory (/home/username)
```

---

## 📁 Linux Filesystem Overview

- Tree-based hierarchy, starts from `/` (root)
- Uses `/` as directory separator (not `\`)
- No drive letters (C:, D:...), everything is mounted under `/`

### 🔹 Common Directories:

| Directory   | Purpose                                                                 |
|-------------|-------------------------------------------------------------------------|
| `/bin`      | Basic essential binaries (`ls`, `cp`, etc.)                            |
| `/boot`     | Boot loader files, kernel, initrd                                       |
| `/dev`      | Device files (e.g., `/dev/sda`, `/dev/mem`)                             |
| `/etc`      | System-wide configuration files                                         |
| `/home`     | Users’ personal directories                                             |
| `/lib`, `/lib32`, `/lib64` | Shared libraries for programs                            |
| `/media`    | Mount point for removable devices                                       |
| `/mnt`      | Mount point used by sysadmins                                           |
| `/opt`      | Optional third-party applications                                       |
| `/proc`     | Virtual filesystem with process info                                    |
| `/root`     | Home directory for root user                                            |
| `/sbin`     | System binaries (e.g., startup tools)                                   |
| `/srv`      | Server data                                                             |
| `/sys`      | Virtual files to interact with the kernel                               |
| `/tmp`      | Temporary files                                                         |
| `/usr`      | Secondary programs, libraries, headers                                  |
| `/var`      | Variable data (logs, mail, cache)                                       |

---

## 🛠 Basic Linux Commands

```bash
ls           # List directory contents
pwd          # Show current directory
cd           # Change directory
mkdir        # Create directory
rmdir        # Remove empty directory
rm -r        # Delete directory and contents
cat file     # Print file content
cp src dst   # Copy files/directories
mv src dst   # Move or rename
touch file   # Create an empty file
* = wildcard

.. = parent directory

~ = home

TAB = autocomplete
```

## 📖 man – Manual Pages

```bash
man <command>
```

### 🔹 Sections:

|Section|Description|
|---|---|
|1|User commands (executables)|
|2|System calls (kernel functions)|
|3|C library functions|
|4|Special files (e.g., `/dev`)|
|5|File formats and conventions|
|6|Games|
|7|Miscellaneous|
|8|System admin commands|
|9|Kernel internals|

---

## 📝 Text Editors in Terminal

```bash
vim file.c nano file.c gedit file.c &
```

- `&` = Run in background (keeps terminal usable)
- Avoid closing the terminal before saving

---

## 🧪 First C Program

```c
#include <stdio.h>

int main() {
    printf("Test\n");
    return 0;
}
```


- `-Wall` – Show all warnings
- `-o` – Output file name

### Example:

```bash
gcc -Wall -o test test.c ./test     # Run the compiled binary
```

**Note**: `./` tells Linux to run from the current directory  
(use it since `.` is not in `$PATH` by default)

---

## ✅ Summary

- Linux uses a case-sensitive terminal-based system
- Everything is a file — even devices and processes
- First C programs are compiled with `gcc`, run via `./`
- Learn key commands (`ls`, `cd`, `mkdir`, `cat`, `man`)    
- Use `man` pages to explore command syntax and functions