from unittest.mock import patch

from src.external_api import amount_transition

@patch('requests.request')
def test_amount_transition(mock_result):
    mock_result.return_value.json.return_value = {'result':1}
    assert amount_transition({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }) == 1
    mock_result.assert_called_once_with('GET', 'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37', headers={'apikey': 'NcqIdbPWRu5M95K6KMvNREvoqw7sXn25'}, data={})
