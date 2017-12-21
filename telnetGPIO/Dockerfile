ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install requirements for add-on
RUN apk add --no-cache python3 alpine-sdk python3-dev jq &&\
	python3 -m ensurepip && \
	pip3 install paho-mqtt bitarray
	
# Copy data for add-on
COPY run.sh /
ADD source /usr/opt/telnetmqtt

# Add config
CONFIG_PATH=/data/options.json

mqtthost="$(jq --raw-output '.mqtthost' $CONFIG_PATH)"
mqttport="$(jq --raw-output '.mqttport' $CONFIG_PATH)"
servicename="$(jq --raw-output '.servicename' $CONFIG_PATH)"
gpiohost="$(jq --raw-output '.gpiohost' $CONFIG_PATH)"
refreshinterval="$(jq --raw-output '.refreshinterval' $CONFIG_PATH)"

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
