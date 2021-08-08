FROM --platform=linux/amd64 harbor.dell.com/devops-images/python-devops:3.8_v2.3.0

# Install Python base packages
RUN python3.8 -m pip install --no-cache-dir --upgrade pip

RUN mkdir neoway-case

WORKDIR neoway-case

COPY . ./

RUN pip install -r requirements.txt

CMD ["python3.8", "-m", "main"]
