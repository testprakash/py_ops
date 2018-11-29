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

ARG MAVEN_VERSION=3.6.0
ARG USER_HOME_DIR="/root"
ARG SHA=fae9c12b570c3ba18116a4e26ea524b29f7279c17cbaadc3326ca72927368924d9131d11b9e851b8dc9162228b6fdea955446be41207a5cfc61283dd8a561d2f
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
  && echo "${SHA}  /tmp/apache-maven.tar.gz" | sha512sum -c - \
  && tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1 \
  && rm -f /tmp/apache-maven.tar.gz \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"
RUN  dpkg-reconfigure python3


COPY requirements.txt /tmp/requirements.txt
RUN  pip install -r /tmp/requirements.txt

CMD ["python", "/src/project/tests"]
