# Needs to have git in global path
import requests
import subprocess
try:
    import git
except:
    print("Missing GitPython module")
    print("Installing...")
    subprocess.run(["pip3", "install", "GitPython"],
                   check=True, stdout=subprocess.PIPE).stdout
    import git
    print("GitPython installed!")


def check_updates():
    with open("version") as f:
        current_version = f.read().strip()

    url = "https://raw.githubusercontent.com/astrohr/NEOPlanner/main/version"

    try:
        r = requests.get(url)
        assert r.status_code == 200
        latest_version = r.content.decode().strip()
    except:
        return None

    if latest_version != current_version:
        return latest_version
    return False


def update():
    g = git.Git()
    g.pull()
    subprocess.run(["pip3", "install", "-r", "requirements.txt"],
                   check=True, stdout=subprocess.PIPE).stdout


if __name__ == "__main__":
    with open("version") as f:
        current_version = f.read().strip()
    print("Current version:", current_version)
    status = check_updates()
    if status:
        print("New version available:", status)
        print("Updating...")
        update()
        print("Update complete")
    elif status == False:
        print(f"You have the latest version ({current_version})")
    else:
        print("Warning: unable to get latest version information!")
