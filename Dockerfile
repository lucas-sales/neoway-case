FROM python:3.8-slim-buster

# Install Python base packages
RUN python3.8 -m pip install --no-cache-dir --upgrade pip

RUN mkdir neoway-case

WORKDIR neoway-case

COPY . ./

RUN pip install -r requirements.txt

CMD ["python3.8", "-m", "main"]
