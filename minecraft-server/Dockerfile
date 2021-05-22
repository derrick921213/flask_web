# Server執行的環境，我們選用JDK 11
FROM adoptopenjdk/openjdk11

# 說明Minecraft Server在Docker裡運行時的目錄
WORKDIR /mcserver

# Server執行的方式，我這邊就是把官網的執行指令複製下來而已
CMD ["java", "-Xmx1024M", "-Xms1024M", "-jar", "server.jar", "nogui"]