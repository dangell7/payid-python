# PayID Python library

[![CircleCI](https://circleci.com/bb/Harpangell/payid-python/tree/master.svg?style=svg&circle-token=3e47a0118e8b37d59b9dae0d884468d3f8f94c99)](https://circleci.com/bb/Harpangell/payid-python/tree/master)

## Installation

```bash
pip install git+https://github.com/dangell7/payid-python.git@master
```

To install from source, run

```bash
git clone https://github.com/dangell7/payid-python.git
cd payid
python setup.py install
```

## Documentation

Please see the [PayID API Documentation](https://docs.payid.org/) for the most up-to-date API documentation.

### Usage

This library has only been tested using Python 3.6.?.

Getting and interacting with accounts:

```python
import payid

payid.network = 'testnet' || 'mainnet'
payid.api_base = 'http://127.0.0.1' || 'https://example.com'
payid.api_version = '1.0'

client = payid.Public
private_client = payid.Private

payIDObject = client.get('alice', 'eth')
payId = payIDObject.payId
print(payId)
```

## Development

We use virtualenv. Install with `[sudo] pip install virtualenv`, initialize with `virtualenv venv`, and activate with `source venv/bin/activate`.

Install the development requirements with `pip install -r requirements/dev.txt`

### Testing

To run the test suite, run `py.test` from the project root.

### Linting

We enforce linting on the code with flake8. Run with `flake8 payid` from the project root.

### TODOs

- create method for Listings
