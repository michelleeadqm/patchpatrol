import subprocess
import logging
import time
from datetime import datetime

# Configure logging
logging.basicConfig(filename='patch_patrol.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_for_updates():
    logging.info("Checking for available Windows updates...")
    try:
        # Execute the command to check for updates
        result = subprocess.run(['powershell', '-Command', 
                                 'Get-WindowsUpdate'], capture_output=True, text=True)
        logging.info(f"Update check output: {result.stdout}")
        return result.stdout
    except Exception as e:
        logging.error(f"Error checking updates: {e}")
        return None

def install_updates():
    logging.info("Installing available Windows updates...")
    try:
        # Execute the command to install updates
        result = subprocess.run(['powershell', '-Command', 
                                 'Install-WindowsUpdate -AcceptAll -AutoReboot'], capture_output=True, text=True)
        logging.info(f"Update installation output: {result.stdout}")
        return result.stdout
    except Exception as e:
        logging.error(f"Error installing updates: {e}")
        return None

def main():
    while True:
        logging.info("Starting PatchPatrol cycle...")
        updates = check_for_updates()
        if updates:
            logging.info("Updates found, proceeding with installation...")
            install_updates()
        else:
            logging.info("No updates found.")

        # Wait for 24 hours before checking again
        time.sleep(86400)

if __name__ == "__main__":
    main()