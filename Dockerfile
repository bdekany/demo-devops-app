FROM opensuse:leap
MAINTAINER Brice DEKANY
RUN zypper install -y python-Flask python-Jinja2 python-redis
ADD ./app /app/
WORKDIR /app
EXPOSE 9000
CMD ["python", "app.py"]
