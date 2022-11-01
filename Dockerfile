FROM alpine:3.15

ENV APP_DIR /app

RUN apk update && \
    apk upgrade && \
    apk add bash && \
    apk add gcc && \
    apk add bash-doc && \
    apk add bash-completion && \
    apk add mysql-client && \
    apk add python-dev && \
    apk add python3-dev && \
    apk add g++ && \
    apk add libffi-dev musl-dev linux-headers && \
    apk add --no-cache supervisor && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache && \
    echo "files = ${APP_DIR}/conf/*.ini" >> /etc/supervisord.conf


ADD . / ./

RUN pip3 install -r /requirements.txt

VOLUME ["${APP_DIR}"]

EXPOSE 9090

CMD ["supervisord", "-c", "/etc/supervisord.conf"]
