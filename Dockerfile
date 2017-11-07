FROM alpine:3.6

RUN apk update && \
    apk upgrade && \
    apk add bash && \
    apk add bash-doc && \
    apk add bash-completion && \
    apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

ADD . / ./

RUN pip3 install -r /requirements.txt

EXPOSE 9090

CMD ["python3", "/run.py"]