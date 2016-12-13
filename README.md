NDN-FCH (Find Closest Hub)
==========================

NDN-FCH (Find Closest Hub) is a geolocation service application for the Named Data Networking (NDN) network. It aims to provide end hosts connecting to the NDN hub network with the ability to quickly locate the NDN hub closest to their current location.

## Deployment Instructions

### Prerequisites

- Python 3
- `pip`
- `virtualenv`

### Creating python environment and dependency installation

    virtualenv .python
    source .python/bin/activate
    pip install -r requirements.txt
    deactivate

### Configuration

    cp config.dist.py config.py
    ## edit config.py

### Database download

To manually download geo-ip mapping and hub position databases:

    ./manage.py update_geodb
    ./manage.py update_hubs

These database need to be periodically refreshed, e.g., using a daily/weekly cronjob

    TBD

## Run the Application

```sh
./manage.py runserver
```

So access the application at the address [http://localhost:5000/](http://localhost:5000/)

> Want to specify a different port?

> ```sh
> $ ./manage.py runserver -h 0.0.0.0 -p 8080
> ```
