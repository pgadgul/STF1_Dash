FROM python:3

WORKDIR /src

COPY /src .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8050

CMD ["python", "app.py"]
