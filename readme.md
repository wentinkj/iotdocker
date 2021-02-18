# docker iot setup
Een test/voorbeeld setup van mijn toekomstige IOT setup, met als belangrijkste componenten:
* [mqtt](https://mosquitto.org/) - eclipse mosquitto voor messaging
* [node-red](https://nodered.org/) - dataverwerking, nu specifiek mqtt berichten naar influxdb
* [influxdb](https://www.influxdata.com/) - timeseries database
* [grafana](https://grafana.com/) - visualisatie van de data
* dsmr - nu een simulatie die random data instuurt op mqtt, straks uitlezen belangrijkste waarden van de slimme meter zie ook start in dsmr.py
* _solar_ - voor het uitlezen van de zonnepanelen
* _..._ - en wat nog meer :-)
* _traefik_ - wens, als proxy/entrypoint voor de verschillende services 

Na het starten via compose in de huidige configuratie loopt de simulatie al en komt er data in influxdb.
Met grafana kun je hiermee stoeien..

Voor huidige wachtwoorden en poortmappings kijk even in de compose file en .env

