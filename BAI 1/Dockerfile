FROM ubuntu:20.04

# Cài đặt Java, Python và các công cụ cần thiết
RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    python3 \
    python3-pip \
    wget

# Tải và cài đặt Hadoop
RUN wget https://downloads.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz && \
    tar -xzf hadoop-3.3.4.tar.gz && \
    mv hadoop-3.3.4 /usr/local/hadoop && \
    rm hadoop-3.3.4.tar.gz

# Thiết lập biến môi trường
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV HADOOP_HOME=/usr/local/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

WORKDIR /app

COPY mapper.py reducer.py input_data.txt ./

CMD ["hadoop", "jar", "$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar", \
     "-files", "mapper.py,reducer.py", \
     "-mapper", "python3 mapper.py", \
     "-reducer", "python3 reducer.py", \
     "-input", "/app/input_data.txt", \
     "-output", "/app/output"]