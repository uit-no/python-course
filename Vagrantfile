# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  # port for jupyter notebook
  config.vm.network "forwarded_port", guest: 8888, host: 8888,
      host_ip: "127.0.0.1", # not visible from outside our host box
      auto_correct: true

  config.vm.provision "shell",
    privileged: false,
    inline: <<-SHELL
    # Python 3.5 on Ubuntu 14.04
    sudo add-apt-repository -y ppa:fkrull/deadsnakes
    sudo apt-get update
    sudo apt-get install -y python3.5-complete
    sudo rm /usr/bin/python3
    sudo ln -s /usr/bin/python3.5 /usr/bin/python3

    # pip on Ubuntu 14.04
    echo "downloading pip..."
    curl -s -O https://bootstrap.pypa.io/get-pip.py
    sudo python3 get-pip.py

    # Anaconda
    echo "downloading Anaconda (this might take a few minutes)..."
    curl -s -O https://repo.continuum.io/archive/Anaconda3-4.0.0-Linux-x86_64.sh
    bash Anaconda3-4.0.0-Linux-x86_64.sh -b
    echo "export PATH=\$PATH:/home/vagrant/anaconda3/bin" | tee -a /home/vagrant/.bashrc
    export PATH=$PATH:/home/vagrant/anaconda3/bin

    # our stuff
    cd /vagrant
    conda create -q -y -n course --file requirements.txt
    source activate course
    echo "source activate course" | tee -a /home/vagrant/.bashrc
  SHELL
end
