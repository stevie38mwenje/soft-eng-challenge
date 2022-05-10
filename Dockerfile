FROM --platform=linux/amd64 python:3.9.5
# kenny:new
# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Causes all output to stdout to be flushed immediately
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y gnupg2
RUN apt-get install apt-transport-https
RUN apt-get install -y rustc
RUN pip install --upgrade pip
#    apt-key add - && \
# Retrieves packages from Microsoft
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev

RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools

# Adds paths to the $PATH environment variable within the .bash_profile and .bashrc files
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/billingportalapi
COPY requirements.txt start-server.sh /opt/app/
#COPY .pip_cache /opt/app/pip_cache/
COPY . /opt/app/billingportalapi/
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
#RUN sed -i '107s/.*/version_info = (1, 3, 12, "final", 0)/' /usr/local/lib/python3.8/site-packages/pymysql/__init__.py
RUN chown -R www-data:www-data /opt/app
# start server
EXPOSE 8010
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]