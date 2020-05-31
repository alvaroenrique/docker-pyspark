
FROM ubuntu:18.04

ARG URL_SPARK="https://downloads.apache.org/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz"
ARG SPARK_FILE="spark-2.4.5-bin-hadoop2.7"
ARG SPARK_HOME="/opt/$SPARK_FILE"


# Opcional, cambia el mirror a http://ubuntu.c3sl.ufpr.br/ubuntu/
RUN \
  sed -i 's/security\.ubuntu\.com\/ubuntu/ubuntu\.c3sl\.ufpr\.br\/ubuntu/g' /etc/apt/sources.list && \
  sed -i 's/archive\.ubuntu\.com\/ubuntu/ubuntu\.c3sl\.ufpr\.br\/ubuntu/g' /etc/apt/sources.list 

RUN apt-get update 

RUN apt-get -yy install openjdk-8-jdk openjdk-8-jre curl
RUN echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64' >> ~/.profile 

RUN curl -O https://downloads.apache.org/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz
RUN tar xzf spark-2.4.5-bin-hadoop2.7.tgz 
RUN mv spark-2.4.5-bin-hadoop2.7 /opt 
RUN echo "export SPARK_HOME=/opt/spark-2.4.5-bin-hadoop2.7" >> ~/.profile 
RUN /bin/bash -c "source ~/.profile"
RUN cp "$SPARK_HOME/conf/spark-env.sh.template" "$SPARK_HOME/conf/spark-env.sh" 
RUN rm -r spark-2.4.5-bin-hadoop2.7.tgz 
RUN ln -s /usr/bin/python3 /usr/bin/python 
RUN apt-get -yy install python3 python3-pip 
RUN cd "$SPARK_HOME/python" && python setup.py install 


CMD ["bash"]