set -e

apt-get update 

apt-get install -y --no-install-recommends \
	apt-transport-https \
	ca-certificates \
	software-properties-common 

apt-get install -y \
	curl \
	emacs \
	git \
	sudo \
	vim \
	wget

apt-get clean
rm -rf /var/lib/apt/lists/*
