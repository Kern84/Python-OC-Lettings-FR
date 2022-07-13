FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

COPY . .

CMD python3 manage.py runserver 0.0.0.0:$PORT