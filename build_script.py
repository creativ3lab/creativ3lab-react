import os
import subprocess

REPO_PATH = os.path.dirname(os.path.abspath(__file__))
BUILD_PATH = 'C:\\Projects\\creativ3lab_hosting'
REPO_URL = 'https://github.com/creativ3lab/creativ3lab-react.git'
BRANCH = 'Creativ3lab'

def clone_repo():
    if not os.path.exists(REPO_PATH):
        subprocess.run(['git', 'clone', '-b', BRANCH, REPO_URL, REPO_PATH])
    else:
        subprocess.run(['git', '-C', REPO_PATH, 'fetch'])
        subprocess.run(['git', '-C', REPO_PATH, 'checkout', BRANCH])
        subprocess.run(['git', '-C', REPO_PATH, 'pull', 'origin', BRANCH])

def build_site():
    # Example: Use a static site generator like Jekyll or Hugo
    subprocess.run(['jekyll', 'build', '-s', REPO_PATH, '-d', BUILD_PATH])

def main():
    clone_repo()
    build_site()

if __name__ == '__main__':
    main()
