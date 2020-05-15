FROM ubuntu:16.04
MAINTAINER Deven Desai <deven.desai.amd@gmail.com>

ARG user=deven

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update

RUN apt-get install -y --no-install-recommends sudo
RUN apt-get install -y --no-install-recommends git
RUN apt-get install -y --no-install-recommends emacs24-nox
# RUN apt-get install -y --no-install-recommends

# #install python3
# RUN apt-get install -y python3 python3-setuptools

# # install cmake and ninja
# RUN apt-get install -y cmake
# RUN apt-get install -y ninja-build

# # install misc utilities
# RUN apt-get install -y --no-install-recommends \
#     autoconf \
#     automake \
#     clang-format-3.8 \
#     curl \
#     libcurl4-openssl-dev \
#     libtool \
#     libssl-dev \
#     mlocate \
#     unzip \
#     wget \
#     zip \
#     zlib1g-dev

RUN useradd --create-home $user
RUN usermod --append --groups sudo $user
RUN passwd -d $user

USER $user
WORKDIR /home/$user

RUN git clone https://github.com/deven-amd/.emacs.d.git

RUN git config --global user.email "deven.desai.amd@gmail.com"
RUN git config --global user.name "Deven Desai"
RUN git config --global core.editor "emacs"

# Run an dummy sudo command to suppress the following message
# (which will otherwise appear evertyime you start the container)
#
# To run a command as administrator (user "root"), use "sudo <command>".
# See "man sudo_root" for details.
#
RUN sudo echo

CMD /bin/bash
