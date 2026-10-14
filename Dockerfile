FROM python:3.12-slim
WORKDIR /lab
COPY app ./app
COPY tools ./tools
COPY sample-data ./sample-data
USER 65532:65532
EXPOSE 8080
ENV LAB_HOST=127.0.0.1 LAB_PORT=8080
CMD ["python", "app/lab_server.py"]
