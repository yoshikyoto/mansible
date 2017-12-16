# coding: utf-8
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # vagrant box list とかで出てくるやつ
  config.vm.box = "centos/7"
  config.vm.hostname = "vagrant"

  # Macのポート 8080 をvagrant の 80 につなげる
  config.vm.network "forwarded_port", guest: 80, host: 8080

  # ipアドレス ipは適当に変更しておｋ
  config.vm.network :private_network, ip: "192.168.33.114"
  config.ssh.insert_key = false
  config.ssh.forward_agent = true

  # ホストとディレクトリを同期する例
  # config.vm.synced_folder "applications", "/home/vagrant/applications", create: true, mount_options: ["uid=vagrant,gid=vagrant"]

  # ansibleの設定
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/playbook.yml"
  end
end
