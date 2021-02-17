FROM nodered/node-red

RUN npm install node-red-contrib-bigtimer
RUN npm install node-red-dashboard
RUN npm install node-red-contrib-boolean-logic-ultimate
RUN npm install node-red-contrib-calc
RUN npm install node-red-contrib-influxdb

# Define volume for Node-RED userdata: Settings, flows, ...
VOLUME ["/data"]

