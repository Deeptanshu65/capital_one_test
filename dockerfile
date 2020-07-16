FROM python:latest
WORKDIR /usr/app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "solution.py"]
