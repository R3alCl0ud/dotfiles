import os

import pulsectl
import shutil
from simple_term_menu import TerminalMenu

replacment_str = "$REPLACE_WITH_ACTUAL_OUTPUT_SINK"


def main(copy:bool=False):
    selected_sink = ask_for_sink()
    link_sinks_content = generate_config(selected_sink)
    with open("./audioconfig/generated/10-link-sinks.conf", "w") as output_file:
        output_file.write(link_sinks_content)
        try:
            if copy:
                print("copying generated config to ~/.config/pipewire/pipewire.conf.d/10-link-sinks.conf")
                shutil.copy("./audioconfig/generated/10-link-sinks.conf",
                            "~/.config/pipewire/pipewire.conf.d/10-link-sinks.conf")
            else:
                print("symlinking generated config to ~/.config/pipewire/pipewire.conf.d/10-link-sinks.conf")
                os.symlink("./audioconfig/generated/10-link-sinks.conf",
                           "/.config/pipewire/pipewire.conf.d/10-link-sinks.conf")
        except Exception as e:
            return e
    return True

def ask_for_sink():
    sink_names = get_sink_names()
    sink_menu = TerminalMenu(sink_names, title="Select an audio sink:")
    selected = sink_names[sink_menu.show()]
    print("Selected sink:", selected)
    return selected

def generate_config(selected_sink):
    with open("./audioconfig/pipewire/10-link-sinks.conf.template") as input_file:
        content = input_file.read()
        return content.replace(replacment_str, selected_sink)

def get_sink_names():
    pulse = pulsectl.Pulse()
    names = []
    for sink in pulse.sink_list():
        names.append(sink.name)
    return names
