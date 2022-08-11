import subprocess

# requests
try:
    import requests
except:
    print("Missing requests module")
    print("Installing...")
    subprocess.run(["pip3", "install", "requests"],
                   check=True, stdout=subprocess.PIPE).stdout
    import requests
    print("requests installed!")

# Git (needs to be in PATH)
try:
    import git
except:
    print("Missing GitPython module")
    print("Installing...")
    subprocess.run(["pip3", "install", "GitPython"],
                   check=True, stdout=subprocess.PIPE).stdout
    import git
    print("GitPython installed!")


def get_latest():
    url = "https://raw.githubusercontent.com/astrohr/NEOPlanner/main/version"

    try:
        r = requests.get(url)
        assert r.status_code == 200
        latest_version = r.content.decode().strip()
    except:
        return None

    return latest_version


def update():
    g = git.Git()
    g.pull()
    subprocess.run(["pip3", "install", "-r", "requirements.txt"],
                   check=True, stdout=subprocess.PIPE).stdout


if __name__ == "__main__":
    with open("version") as f:
        current_version = f.read().strip()
    print("Current version:", current_version)
    latest_version = get_latest()
    if latest_version != current_version:
        print("New version available:", latest_version)
        print("Updating...")
        update()
        print("Update complete")
    elif latest_version == current_version:
        print(f"You have the latest version ({current_version})")
    else:
        print("Warning: unable to get latest version information!")
