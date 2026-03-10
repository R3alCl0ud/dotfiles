mkdir -p ~/.config/pipewire/pipewire.conf.d
mkdir -p ~/.config/wireplumber/wireplumber.conf.d

echo linking files to pipewire.conf.d/
ln -s ./audioconfig/pipewire/10-link-sinks.conf ~/.config/pipewire/pipewire.conf.d/

echo linking files to wireplumber.d/
ln -s ./audioconfig/wireplumber/10-audio-sinks.conf ~/.config/wireplumber/wireplumber.conf.d
ln -s ./audioconfig/wireplumber/10-no-auto-gain.conf ~/.config/wireplumber/wireplumber.conf.d
