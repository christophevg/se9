# se9

> proof of concept of a simple product search engine started in an agile way

## Prerequisites

- mongoDB
- Python 3

```bash
$ git clone https://github.com/christophevg/se9
$ cd iv8
$ virtualenv -p python3 venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
```

## Minimal Survival Commands

You can run an interactive web-based application from the checked out repository:

```bash
(venv) $ gunicorn se9:server
```

... and visit [http://localhost:8000](http://localhost:8000)
... and play with the Swagger UI ;-)

> Pro-Tip: there is also a top-level `Makefile`, allowing for a simple `make` command, generating and loading the environment all-in-one-go for you.

Or alternatively, you can deploy it to [Heroku](https://heroku.com) and play with it over there. 

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

