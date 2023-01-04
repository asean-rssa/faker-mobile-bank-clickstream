# Mobile Banking Clickstream Faker Provider for Python

  * [Purpose](#purpose)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Features](#features)

## Purpose

This is a custom `Faker` provider for Python that generates clickstream session data from a mobile banking app. 

## Installation

The Clickstream Faker Provider for Python is available to install from PyPi using `pip`.

```bash
pip install faker_mobile_bank_clickstream
```

## Usage

Sample code of Clickstream Provider usage.

```python
from faker import Faker
from faker_mobile_bank_clickstream import ClickstreamProvider

fake = Faker()
fake.add_provider(ClickstreamProvider)
fake.session_clickstream()

# or...
fake.session_clickstream(rand_session_max_size=50)  # random number of events from 1 to 50
```

The `session_clickstream()` method returns an array of JSON objects that represents a unique web session. By default, is
configured to return a random number of session events from the range of 1 through 25.

An example response object is the below:

```json
[
  {
    "ip": "85.59.39.221",
    "user_id": 777198,
    "user_agent": "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/11D257 Safari/9537.53",
    "session_id": "d5cba274f7724780d1ed2b60650101892260748df21b0e2fb8b2b2fd88cedf23",
    "event_time": "28/03/2022 23:09:48.360212",
    "event_name": "Login"
  },
  {
    "ip": "85.59.39.221",
    "user_id": 777198,
    "user_agent": "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/11D257 Safari/9537.53",
    "session_id": "d5cba274f7724780d1ed2b60650101892260748df21b0e2fb8b2b2fd88cedf23",
    "event_time": "28/03/2022 23:14:13.360227",
    "event_name": "SelectTransfer"
  },
  {
    "ip": "85.59.39.221",
    "user_id": 777198,
    "user_agent": "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/11D257 Safari/9537.53",
    "session_id": "d5cba274f7724780d1ed2b60650101892260748df21b0e2fb8b2b2fd88cedf23",
    "event_time": "28/03/2022 23:17:49.360241",
    "event_name": "FillTransferDetails"
  },
  {
    "ip": "85.59.39.221",
    "user_id": 777198,
    "user_agent": "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/11D257 Safari/9537.53",
    "session_id": "d5cba274f7724780d1ed2b60650101892260748df21b0e2fb8b2b2fd88cedf23",
    "event_time": "28/03/2022 23:22:15.360252",
    "event_name": "CompleteTransfer"
  }
]
```

## Features

Each user session includes some static data that are randomly calculated only once, such as the `ip`, `user_agent`, etc.

The events that are available on this clickstream are the following ones, and an event dependency has been configured to
provide a more real representation of a web session flow:

- `Login`
- `Logout`
- `ViewHome`
- `ViewAccounts`
- `ViewProducts`
- `SelectTransfer`
- `ViewTransactions`
- `ViewCreditCard`
- `ViewLoan`
- `ApplyCreditCard`
- `ApplyLoan`
- `FillCreditCardApplication`
- `FillLoanApplication`
- `SubmitCreditCardApplication`
- `SubmitLoanApplication`
- `FillTransferDetails`
- `CompleteTransfer`
