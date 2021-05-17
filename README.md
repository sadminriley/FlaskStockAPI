# Stock Quote API

I've also wrote a tutorial below on deploying a very similar Flask app to EKS on AWS.

# How run and deploy a Flask API to AWS EKS

https://fasterdevops.github.io/flask-docker-eks/


## Financial Modeling Prep
This utilizes the free API found on https://financialmodelingprep.com/

Save your API key in the .key file before running

## Building the application
```
docker build -t stockapi:latest .
```

## Running the application
```
docker run -t -p 5000:5000 stockapi
```

## Usage

### Quote [GET]

request
```
curl -X GET http://localhost:5000/quote/AAPL
```

result
```
[
  {
    "price": 55.39,
    "symbol": "L",
    "volume": 355712
  }
]

```

### Profile

request
```
curl -X GET localhost:5000/profile/TSLA
```

result
```
[
  {
    "address": "3500 Deer Creek Rd",
    "beta": 2.010479,
    "ceo": "Mr. Elon Musk",
    "changes": -10.34,
    "cik": "0001318605",
    "city": "Palo Alto",
    "companyName": "Tesla Inc",
    "country": "US",
    "currency": "USD",
    "cusip": "88160R101",
    "dcf": 458.052,
    "dcfDiff": 12772.3,
    "defaultImage": false,
    "description": "Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems in the United States, China, Netherlands, Norway, and internationally. The company operates in two segments, Automotive; and Energy Generation and Storage. The Automotive segment offers sedans and sport utility vehicles. It also provides electric powertrain components and systems; and services for electric vehicles through its company-owned service locations, and Tesla mobile service technicians, as well as sells used vehicles. This segment markets and sells its products through a network of company-owned stores and galleries, as well as through its own Website. The Energy Generation and Storage segment offers energy storage products, such as rechargeable lithium-ion battery systems for use in homes, industrial, commercial facilities, and utility grids; and designs, manufactures, installs, maintains, leases, and sells solar energy generation and energy storage products to residential and commercial customers. It also provides vehicle insurance services, as well as renewable energy. The company was formerly known as Tesla Motors, Inc. and changed its name to Tesla, Inc. in February 2017. Tesla, Inc. was founded in 2003 and is headquartered in Palo Alto, California.",
    "exchange": "Nasdaq Global Select",
    "exchangeShortName": "NASDAQ",
    "fullTimeEmployees": "70757",
    "image": "https://financialmodelingprep.com/image-stock/TSLA.png",
    "industry": "Auto Manufacturers",
    "ipoDate": "2010-06-29",
    "isActivelyTrading": true,
    "isEtf": false,
    "isin": "US88160R1014",
    "lastDiv": 0.0,
    "mktCap": 666522681344,
    "phone": "16506815000",
    "price": 694.4,
    "range": "136.608-900.4",
    "sector": "Consumer Cyclical",
    "state": "CALIFORNIA",
    "symbol": "TSLA",
    "volAvg": 34197081,
    "website": "https://www.tesla.com/",
    "zip": "94304"
  }
]
```

### Executives - get key company executives

request
```
curl -X GET localhost:5000/executives/AAPL
```

result
```
{
    "currencyPay": "USD",
    "gender": "male",
    "name": "Mr. Greg  Joswiak",
    "pay": null,
    "title": "Senior Vice President of Worldwide Marketing",
    "titleSince": null,
    "yearBorn": null
  },
  {
    "currencyPay": "USD",
    "gender": "female",
    "name": "Ms. Nancy  Paxton",
    "pay": null,
    "title": "Senior Director of Investor Relations & Treasury",
    "titleSince": null,
    "yearBorn": null
  },
  {
    "currencyPay": "USD",
    "gender": "female",
    "name": "Ms. Mary  Demby",
    "pay": null,
    "title": "Chief Information Officer",
    "titleSince": null,
    "yearBorn": null
  },
  {
    "currencyPay": "USD",
    "gender": "male",
    "name": "Mr. James  Wilson",
    "pay": null,
    "title": "Chief Technology Officer",
    "titleSince": null,
    "yearBorn": null
  },
  {
    "currencyPay": "USD",
    "gender": "male",
    "name": "Mr. Chris  Kondo",
    "pay": null,
    "title": "Senior Director of Corporation Accounting",
    "titleSince": null,
    "yearBorn": null
  },
  {
    "currencyPay": "USD",
    "gender": "female",
    "name": "Ms. Deirdre  O'Brien",
    "pay": 4610000,
    "title": "Senior Vice President of People & Retail",
    "titleSince": null,
    "yearBorn": 1967
  },
  {
    "currencyPay": "USD",
    "gender": "female",
    "name": "Ms. Katherine L. Adams",
    "pay": 4590000,
    "title": "Senior Vice President, Gen. Counsel & Sec.",
    "titleSince": null,
    "yearBorn": 1964
  },
  {
    "currencyPay": "USD",
    "gender": "male",
    "name": "Mr. Jeffrey E. Williams",
    "pay": 4590000,
    "title": "Chief Operating Officer",
    "titleSince": null,
    "yearBorn": 1964
  },
  {
    "currencyPay": "USD",
    "gender": "male",
    "name": "Mr. Luca  Maestri",
    "pay": 4600000,
    "title": "Chief Financial Officer & Senior Vice President",
    "titleSince": null,
    "yearBorn": 1964
  },
  {
    "currencyPay": "USD",
    "gender": "male",
    "name": "Mr. Timothy D. Cook",
    "pay": 14770000,
    "title": "Chief Executive Officer & Director",
    "titleSince": null,
    "yearBorn": 1961
  }
]
```

