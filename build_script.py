import os
import subprocess

REPO_PATH = os.path.dirname(os.path.abspath(__file__))
BUILD_PATH = 'C:\Projects\creativ3lab_hosting'

def clone_repo():
    if not os.path.exists(REPO_PATH):
        subprocess.run(['git', 'clone', 'https://your-git-server/repo.git', REPO_PATH])
    else:
        subprocess.run(['git', '-C', REPO_PATH, 'pull'])

def build_site():
    # Example: Use a static site generator like Jekyll or Hugo
    subprocess.run(['jekyll', 'build', '-s', REPO_PATH, '-d', BUILD_PATH])

def main():
    clone_repo()
    build_site()

if __name__ == '__main__':
    main()
