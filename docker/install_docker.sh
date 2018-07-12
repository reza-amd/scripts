# based on instructions from the following wiki page
#
# http://confluence.amd.com/pages/viewpage.action?spaceKey=~jpoznano&title=Docker+Images+for+DL+Frameworks
#

curl -fsSL get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo addgroup docker

sudo adduser $LOGNAME docker
