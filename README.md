# PatchPatrol

PatchPatrol is a simple yet effective tool for keeping Windows systems secure by monitoring and applying the latest security patches and updates. This script automates the process of checking for available Windows updates and installing them, ensuring your system is always up-to-date with the latest security enhancements.

## Features

- Automatically checks for Windows updates.
- Installs available updates and reboots the system if necessary.
- Logs all activities for easy monitoring and troubleshooting.

## Requirements

- Windows operating system.
- Python 3.x installed on your system.
- PowerShell must be installed and accessible via the command line.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/patchpatrol.git
   ```

2. Navigate to the cloned directory:

   ```bash
   cd patchpatrol
   ```

3. Ensure Python and PowerShell are installed and added to your system's PATH.

## Usage

To start PatchPatrol, simply run the `patch_patrol.py` script:

```bash
python patch_patrol.py
```

PatchPatrol will continuously run, checking for updates every 24 hours and applying them as necessary. All actions are logged in `patch_patrol.log`.

## Logging

PatchPatrol creates a log file `patch_patrol.log` in the same directory where the script is run. This log file will contain detailed information about each update check and installation process, including any errors encountered.

## Contributing

Contributions are welcome! If you have suggestions or feature requests, please open an issue or submit a pull request.

## Disclaimer

Use this script at your own risk. Ensure you have backups of your important data before running automated update scripts.

## License

This project is licensed under the MIT License - see the LICENSE file for details.