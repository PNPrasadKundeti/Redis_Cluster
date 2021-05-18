# Redis_Cluster
Redis Cluster Creation OSS and Enterprise 
Redis OSS/Enterprise Installation and Configuration Exercise
============================================================
 
1. Download and install standalone Redis OSS, version 6.x, on GCP Instance 1.

Step 1: download the Redis OSS from  https://redis.io/download 
Step 2: run the following commands

$ wget https://download.redis.io/releases/redis-6.2.3.tar.gz
$ tar xzf redis-6.2.3.tar.gz
$ cd redis-6.2.3
$ make

Started the server using the following command

$ src/redis-server

Started the Redis CLI using the following command for testing the connectivity

$ src/redis-cli

redis> set foo bar
OK
redis> get foo
"bar"
￼

2. Use RedisLabs' memtier-benchmark utility to load some data into a standalone Redis DB on Redis OSS.

Step 1: Installing the RedisLabs memtier-benchmark utility 
apt-get install build-essential autoconf automake libpcre3-dev libevent-dev pkg-config zlib1g-dev libssl-dev

Step 2: Clone the git repository 
git clone https://github.com/RedisLabs/memtier_benchmark.git
cd memtier_benchmark

Step3: Run the autoreconf and make the application 
autoreconf -ivf
./configure
make


Step4: verify version of meatier-benchmark 

./memtier_benchmark --version


Step 5: imported some sample data from https://github.com/redis-developer/redis-datasets/blob/movie-dataset/movie-database/import_actors.redis 
Pushed into the Redis cluster
￼

 
3. Download and install Redis Enterprise GA version on EC2 Instance 2 using the no DNS option.
   A) Use "wget https://s3.amazonaws.com/redis-enterprise-software-downloads/6.0.20/redislabs-6.0.20-69-xenial-amd64.tar"

Installation of Redis Enterprise:

Verifying the OS: its Ubuntu 18.04.1 LTS bionic
trainee@interview-2:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.1 LTS
Release:	18.04
Codename:	bionic

Step1: Downloaded the comparable software as the above provided links is of incorrect (Xenial vs Bionic)

redislabs-6.0.20-69-bionic-amd64.tar

Step 2: Extracted the software 

trainee@interview-2:~$ ls
redislabs-6.0.20-69-bionic-amd64.tar
trainee@interview-2:~$ chmod -R 777 .
trainee@interview-2:~$ ls
redislabs-6.0.20-69-bionic-amd64.tar

trainee@interview-2:~$ tar -xvf redislabs-6.0.20-69-bionic-amd64.tar 

Step 3: installed the software using install.sh script

trainee@interview-2:~$ sudo ./install.sh

Step 4: Verified the installation is completed

Summary:
-------
ALL TESTS PASSED.


2021-05-16 22:59:54.156 [!] Please logout and login again to make sure all environment changes are applied.
2021-05-16 22:59:54.158 [!] Point your browser at the following URL to continue:
2021-05-16 22:59:54.162 [!] https://192.168.0.62:8443
￼

Step 5: Access the URL with in the console

trainee@interview-2:~$ curl https://<IPAddress>:8443 -kv
￼

Note: I’m not able to access link from the browser as the port 53 is occupied, so performed the following steps to resolve it as mentioned in the requirement 

Step 6: Copy the steps from the following link and run it. 
https://docs.redislabs.com/latest/rs/getting-started/ 

1. Run: sudo vi /etc/systemd/resolved.conf
2. Add DNSStubListener=no as the last line in the file and save the file.
3. Run: sudo mv /etc/resolv.conf /etc/resolv.conf.orig
4. Run: sudo ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf
5. Run: sudo service systemd-resolved restart

Step 7: Now access the link Redis enterprise link on https://<IPAddress>:8443/#/setup 
￼

4. Within Redis Enterprise, create a single node cluster and an empty database.

Step1: Setting up the cluster using default options
￼
Step2: Don’t have the license key so using the trail version 
￼
Step 3: Setting up the default admin credentials using my personal id
￼
Step 4: Creating a empty database

￼

5. Enable "Replica Of" between the Redis Enterprise and the Redis OSS databases - where your Source DB is "Redis OSS" and your Target DB is "Redis Enterprise".

6. Write a small script/program using a language of your choice (e.g. Java, Python, Ruby, Go, C#, or JavaScript) to complete the following:
   A) Insert the values 1-100 into the Redis OSS database on GCP Instance 1.
   B) Read and print them in a reverse order from the Redis Enterprise database on GCP Instance 2.

import redis
  
r = redis.Redis(
    host='<Cluster IP Address>',
    port=<Redis Port>)
i=1
while(i < 101):
    r.rpush('demolist', i)
    i += 1
#Print out the values from 1 - 100  
print(r.lrange('demolist', 0, -1))


python script.py [‘1’, ‘2’, ‘3’, ‘4’, ‘5’, ‘6’, ‘7’, ‘8’, ‘9’, ‘10’, ‘11’, ‘12’, ‘13’, ‘14’, ‘15’, ‘16’, ‘17’, ‘18’, ‘19’, ‘20’, ‘21’, ‘22’, ‘23’, ‘24’, ‘25’, ‘26’, ‘27’, ‘28’, ‘29’, ‘30’, ‘31’, ‘32’, ‘33’, ‘34’, ‘35’, ‘36’, ‘37’, ‘38’, ‘39’, ‘40’, ‘41’, ‘42’, ‘43’, ‘44’, ‘45’, ‘46’, ‘47’, ‘48’, ‘49’, ‘50’, ‘51’, ‘52’, ‘53’, ‘54’, ‘55’, ‘56’, ‘57’, ‘58’, ‘59’, ‘60’, ‘61’, ‘62’, ‘63’, ‘64’, ‘65’, ‘66’, ‘67’, ‘68’, ‘69’, ‘70’, ‘71’, ‘72’, ‘73’, ‘74’, ‘75’, ‘76’, ‘77’, ‘78’, ‘79’, ‘80’, ‘81’, ‘82’, ‘83’, ‘84’, ‘85’, ‘86’, ‘87’, ‘88’, ‘89’, ‘90’, ‘91’, ‘92’, ‘93’, ‘94’, ‘95’, ‘96’, ‘97’, ‘98’, ‘99’, ‘100’]
