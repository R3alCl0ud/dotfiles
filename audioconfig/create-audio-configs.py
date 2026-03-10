import pulsectl
from simple_term_menu import TerminalMenu

replacment_str = "$REPLACE_WITH_ACTUAL_OUTPUT_SINK"

def main():
    pulse = pulsectl.Pulse()
    sink_names = get_sink_names()
    sink_menu = TerminalMenu(sink_names)
    print("Select an audio sink:")
    selected = sink_names[sink_menu.show()]
    print("Selected sink:", selected)

    with open("./audioconfig/generated/10-link-sinks.conf", "w") as output_file:
        with open("./audioconfig/pipewire/10-link-sinks.conf.template", "r") as input_file:
            content = input_file.read()
            content = content.replace(replacment_str, selected)
            output_file.write(content)

def get_sink_names():
    pulse = pulsectl.Pulse()
    names = []
    for sink in pulse.sink_list():
        names.append(sink.name)
    return names



if __name__ == "__main__":
    main()