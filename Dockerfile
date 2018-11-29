FROM python:3.7-stretch


# repo needed for jdk install below.
RUN echo 'deb http://deb.debian.org/debian stretch-backports main' > /etc/apt/sources.list.d/backports.list

# Update image & install application dependant packages.
RUN apt-get update && apt-get install -y \
nano \
libxext6 \
libfreetype6-dev \
libjpeg62-turbo-dev \
libpng-dev \
libmcrypt-dev \
libxslt-dev \
libpcre3-dev \
libxrender1 \
libfontconfig \
uuid-dev \
ghostscript \
curl \
wget \
ca-certificates-java

RUN apt-get -t stretch-backports install -y default-jdk-headless

RUN apt-get install -y maven

RUN  dpkg-reconfigure python3
# Define commonly used JAVA_HOME variable
# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Bundle app source
COPY . /usr/src/app
# RUN rm /etc/ssl/certs/java/cacerts ; update-ca-certificates -f 
ENV MAVEN_OPTS "-Djavax.net.ssl.trustStorePassword=changeit"
# this is just for quick testing 
# ADD pom.xml /tmp/
#RUN mkdir .mvn
#RUN echo -Djavax.net.ssl.trustStorePassword=changeit >  .mvn/jvm.config
ENV PYTHONUNBUFFERED 0
ENV PYTHONPATH /usr/src/app/project:/usr/src/app/project/lib
ENTRYPOINT [ "python", "-m", "project" ]
