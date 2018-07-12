rm -rf build
mkdir build
cd build

#-DCMAKE_BUILD_TYPE=Debug

cmake -DEIGEN_TEST_CXX11=ON -DEIGEN_TEST_HIP=ON ..

#make check -j$(nproc)

#make check -j$(nproc) >& run_tests.log &
