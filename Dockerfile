FROM alpine:3.6

ENV APP_DIR /app

RUN apk update && \
    apk upgrade && \
    apk add bash && \
    apk add bash-doc && \
    apk add bash-completion && \
    apk add mysql-client && \
    apk add --no-cache python3 supervisor && \
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

#exec gunicorn --workers 3 --bind 127.0.0.1:9090 app:app
#CMD ["gunicorn", "--workers", "3", "--bind", ":9090", "app:app"]
#CMD ["python3", "/run.py"]
CMD ["supervisord", "-c", "/etc/supervisord.conf"]
