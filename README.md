# baseapi
PyEve based api demo.


## Installation
Thanks to docker swarm the bulk of the effort to install is done with the docker-compose.yml file. One should also have
setup the services from: https://github.com/Dallas-Makerspace/CommunityGrid.

But the most simple part is once the image is built this kicks off the service at $VIRTUAL_HOST.

### Virtual Machine
I'd suggest looking at [denzuko-devops/assets](https://github.com/denzuko-devops/assets/blob/master/workstation/Vagrantfile) for an example demo vagrantfile to deploy into aws. But overall any ubuntu based would work.

```
vagrant plugin install vagrant-aws
vagrant init hashicorp/precise64
vagrant up
```

### base new vm
```
docker-machine create -d generic ... webhost
eval $(docker-machine env webhost)

docker swarm init
docker network create -d overlay --scope swarm
```

### Post Docker

`make VIRTUAL_HOST=myapi.testnet.dapla.net`

xdg-open https://$VIRTUAL_HOST || start $VIRTUAL_HOST || open $VIRTUAL_HOST
