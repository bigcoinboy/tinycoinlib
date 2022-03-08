# TinyCoinLib (pre-release, v0.0.1)

A minimalistic any coin (Bitcoin, Litecoin, Dogecoin..)
RPC client and utilities for Python 3.

- Tiny
- Readable code base
- Free and open software (GPLv3)
- No external dependencies
- No API breaking changes in horizon

With it, your Python programs can interface with a Core Wallet.

- A JSON-RPC client ([```TinyCoinTalk``` @ talk.py](
https://github.com/bigcoinboy/tinycoinlib/tree/main/src/tinycoinlib/talk.py))

In addition, simple APIs to easily

- Accept coin payments
([```TinyCoinReceive``` @ receive.py](
https://github.com/bigcoinboy/tinycoinlib/tree/main/src/tinycoinlib/receive.py))
- Make coin payments
([```TinyCoinSend``` @ send.py](
https://github.com/bigcoinboy/tinycoinlib/tree/main/src/tinycoinlib/send.py))


**Warning!** TinyCoinLib comes without any warranty.
Improper use or software bugs can lead to loss of coins.
Run only on trusted platforms.
Proceed at your own risk.

**Warning!** TinyCoinLib is in early development and not
production ready yet. Its features remain mainly untested.
This will change in future revisions.

**Warning!** Pre-release versions (v.0.0.Z) are completely
untested. Functionality is likely broken.


## 💿 Installing

First, install TinyCoinLib form the Python Package Index

```
pip install tinycoinlib
```

Next, download the Core Wallet
from **a trusted source** and verify its integrity
(checksums *and* signature).
Start the bundled coind program
(bitcoind, litecoind, dogecoind, ...) and
wait for the blockchain to synchronise.

Then you are ready to go.


## 📚 Examples

### 1) General RPC commands

```python
from tinycoinlib.talk import TinyCoinTalk

talker = TinyCoinTalk('litecoin')
response = talker.call('getblockhash 69')
```

The constructor takes a URL as its first parameter.
It points to the {}coind RPC server or
is a special value listed in
the ```PRESET_PORTS``` dictionary.

The ```call``` method takes in a command and returns
the server's response.

### 2) Accept payments (receive coins)



```python
from tinycoinlib.receive import TinyCoinReceive

receiver = TinyCoinReceive('127.0.0.1:18933')
trans_id = 'my-transaction-id'

paymend_address = receiver.get_payment_address(trans_id)
is_complete, amount = receiver.payment_completed(trans_id, 42)
```

The ```get_payment_address``` method adds (if not already existing)
a receive address with the label *my-transaction-id*
to the Core wallet. The ```payment_completed``` method checks
if the payment has been completed (42 or more coins in the address).

### 3) Make payments (send coins)

```python
from tinycoinlib.send import TinyCoinSend

sender = TinyCoinSend('dogecoin')

transaction_id = sender.send(1.38, 'DMrzmskQzXJ9pDHQBxBu5de36UaH5EYtDa')
```

```TinyCoinSend``` has two more methods, ```get_balance```
and ```get_details``` for wallet balance and
transaction details (confirmations, fee, ...) enquery, respectively.



## Contributing

For bugs and ideas, please see our [Issues](https://github.com/bigcoinboy/tinycoinlib/issues).
Further details are in
[CONTRIBUTING.md](https://github.com/bigcoinboy/tinycoinlib/blob/main/CONTRIBUTING.md).



## ☕Supporting the project

Financial support is highly appreciated as it allows me (**BigCoinBoy**)
to work on this project

- Bitcoin: ```bc1qp4xyynjqzfffxjsq8xucd7jfjs58sm0reunm9d``` |
[URI](bitcoin:BC1QP4XYYNJQZFFFXJSQ8XUCD7JFJS58SM0REUNM9D?label=Donation%20for%20TinyCoinLib&message=Thank%20you%20for%20supporting%20TinyCoinLib%21%20Your%20action%20is%20highly%20appreciated.%20Yours%2C%20-%20BigCoinBoy) |
[QR-code](https://github.com/bigcoinboy/tinycoinlib/blob/main/support_files/bitcoin-qr.png) |
[History](https://bitcoinblockexplorers.com/address/bc1qp4xyynjqzfffxjsq8xucd7jfjs58sm0reunm9d)
- Litecoin: ```ltc1quaqg6kfragqcfg3z4w2jlupsf4dcf4e59gujcg``` |
[URI](litecoin:ltc1quaqg6kfragqcfg3z4w2jlupsf4dcf4e59gujcg?label=Donation%20for%20TinyCoinLib&message=Thank%20you%20for%20supporting%20TinyCoinLib%21%20Your%20action%20is%20highly%20appreciated.%20Yours%2C%20-%20BigCoinBoy) |
[QR-code](https://github.com/bigcoinboy/tinycoinlib/blob/main/support_files/litecoin-qr.png) |
[History](https://litecoinblockexplorer.net/address/ltc1quaqg6kfragqcfg3z4w2jlupsf4dcf4e59gujcg)
- Dogecoin: ```DMrzmskQzXJ9pDHQBxBu5de36UaH5EYtDa``` |
[URI](dogecoin:DMrzmskQzXJ9pDHQBxBu5de36UaH5EYtDa?label=Donation%20for%20TinyCoinLib&message=Thank%20you%20for%20supporting%20TinyCoinLib%21%20Your%20action%20is%20highly%20appreciated.%20Yours%2C%20-%20BigCoinBoy) |
[QR-code](https://github.com/bigcoinboy/tinycoinlib/blob/main/support_files/dogecoin-qr.png) |
[History](https://dogeblocks.com/address/DMrzmskQzXJ9pDHQBxBu5de36UaH5EYtDa)

Thank you to everyone who has donated!

