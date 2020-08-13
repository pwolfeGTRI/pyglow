# Run as:
#
# $ docker build -t pyglow_image .
#

# Start with a Python base image:
FROM python:3.6-buster

# Install required Linux tools:
RUN apt update && apt install -y \
    x11-apps \
    unzip \
    rsync \
    gfortran \
    perl  

# Install pyglow Python dependencies:
COPY requirements.txt /
RUN pip3 install -r requirements.txt

# Copy source code into container:
COPY src/ /pyglow/src/
COPY test/ /pyglow/test/
COPY examples/ /pyglow/examples
COPY setup.py /pyglow
WORKDIR /pyglow

# Compile & install:
RUN make -C src/pyglow/models source
RUN python3 setup.py install --user

# # Run unit tests:
# CMD coverage run --source src -m pytest test/
# # Run graphics test:
# CMD /usr/bin/xeyes

# notes to start container run
# docker run -it -e DISPLAY=host.docker.internal:0 --name my_pyglow pyglow_image /bin/bash
# docker ps to check if running
# docker exec -it my_pyglow /bin/bash to join a running container

CMD /usr/bin/bash