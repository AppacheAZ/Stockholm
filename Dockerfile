FROM python:latest
COPY run.sh /run.sh
COPY services /services
RUN chmod +x run.sh
RUN chmod +x services
RUN chmod +x services/*

RUN pip install cryptography
ENTRYPOINT ["/run.sh"]