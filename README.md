# My Fedora Setup

This repository contains scripts to replicate my Fedora setup on a new machine.

## Steps to Execute the Scripts on a New Machine

1. **Prepare the New Machine:**
   - Install Fedora on your new machine.
   - Make sure the machine is connected to the internet.

2. **Install Git (if not already installed):**
   - Open a terminal and run the following command:
     ```bash
     sudo dnf install git
     ```

3. **Clone the GitHub Repository:**
   - In the terminal, navigate to the directory where you want to clone the repository (e.g., your home folder):
     ```bash
     cd ~
     ```
   - Clone the repository with the following command (replace `<TOKEN>` with your personal access token):
     ```bash
     git clone https://github.com/alissoninacio1/my-fedora-setup.git
     ```

4. **Navigate to the Cloned Directory:**
   - After cloning the repository, enter the directory:
     ```bash
     cd my-fedora-setup
     ```

5. **Execute the Scripts:**
   - To run all the installation scripts you created, use the following command:
     ```bash
     chmod +x *.sh  # To make all scripts executable
     ```
   - Now you can execute each script individually, for example:
     ```bash
     ./install_packages.sh
     ./configure_system.sh
     ```
   - Alternatively, if you have a main script that calls the others, simply run that script.

6. **Verify Everything Is Correct:**
   - After executing the scripts, check if the applications and settings are as expected.

## Additional Tips
- **Documentation:** Keep a README in the repository with instructions on how to use the scripts. This can help in setting up new machines in the future.
- **Updates:** Whenever you make changes to the scripts, be sure to update the GitHub repository so that the latest version is available.
- **Testing:** Consider testing the scripts in a virtual machine before running them on a production system.
