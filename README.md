# Cattails MMJ Python library

[![CircleCI](https://circleci.com/bb/Harpangell/mmj-python/tree/master.svg?style=svg&circle-token=3e47a0118e8b37d59b9dae0d884468d3f8f94c99)](https://circleci.com/bb/Harpangell/mmj-python/tree/master)

## Installation

```bash
pip install git+git://bitbucket.org/Harpangell/mmj-python.git@master
```

To install from source, run

```bash
git clone https://Harpangell@bitbucket.org/Harpangell/mmj-python.git
cd mmj
python setup.py install
```

## Documentation

Please see the [MMJ API Documentation](https://api-co.mmj.com/Documentation/#getting-started) for the most up-to-date API documentation.

### Usage

This library has only been tested using Python 3.6.?.

Getting and interacting with locations:

```python
import mmj

mmj.api_key = 'xxx'

facilities = mmj.Facility.all()
facilities = facilities[0]

# print facilities.employees
# print facilities.harvests
# print facilities.labtests
# print facilities.items
# print facilities.packages
# print facilities.patients
# print facilities.plantbatches
# print facilities.plants
# print facilities.rooms
# print facilities.sales
# print facilities.strains
# print facilities.transfers
# print facilities.unitsofmeasures
```

Properties are cached on each model instance. To refresh, do `facility = Facility.get(facility.LicenseNumber)`. (TODO: allow properties to be refreshed manually)

Objects embedded in API responses are added as properties on each model instance. To refresh, do `facilities.refresh()`.

Interacting with sales:

```python

new_transactions = [
  {
    packageLabel = 'ABCDEF012345670000010331',
    quantity = 1.0,
    unitOfMeasure = 'Ounces',
    totalAmount = 9.99,
  },
  {
    packageLabel = 'ABCDEF012345670000010332',
    quantity = 1.0,
    unitOfMeasure = ,
    totalAmount = 9.99,
  }
]

sales_date_time = datatime.utcnow()
sales_customer_type = 'Consumer'
patient_license_number = None
caregiver_license_number = None
identification_method = None
transactions = new_transactions

sales_receipt = facility.create_sales_receipt(
    sales_date_time,
    sales_customer_type,
    patient_license_number,
    identification_method,
    transactions,
)
print sales_receipt
# sales_receipt.void()
```

## Development

We use virtualenv. Install with `[sudo] pip install virtualenv`, initialize with `virtualenv venv`, and activate with `source venv/bin/activate`.

Install the development requirements with `pip install -r requirements/dev.txt`

### Testing

To run the test suite, run `py.test` from the project root.

### Linting

We enforce linting on the code with flake8. Run with `flake8 mmj` from the project root.

### TODOs

- create method for Sales
- create method for Employees
- create method for Harvests
- create method for Lab Tests
- create method for Patients
- create method for Plant Batches
- create method for Plants
- create method for Rooms
- create method for Strains
- create method for Transfers
- create method for Units of Measures
