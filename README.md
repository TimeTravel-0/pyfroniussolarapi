pyfroniussolarapi
=================

What?

Fronis Solar API v1 (JSON) wrapper for Datamanager 2 card in python

It is planned to add a "dashboard" script that shows live data based on matplotlib



Why?

Fronius provides solarweb.com for data logging of their solar inverters.
But:
    a) they offer "pro" access for free only for a limited amount of time,
       after that they want money for the detailled report (e.g. on MPPT level)
    b) I want to combine the inverter data with other data sources (e.g. smart meter),
       weather data/forecast etc etc. I want to do this on my own server.

How?

Fronius published an JSON API documentation (Google: Fronis Solar API V1). I based this wrapper
on that pdf.

Fun fact: The data logger runs Linux / Busybox :)
