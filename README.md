pyfroniussolarapi
=================

What?

Fronius Solar API v1 (JSON) wrapper in python

It is planned to add a "dashboard" script that shows live data based on matplotlib
to demonstrate the API features.

As I got just the solar inverter, but no "Sensorbox" etc., sensor and mains meter
functionality is missing or untested.



Why?

Fronius provides solarweb.com for data logging of their solar inverters.
But:
    a) they offer "premium" access for free only for a limited amount of time,
       after that they want money for the detailed report (e.g. on MPPT level)
    b) I want to combine the inverter data with other data sources (e.g. smart meter),
       weather data/forecast etc etc. I want to do this on my own server.

How?

Fronius published an JSON API documentation (Google: Fronius Solar API V1). This wrapper is based
on that pdf.

Fun fact: The data logger runs Linux / Busybox :)
