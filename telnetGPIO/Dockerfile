#ARG BUILD_FROM
#FROM $BUILD_FROM
#FROM hassioaddons/base-amd64
FROM hassioaddons/base-armhf

ENV LANG C.UTF-8

# Install requirements for add-on
RUN apk add --no-cache python3 alpine-sdk python3-dev jq &&\
	python3 -m ensurepip && \
	pip3 install paho-mqtt bitarray
	
# Copy data for add-on
COPY run.sh /
ADD source /usr/opt/telnetmqtt

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
