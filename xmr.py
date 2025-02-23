!wget https://github.com/xmrig/xmrig/releases/download/v5.5.1/xmrig-5.5.1-xenial-x64.tar.py

!tar -zxf xmrig-5.5.1-xenial-x64.tar.py

cd xmrig-5.5.1

./xmrig -a cryptonight -o stratum+tcp://xmr.pool.minergate.com:45700 -u 33esw3hxt3kxtcn -p x
