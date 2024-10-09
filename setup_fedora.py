import os
import subprocess

def clone_repository(github_user, token):
    repo_url = f"https://{token}@github.com/{github_user}/my-fedora-setup.git"

    # Clone the repository
    try:
        subprocess.run(["git", "clone", repo_url], check=True)
        print("Repository cloned successfully!")
    except subprocess.CalledProcessError:
        print("Failed to clone the repository. Please check your credentials and repository URL.")

def make_scripts_executable(directory):
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".sh"):
                filepath = os.path.join(directory, filename)
                os.chmod(filepath, 0o775)  # Make the script executable
        print("Scripts made executable.")
    except Exception as e:
        print(f"Error making scripts executable: {e}")

def run_scripts(directory):
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".sh"):
                print(f"Running {filename}...")
                subprocess.run([os.path.join(directory, filename)], check=True)
        print("All scripts executed successfully.")
    except subprocess.CalledProcessError:
        print("Error occurred while executing the scripts.")

def main():
    # User input
    github_user = input("Enter your GitHub username: ")
    token = input("Enter your GitHub token: ")

    # Clone the repository
    clone_repository(github_user, token)

    # Change to the cloned repository directory
    repo_directory = os.path.join(os.path.expanduser("~"), "my-fedora-setup")
    os.chdir(repo_directory)

    # Make scripts executable
    make_scripts_executable(repo_directory)

    # Run the scripts
    run_scripts(repo_directory)

if __name__ == "__main__":
    main()
