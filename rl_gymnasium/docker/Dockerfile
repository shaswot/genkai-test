FROM ml_basic:20240820

RUN apt-get -yqq update --fix-missing
RUN apt-get -yqq install \
	swig \
    	patchelf \
   	curl \
    	libgl1-mesa-dev \
    	libgl1-mesa-glx \
   	libglew-dev \
    	libosmesa6-dev \
    	software-properties-common \
    	xpra \
    	xserver-xorg-dev \
    && 	apt-get clean \
    && 	rm -rf /var/lib/apt/lists/*

RUN mkdir -p /root/.mujoco \
    && wget https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz -O mujoco.tar.gz \
    && tar -xf mujoco.tar.gz -C /root/.mujoco \
    && rm mujoco.tar.gz

ENV LD_LIBRARY_PATH=/root/.mujoco/mujoco210/bin:${LD_LIBRARY_PATH}
ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}

# Install other packages
COPY ./docker/requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
