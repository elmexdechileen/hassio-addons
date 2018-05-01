ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Try to fix repos
RUN echo "ipv6" >> /etc/modules


# Install requirements for add-on
RUN apk add --no-cache python3 alpine-sdk python3-dev jq &&\
	python3 -m ensurepip &&\
	pip3 install paho-mqtt bitarray

# Copy data for add-on
COPY run.sh /
ADD source /usr/opt/telnetmqtt

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
