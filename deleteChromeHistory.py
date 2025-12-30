#!/usr/bin/env python3
"""
Safe Chrome/Chromium history cleanup script.
- Detects Chrome/Chromium profiles in ~/.config
- Prompts for confirmation before backing up and deleting History files
- Creates a timestamped .bak before removing files

Run this script manually. It will NOT run automatically.
"""

import os
import shutil
import subprocess
import time
import sys


def find_profiles():
    homedir = os.path.expanduser('~')
    chrome_path = os.path.join(homedir, '.config', 'google-chrome', 'Default')
    chromium_path = os.path.join(homedir, '.config', 'chromium', 'Default')
    available = {}
    if os.path.isdir(chrome_path):
        available['chrome'] = chrome_path
    if os.path.isdir(chromium_path):
        available['chromium'] = chromium_path
    return available


def backup_and_remove(history_path):
    ts = time.strftime('%Y%m%d-%H%M%S')
    dirpath = os.path.dirname(history_path)
    bak = os.path.join(dirpath, f'History.bak.{ts}')
    if os.path.exists(history_path):
        try:
            shutil.move(history_path, bak)
            # try to remove other History* files (journal, shared_memory, etc.)
            for name in os.listdir(dirpath):
                if name.startswith('History') and name != os.path.basename(bak):
                    try:
                        os.remove(os.path.join(dirpath, name))
                    except Exception:
                        # ignore remove errors for non-critical files
                        pass
            print(f'Backed up and removed history. Backup created: {bak}')
            return True
        except Exception as e:
            print(f'Failed to back up/remove history: {e}')
            return False
    else:
        print(f'No History file found at: {history_path}')
        return False


def kill_browser(name):
    # Attempt to kill browser processes by common binary names
    names = []
    if name == 'chrome':
        names = ['google-chrome', 'chrome']
    elif name == 'chromium':
        names = ['chromium', 'chromium-browser']

    for n in names:
        try:
            subprocess.run(['pkill', '-f', n], check=False)
        except Exception:
            pass


def main():
    avail = find_profiles()
    if not avail:
        print('No Chrome or Chromium profiles found in ~/.config. Nothing to do.')
        sys.exit(0)

    print('Detected profiles:')
    for k, p in avail.items():
        print(f' - {k}: {p}')

    default = 'chrome' if 'chrome' in avail else list(avail.keys())[0]
    choice = input(f'Which target to clean? (chrome/chromium) [{default}]: ').strip().lower() or default
    if choice not in avail:
        print('Invalid choice; aborting.')
        sys.exit(1)

    confirm = input('This will permanently delete local history files (a timestamped .bak will be created). Type YES to confirm: ')
    if confirm != 'YES':
        print('Aborted by user.')
        return

    kill = input('Kill browser processes before delete? (y/N): ').strip().lower()
    if kill == 'y':
        print('Killing browser processes...')
        kill_browser(choice)

    history_path = os.path.join(avail[choice], 'History')
    backup_and_remove(history_path)
    print('Operation complete.')


if __name__ == '__main__':
    main()