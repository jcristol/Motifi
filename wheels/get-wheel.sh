git clone https://github.com/Jamonek/Robinhood
cd Robinhood
python setup.py bdist_wheel --universal
mv dist/Robinhood-1.0.1-py2.py3-none-any.whl ..
cd ..
rm -rf Robinhood
