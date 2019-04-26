
python_mods="./requirements.txt"

if [ -f $python_mods ]; then
    print "Installing modules from $python_mods"
    pip install -r $python_mods
fi

