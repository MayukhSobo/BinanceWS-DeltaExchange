FROM python:3.8
LABEL maintainer="Mayukh Sarkar <mayukh2012@hotmail.com>"
# RUN apk --no-cache add ca-certificates
COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt
COPY . .
CMD [ "python", "./main.py" ]