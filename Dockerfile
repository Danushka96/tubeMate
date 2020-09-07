# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
COPY . .
RUN npm run build

# deploy stage
FROM python:3.7-alpine
MAINTAINER "Danushka Herath (https://github.com/danushka96)"
WORKDIR app
COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps gcc musl-dev openssl-dev libffi-dev libxslt-dev
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY --from=build-stage /app/templates ./templates
COPY tubemate.py .
COPY wsgi.py .
RUN apk del .build-deps gcc musl-dev openssl-dev libffi-dev libxslt-dev
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
