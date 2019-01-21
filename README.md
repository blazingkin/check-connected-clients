# check-connected-clients
Checks currently connected clients to an Archer A7 router

For use with hardware version `Archer A7 v5.0` and firmware version `1.0.7 Build 20181210`

### Dependencies

1. Docker


### To use,

1. Clone the repository
2. Create a `.env` file that looks like the following

```
ROUTER_IP=192.168.1.1 # Example, may be 192.168.2.1 or other
ADMIN_PASS=***** # Admin password for the router
```

3. Run the following `docker build . -t router_scrape && docker run --env-file .env -it router_scrape`

4. The output contains the names, ips and mac addresses of all connected wireless clients