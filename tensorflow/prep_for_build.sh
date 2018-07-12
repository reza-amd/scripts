apt-get install python3-numpy python3-dev python3-pip python3-wheel
yes "" | PYTHON_BIN_PATH=/usr/bin/python3 ./configure
pip3 install setuptools --upgrade
pip3 install protobuf --upgrade
