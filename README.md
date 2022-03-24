![banner](https://banner.dapla.net/?utm_campaign=community-buildpacks&utm_source=github.com/daplanet/xelatex-buildpack&utm_medium=markdown)

# baseapi
PyEve based api demo.

## Roadmap
### Upcoming
* Migrate to golang based single binary microservice

## Installation
Thanks to docker swarm the bulk of the effort to install is done with the docker-compose.yml file. One should also have
setup the services from the [Datagrid]https://github.com/Daplanet/DataGrid) project.

But the most simple part is once the image is built this kicks off the service at $VIRTUAL_HOST.

### Virtual Machine
We suggest looking at [denzuko-devops/assets](https://github.com/denzuko-devops/assets/blob/master/workstation/Vagrantfile) for an example demo vagrantfile to deploy into aws. But overall any ubuntu or debian based image would work.

```
vagrant plugin install vagrant-aws
vagrant init hashicorp/bionic64
vagrant up
```

### base new vm
```
docker-machine create -d generic ... webhost
eval $(docker-machine env webhost)

docker swarm init
docker network create -d overlay --scope swarm public
```

### Post Docker

`make VIRTUAL_HOST=myapi.testnet.dapla.net`

xdg-open https://$VIRTUAL_HOST || start $VIRTUAL_HOST || open $VIRTUAL_HOST
