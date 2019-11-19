import datetime

from se9 import db

def search(
  arrivalDate, duration,
  paxCount=None, paxAges=None, destination=None, productCategory=None,
  productType=None, brand=None, name=None, reviewScore=None, starRating=None,
  board=None, budget=None, accommodationType=None, accommodationFacilities=None
  ):
  
  start = datetime.datetime.now()

  # TODO go to MongoDB and perform query
  results = []
  
  end = datetime.datetime.now()
  delta = end - start

  return {
    "x-request" : {
      "arrivalDate"             : arrivalDate,
      "duration"                : duration,
      "paxCount"                : paxCount,
      "paxAges"                 : paxAges,
      "destination"             : destination,
      "productCategory"         : productCategory,
      "productType"             : productType,
      "brand"                   : brand,
      "name"                    : name,
      "reviewScore"             : reviewScore,
      "starRating"              : starRating,
      "board"                   : board,
      "budget"                  : budget,
      "accommodationType"       : accommodationType,
      "accommodationFacilities" : accommodationFacilities
    } ,
    "results" : results,
    "x-elapsed-us" : int(delta.total_seconds() * 1000000)
  }
