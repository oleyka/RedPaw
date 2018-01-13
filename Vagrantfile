# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 1
	v.customize ["modifyvm", :id, "--vram", "256"]
    v.customize ["modifyvm", :id, "--hwvirtex", "on"]
    v.customize ["modifyvm", :id, "--audio", "none"]
    v.customize ["modifyvm", :id, "--nictype1", "virtio"]
    v.customize ["modifyvm", :id, "--nictype2", "virtio"]
  end

  config.vm.box = "freebsd/FreeBSD-11.1-STABLE"
  config.vm.box_check_update = false
  config.vm.synced_folder ".", "/vagrant", id: "vagrant-root",
    :nfs => true,
    :mount_options => ['soft']

  config.vm.guest = "freebsd"
  config.vm.hostname = "redpaw.local"
  config.vm.network :private_network, ip: "192.168.42.42"
  config.vm.network :forwarded_port, host: 8000, guest: 8000
  config.vm.base_mac = "080027D14C66"
  config.vm.boot_timeout = 600

  config.ssh.forward_agent = true
  config.ssh.forward_x11 = true
  config.ssh.shell = "sh"

  config.vm.provision "shell" do |s|
    s.inline = "env ASSUME_ALWAYS_YES=YES pkg install python"
  end

  config.vm.provision "ansible" do |a|
    a.playbook = "manage/bootstrap-vagrant.yml"
    a.verbose = "vvv"
    a.extra_vars = {
      :ansible_python_interpreter => "/usr/local/bin/python",
      :owner => "admin"
    }
  end
end
