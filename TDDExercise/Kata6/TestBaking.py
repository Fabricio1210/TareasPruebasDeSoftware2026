from unittest import mock
import unittest
from datetime import datetime
from faker import Faker
import Baking
from Baking import Account, main

class TestAccount(unittest.TestCase):

  def setUp(self):
    self.fake = Faker()

  def test_init(self):
    testAccount = Account()
    self.assertEqual(testAccount.balance, 0)
    self.assertEqual(testAccount.history, [])

  def test_deposit(self):
    amount = self.fake.random_int(min=100, max=5000)
    account = Account()
    account.deposit(amount)

    self.assertEqual(account.balance, amount)
    self.assertEqual(len(account.history), 1)
    self.assertEqual(account.history[0]['amount'], amount)
    self.assertEqual(account.history[0]['balance'], amount)

  def test_withdraw(self):
    amount = self.fake.random_int(min=100, max=5000)
    withdraw_amount = self.fake.random_int(min=1, max=amount)
    account = Account()
    account.deposit(amount)
    account.withdraw(withdraw_amount)

    self.assertEqual(account.balance, amount - withdraw_amount)
    self.assertEqual(len(account.history), 2)
    self.assertEqual(account.history[1]['amount'], -withdraw_amount)
    self.assertEqual(account.history[1]['balance'], amount - withdraw_amount)

  def test_withdraw_not_enough_balance(self):
    account = Account()

    with mock.patch('builtins.print') as mock_print:
      account.withdraw(100)

    mock_print.assert_called_once_with('No tienes ese dinero compa')
    self.assertEqual(account.balance, 0)
    self.assertEqual(account.history, [])

  def test_print_statement(self):
    account = Account()

    with mock.patch.object(Baking, 'datetime') as mock_datetime:
      mock_datetime.now.side_effect = [
        datetime(2026, 4, 14),
        datetime(2026, 4, 15),
      ]
      account.deposit(500)
      account.withdraw(100)

    with mock.patch('builtins.print') as mock_print:
      account.printStatement()

    mock_print.assert_has_calls([
      mock.call('DATE         | AMOUNT     | BALANCE   '),
      mock.call('15/04/2026   | -100       | 400       '),
      mock.call('14/04/2026   | 500        | 500       '),
    ])

  def test_main(self):
    with mock.patch.object(Baking, 'Account') as mock_account_class:
      mock_account_instance = mock_account_class.return_value

      main()

    mock_account_class.assert_called_once_with()
    mock_account_instance.deposit.assert_called_once_with(500)
    mock_account_instance.withdraw.assert_called_once_with(100)
    mock_account_instance.printStatement.assert_called_once_with()

