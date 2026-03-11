echo "Creating python virtual environment"
python -m venv dotfiles
echo "Entering virtual environment"
source .venv/bin/activate
echo "Entered virtual environment"
echo "Installing python dependencies"
pip install simple_term_menu pulsectl
echo "Running Python Program"
python index.py