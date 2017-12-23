ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install requirements for add-on
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    rm -rf /var/cache/apk/*


# Copy data for add-on
COPY ./source/pigpio.py /usr/lib/python3.5/site-packages/pigpio.py
COPY ./source/main.py /main.py

RUN chmod a+x /main.py

COPY run.sh /


RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
