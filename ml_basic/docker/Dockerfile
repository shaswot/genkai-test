FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
# Minimal docker image to start jupyterlab
# Refer requirements.txt for environment packages
# Does not have linux packages to support rendering
# Does not override jupyterlab defaults

# Set bash as the default shell
ENV SHELL=/bin/bash

# Build with some basic utilities
RUN apt-get -yqq update --fix-missing
RUN apt-get -yqq install \
	python3-pip \
	apt-utils \
	vim \
	git \
	screen \
	htop \
	wget \
	net-tools \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# folder to share files with host machine
# /stash folder stores large dumpfiles that can be accessed from the host computer
RUN mkdir -p /stash
VOLUME /stash

# build with some basic python packages
RUN pip install --upgrade pip
RUN pip install \
	jupyterlab \
	ipywidgets \
	ipynbname \
	autopep8 \
	gitpython \
	matplotlib \
	tqdm 
	
# Install other packages
COPY ./docker/requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# define the port number(s) the container should expose
# All running containers expose 8888 and 6006
# They are redirected to other ports using docker -p <machine_port>:8888
EXPOSE 8888
EXPOSE 6006

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION=v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

# start jupyter lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser", "--notebook-dir=/"]
