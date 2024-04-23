FROM python:3.12.2-slim

WORKDIR /usr/src/dvm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat-traditional

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/dvm/entrypoint.sh
RUN chmod +x /usr/src/dvm/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/dvm/entrypoint.sh"]