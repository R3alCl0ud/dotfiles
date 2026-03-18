import os
# import pwd
from typing import Any

import pulsectl
import shutil
from simple_term_menu import TerminalMenu

# REPLACEMENT_STR = "$REPLACE_WITH_ACTUAL_OUTPUT_SINK"
PH_OUTPUT = "$OUTPUT_SINK_PLACEHOLDER"
PW_SRC = f"{os.getcwd()}/audioconfig/pipewire"
WP_SRC = f"{os.getcwd()}/audioconfig/wireplumber"


PW_DEST = f"/home/{os.getlogin()}/.config/pipewire/pipewire.conf.d"
WP_DEST = f"/home/{os.getlogin()}/.config/wireplumber/wireplumber.conf.d"


wireplumber = (WP_SRC, WP_DEST)
pipewire = (PW_SRC, PW_DEST)

programs = [wireplumber, pipewire]

def main(copy: bool = False):
    # Ask for sink to use as output and then generate and write to disk the link-sinks.conf file
    selected = ask_for_sink()
    generate_config(selected)
    # clean the destination so the final files do not fail to link/copy
    for program in programs:
        clean_dest(program[1])

    if copy:
        copy_configs()
    else:
        symlink_configs()
    return True

def ask_for_sink():
    sink_names = get_sink_names()
    sink_menu = TerminalMenu(sink_names, title="Select an audio sink:")
    selected = sink_names[sink_menu.show()]
    print("Selected sink:", selected)
    return selected


def generate_config(selected_sink):
    with open(f"{pipewire[0]}/templates/10-link-sinks.conf") as input_file:
        content = input_file.read().replace(PH_OUTPUT, selected_sink)
        with open('./audioconfig/pipewire/generated/10-link-sinks.conf', 'w') as output_file:
            output_file.write(content)


def symlink_configs():
    for program in programs:
        print(f"Linking {program[0]} to {program[1]}")
        for suffix in ["", "/generated"]:
            for entry in os.scandir(f"{program[0]}{suffix}"):
                if entry.is_file() and entry.name.endswith(".conf"):
                    os.symlink(entry.path, f"{program[1]}/{entry.name}")


def copy_configs():
    for program in programs:
        print(f"Copying {program[0]} to {program[1]}")
        for suffix in ["", "/generated"]:
            for entry in os.scandir(f"{program[0]}{suffix}"):
                if entry.is_file() and entry.name.endswith(".conf"):
                    shutil.copy(entry.path, f"{program[1]}/{entry.name}")


def clean_dest(dest):
    for entry in os.scandir(dest):
        print(f"Removing {entry.path}")
        os.remove(entry.path)

def get_sink_names():
    pulse = pulsectl.Pulse()
    names = []
    for sink in pulse.sink_list():
        names.append(sink.name)
    names.sort()
    return names
