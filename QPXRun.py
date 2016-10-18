import google_flight_api as gf
import sys
t = gf.GoogleFlight("AIzaSyBr1N7_dACHiDKSr02lAgzPUeV4G69PfyY")
origin = str(sys.argv[1])
dest1 = str(sys.argv[2])
dest2 = str(sys.argv[3])

req = {
  "request": {
    "slice": [
      {
        "origin": origin,
        "destination": dest1,
        "date": "2017-10-21"
      },
      {
        "origin": dest2,
        "destination": origin,
        "date": "2017-11-05"
      }
    ],
    "passengers": {
      "adultCount": 2,
      "infantInLapCount": 0,
      "infantInSeatCount": 0,
      "childCount": 2,
      "seniorCount": 0
    },
    "solutions": 10,
    "maxPrice": "GBP1500",
    "saleCountry": "GB",
    "refundable": "false"
  }
}

t.get(req)
#t.readable(t.data)
t.print_result()


#t.print_trip(t.trips)