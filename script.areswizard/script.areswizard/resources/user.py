exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MmYgMjMsIDgyLCAxMGIsIDEzLCBkYiwgNTYKMmYgYyxkZCwgZTMsIGQ4CjJmIGUwLCBmOSwgNGIsIGRiLmMwCmMxIDIzIDJmIDViIGE1IGJhCjJmIDIxLCBkNgpjMSBiNSAyZiBkMAoyZiAxNwoKCjk2PSAnZDcuMjQnCjE1ID0gODIuZWIoOTYpCjhmID0gMjMuNWIoMTUuYTEoJ2QzJykpCjFkID0gZGIuYzAuZmMoOGYsICdiZicpCgoKZDUgMWMKMWMgPSAnMzEuMTA3JwoyNSA9ICJkZiIKCmQ1IGI0CmI0ID0gMTMuMWEoM2UoNTYuNDNbMV0pLCAnYjQnKQoKZDUgMTgKMTggPSAxMy4xYSgzZSg1Ni40M1sxXSksICcxOCcpCmQ1IDFmCjFmID0gMTMuMWEoM2UoNTYuNDNbMV0pLCAnMWYnKQpkNSBiCmIgPSAxMy4xYSgzZSg1Ni40M1sxXSksICdiJykKZDUgNTIKNTIgPSAxMy4xYSgzZSg1Ni40M1sxXSksICc1MicpCgoKCgoKCgoKCjU4IGRjKDIxKToKCQoJNzUgPSAxMGIuMTE0KCkKCTc1LjM0KCIyMSIsIDIxLCAiIiwiIikKCQoKNTggNyg4OCwgM2QsIDUzLCA4NT1jNik6CgkyZCA4NToKCSAgIGI4OiBjZSA9IGUzLmEyKCIoPzExMikiICsgM2QgKyAiKFtcY2JcMTBmXSs/KSIgKyA1MywgODgpLmIwKDEpCgkgICA3ZTogY2UgPSAnJwoJNmI6CgkgICBiODogY2UgPSBlMy5hMigiKD8xMTIpKCIgKyAzZCArICJbXGNiXDEwZl0rPyIgKyA1MyArICIpIiwgODgpLmIwKDEpCgkgICA3ZTogY2UgPSAnJwoJOWYgY2UKCgo1OCA5NygyMSk6CgoJOGMgPSAiZWEiCgkyZCA4YyAxMTMgMjE6CgkJOWIgPSAyMS45MygnXScpCgkJNTcgPSAyMVs5YisxOl0KCQk5MCA9IDU3LjkzKCdbJykKCQkyMSA9IDU3Wzo5MF0KCQk5ZiAyMQoKCQkKNTggOTEoMjIsIGNhKToKCgk3YigpCgoJCQkKCQkKCWUgPSAyMy40MCgiIiwgIjQ1IDc5IDhiIDE4IGNkIikKCWUuNGQoKQoJMjkgPSBlLjRjKCkKCQoJZSA9IDIzLjQwKCIiLCAiNDUgNzkgYSAyYyAxMGQgOGQgYWEgKDEwMSBiZSBkYSBlZiBhIGI0KSIpCgllLjRkKCkKCTI2ID0gZS40YygpCgkKCWUgPSAyMy40MCgiIiwgIjQ1IDc5IDhiIDE5IikKCWUuOWQoYzYpCgllLjRkKCkKCTI4ID0gZS40YygpCgkKCQoJCgkKCQoJIyAxYiA9IHsnY2EnOiBjYX0KCQoJIyA2MSA3MSgxZCwgJzEwNCcpIGE1IGY6CgkJIyA0Yi5hMygxYiwgZikKCQoJIyBmLjVjCgkKCQoJMTUuNigiY2EiLCBjYSkKCTE1LjYoImI0IiwgMjYpCgkjIDE1LjYoIjE4IiwgMjkpCgkKCgkKCQkKCWQgPSAnNjY6Ly8yNC5iMy5hYi8nKzFjKyc/NDg9OTEmNzY9JysyNisnJmYzPScrMjgrJyYxOD0nKzI5KycmY2E9JytjYSsnJjc0PScrNzQrJyY2Zj0nKzZmKycmNTA9Jys1MCArICcmMjI9JyArIDIyICsgJyY3OD0nICsgMTcuMTcuODMoKS4zMCgnJWNiJykKCQoJM2YgPSBkLjRmICgiICIsICIlMjAiKQoJCgkyZCBiID09ICIyZSI6CgkJMTIgJ0AzMTogNjkgZDogJyArIDM2KDNmKQoJCgkKCWM3ID0gYy4yYSgzZikKCWM3LjFlKCc0ZS0zYicsIDI1KQoJOCA9IGMuMmIoYzcpCgkxMDggPSA4LjRhKCkKCgkJCgkyZCBiID09ICIyZSI6CgkJMTIgJ0AzMTogNjkgNjc6ICcgKyAzNigxMDgpCgkKCSMgNjEgNzEoMWQsICdjZScsMCkgYTUgZjoKCQkjIDFiID0gNGIuYzQoZikKCgkjIGNhID0gMWJbJ2NhJ10KCSMjIGI0ID0gMWJbJ2I0J10KCSMjIDE5ID0gMWJbJzE5J10KCSMjIDE4ID0gMWJbJzE4J10KCgkKCQoJMTAgPSAiMTAiCgk2NCA9IDEwOC45MygxMCkKCQoJMmQgNjQgPD4gLTE6CgkJCgkJMmMgPSA3KDEwOCwgJzEwOicsICcvJykKCQk2MyA9IDcoMTA4LCAnISEnLCAnISEnKQoJCQoJCQoJCTc1ID0gMTBiLjExNCgpCgkJNzUuMzQoImIyIGM5IiwgIjczIGZhIGZiIGZmIGQ0IisyYywgIiIsIiIpCgkJMTUuNigiMWYiLCAiYWQiKQoJCQoJCQoJCQoJCTFiID0geydjYSc6IGNhLCAnMTgnOiAnMTAnfQoJCgkJNjEgNzEoMWQsICcxMDQnKSBhNSBmOgoJCQk0Yi5hMygxYiwgZikKCQkKCQlmLjVjCgkJCgkJCgkJMTUuNigiY2EiLCBjYSkKCQkxNS42KCJiNCIsIDI2KQoJCSMgMTUuNigiMTkiLCA2MykKCQkjIDE1LjYoIjE4IiwgIjEwIikKCQkKCQkKCQk5ZiAoMTApCgkKCQoJCgkyZCAxMDggPT0gImI3IjoKCQoJCgkJMTUuNigiMWYiLCAiN2QiKQoJCTE1LjYoImI0IiwgMjYpCgkJIyAxNS42KCIxOSIsIDI4KQoJCSMgMTUuNigiMTgiLCAyOSkKCQoJCTc1ID0gMTBiLjExNCgpCgkJNzUuMzQoIjQ1IGIxIDhiIDE4IiwgImE4IDE4IDU1IGVkIDYxIDExNSA3YyAxMTYuICgxMGUgMTAyIGZlIGEgZTEgMTEwIGQxIGYyIGVlIGNjLi4gMTA2JzExOCBlMiBmMiBiMSBmMCBlNCAxMDMpIiwgIiIsIiIpCgkJCgkJODkgPSB7J2I0JzogMjYsICcxOSc6IDI4LCAnMTgnOiAyOX0KCQkKCQk3NyA9IDRiLmU2KDg5KQoJCQoJCQoJCTlmICg3NykKCQkKCQkKCQkKCTJkIDEwOCA9PSAiODciOgoJCgkJCgkJCgkJMWIgPSB7J2NhJzogY2F9CgkKCQk2MSA3MSgxZCwgJzEwNCcpIGE1IGY6CgkJCTRiLmEzKDFiLCBmKQoJCQoJCWYuNWMKCQkKCQkKCQkxNS42KCJjYSIsIGNhKQoJCTE1LjYoImI0IiwgIiIpCgkJIyAxNS42KCIxOCIsICIiKQoJCQoJCQoJCTc1ID0gMTBiLjExNCgpCgkJNzUuMzQoIjdmIDE5IiwgIjdmIDE5IiwgIiIsIiIpCgkJCgkJCgkJOWYgKDEwOCkJCgkJCgkJCQoJNmI6CgkJCgkJNzUgPSAxMGIuMTE0KCkKCQk3NS4zNCgiNWYsIDVlIDU1IGEgMzgiLCAiYTggNWQgMzI6IFxjOFxjOCAiICsgMTA4LCAiIiwiIikKCQkyZCBiID09ICIyZSI6CgkJCTEyICdAMzE6IGQ6ICcgKyAzNigzZikKCQkKCQk5ZiAoMTA4KQoJCQoJCQoKCQkKNTggNDEoYjQsIDIyLCBjYSk6CgoKCgllID0gMjMuNDAoIiIsICI0NSA3OSA4YiA3YyAxMTYgKDEwYSBjMykiKQoJZS40ZCgpCgk0NCA9IGUuNGMoKQoJCgk2MSA3MSgxZCwgJ2NlJywwKSBhNSBmOgoJCTFiID0gNGIuYzQoZikKCgljYSA9IDFiWydjYSddCgkKCSMgYjQgPSAxMy4xYSgzZSg1Ni40M1sxXSksICdiNCcpCgkjIDE5ID0gMTMuMWEoM2UoNTYuNDNbMV0pLCAnMTknKQoJIyAxOCA9IDEzLjFhKDNlKDU2LjQzWzFdKSwgJzE4JykKCgoJCglkID0gJzY2Oi8vMjQuYjMuYWIvJysxYysnPzQ4PTQxJjc2PScrYjQrJyYyMj0nKzIyKycmY2E9JytjYSsnJjllPScrNDQgKyAnJjc4PScgKyAxNy4xNy44MygpLjMwKCclY2InKQoJCgkyZCBiID09ICIyZSI6CgkJMTIgJ0AzMTogNDEgZCA9ICcgKyAzNihkKQoJCgljNyA9IGMuMmEoZCkKCWM3LjFlKCc0ZS0zYicsIDI1KQoJOCA9IGMuMmIoYzcpCgkxMDggPSA4LjRhKCkKCQoJCgkyZCAxMDggPT0gImI2IjoKCQoJCTc1ID0gMTBiLjExNCgpCgkJNzUuMzQoIjZhIiwgIjczIGFhIGZiIDgzIGFmLi4gZjUgMTA5IGU5Li4iLCAiIiwiIikKCQkKCQk5ZiAoMTA4KQoJCQoJNmI6CgkJCgkJNzUgPSAxMGIuMTE0KCkKCQk3NS4zNCgiNWYsIDVlIDU1IGEgMzgiLCAiYTggNWQgMzIiLCAiIiwiIikKCQkKCQkKCQkyZCBiID09ICIyZSI6CgkJCTEyICdAMzE6IDQxIDggPSAnICsgMzYoMTA4KQoJCQkxMiAnQDMxOiBkOiAnICsgMzYoZCkKCQkKCQkKCQk5ZiAoMTA4KQoJCQoJCgkKCQo1OCA4MShiNCwgMmMsIDIyLCBjYSk6CgoKCTE0ID0gWyIxIiwiMiIsIjMiLCI0IiwiNSJdCgkKCTE2ID0gMTBiLjExNCgpLjgwKCJiYiBhOSA5NT8iLCAxNCkKCQoJIyA3NSA9IDEwYi4xMTQoKQoJIyA3NS4zNCgiNjciLCAxNFsxNl0sICIiLCIiKQoJCgkKCTI3ID0gM2UoMTRbMTZdKQoJCgkKCWQgPSAnNjY6Ly8yNC5iMy5hYi8nKzFjKyc/NDg9ODEmNzY9JytiNCsnJjIyPScrMjIrJyYyYz0nKzJjKycmY2E9JytjYSsnJjI3PScrMzYoMjcpICsgJyY3OD0nICsgMTcuMTcuODMoKS4zMCgnJWNiJykKCQoJMmQgYiA9PSAiMmUiOgoJCTEyICdANTkgLS0+JwoJCTEyICcgJwoJCTEyIGQKCQoJZCA9IGQuNGYgKCIgIiwgIiUyMCIpCgkKCTJkIGIgPT0gIjJlIjoKCQkxMiAnQDU5IC0tPicKCQkxMiAnICcKCQkxMiBkCgkKCSMxMiBkCgkKCWM3ID0gYy4yYShkKQoJYzcuMWUoJzRlLTNiJywgMjUpCgk4ID0gYy4yYihjNykKCWI5ID0gOC40YSgpCgkKCTJkIGIgPT0gIjJlIjoKCQkxMiAnQDhlIC0tPicKCQkxMiAnICcKCQkxMiBiOQoJCgoJMmQgYjkgPT0gIjYwIjoKCgkJNzUgPSAxMGIuMTE0KCkKCQk3NS4zNCgiNmEiLCAiNzMgMTQgNTUgNjUiLCAiIiwiIikKCQkKCQk5ZgoJCQoJCgkyZCBiOSA9PSAiNTQiOgoKCQk3NSA9IDEwYi4xMTQoKQoJCTc1LjM0KCI2YyA0NiIsICJiYyA2ZSA0NiA4ZCAxNSIsICIiLCIiKQoJCQoJCTlmCgkJCgk2YjoKCQkKCQk3NSA9IDEwYi4xMTQoKQoJCTc1LjM0KCI1ZiwgNWUgNTUgYSAzOCIsICJhOCA1ZCAzMjogXGM4XGM4IC0iICsgYjksICIiLCIiKQoJCTJkIGIgPT0gIjJlIjoKCQkJMTIgJ0AzMTogZDogJyArIDM2KGQpCgkJCgkJOWYKCQoJCgoJCgkKNTggODQoYjQsIDJjLCAyMiwgY2EpOgoKCgkJCgkKCTE0ID0gWyIxIiwiMiIsIjMiLCI0IiwiNSJdCgkKCTE2ID0gMTBiLjExNCgpLjgwKCJiYiBhOSA5NT8iLCAxNCkKCQoJIyA3NSA9IDEwYi4xMTQoKQoJIyA3NS4zNCgiNjciLCAxNFsxNl0sICIiLCIiKQoJCgkKCTI3ID0gM2UoMTRbMTZdKQoJCgkKCWQgPSAnNjY6Ly8yNC5iMy5hYi8nKzFjKyc/NDg9ODQmNzY9JytiNCsnJjIyPScrMjIrJyYyYz0nKzJjKycmY2E9JytjYSsnJjI3PScrMzYoMjcpICsgJyY3OD0nICsgMTcuMTcuODMoKS4zMCgnJWNiJykKCQoJZCA9IGQuNGYgKCIgIiwgIiUyMCIpCgkJCgoJCgljNyA9IGMuMmEoZCkKCWM3LjFlKCc0ZS0zYicsIDI1KQoJOCA9IGMuMmIoYzcpCgliOSA9IDguNGEoKQoJCgoJMmQgYjkgPT0gIjYwIjoKCgkJNzUgPSAxMGIuMTE0KCkKCQk3NS4zNCgiNmEiLCAiNzMgMTQgNTUgNjUiLCAiIiwiIikKCQkKCQk5ZgoJCQoJCgkyZCBiOSA9PSAiNTQiOgoKCQk3NSA9IDEwYi4xMTQoKQoJCTc1LjM0KCI2YyA0NiIsICJiYyA2ZSA0NiA4ZCBlYyIsICIiLCIiKQoJCQoJCTlmCgkJCgk2YjoKCQkKCQk3NSA9IDEwYi4xMTQoKQoJCTc1LjM0KCI1ZiwgNWUgNTUgYSAzOCIsICJhOCA1ZCAzMjogXGM4XGM4IC0iICsgYjksICIiLCIiKQoJCTJkIGIgPT0gIjJlIjoKCQkJMTIgJ0AzMTogZDogJyArIDM2KGQpCgkJCgkJOWYKCQoJCQoKCgkKNTggOTIoYjQsIDJjLCAyMiwgY2EpOgoKCgoJCQoJCgkxNCA9IFsiMSIsIjIiLCIzIiwiNCIsIjUiXQoJCgkxNiA9IDEwYi4xMTQoKS44MCgiYmIgYTkgOTU/IiwgMTQpCgkKCSMgNzUgPSAxMGIuMTE0KCkKCSMgNzUuMzQoIjY3IiwgMTRbMTZdLCAiIiwiIikKCQoJCgkyNyA9IDNlKDE0WzE2XSkKCQoJCglkID0gJzY2Oi8vMjQuYjMuYWIvJysxYysnPzQ4PTkyJjc2PScrYjQrJyYyMj0nKzIyKycmMmM9JysyYysnJmNhPScrY2ErJyYyNz0nKzM2KDI3KSArICcmNzg9JyArIDE3LjE3LjgzKCkuMzAoJyVjYicpCgkKCWQgPSBkLjRmICgiICIsICIlMjAiKQoJCgljNyA9IGMuMmEoZCkKCWM3LjFlKCc0ZS0zYicsIDI1KQoJOCA9IGMuMmIoYzcpCgliOSA9IDguNGEoKQoJCgoJMmQgYjkgPT0gIjYwIjoKCgkJNzUgPSAxMGIuMTE0KCkKCQk3NS4zNCgiNmEiLCAiNzMgMTQgNTUgNjUiLCAiIiwiIikKCQkKCQk5ZgoJCQoJCgkyZCBiOSA9PSAiNTQiOgoKCQk3NSA9IDEwYi4xMTQoKQoJCTc1LjM0KCI2YyA0NiIsICJiYyA2ZSA0NiA4ZCBmNyIsICIiLCIiKQoJCQoJCTlmCgkJCgk2YjoKCQkKCQk3NSA9IDEwYi4xMTQoKQoJCTc1LjM0KCI1ZiwgNWUgNTUgYSAzOCIsICJhOCA1ZCAzMjogXGM4XGM4IC0iICsgYjksICIiLCIiKQoJCTJkIGIgPT0gIjJlIjoKCQkJMTIgJ0AzMTogZDogJyArIDM2KGQpCgkJCgkJOWYKCQoJCgkJCgoJCgkJCQo1OCA3YigpOgoJCglkNSA3NAoJZDUgNTAKCWQ1IDM5CglkNSA2ZgoJZDUgOTQKCWQ1IDQ3CglkNSAyMgoJZDUgM2MKCQoJYjg6CgkJZCA9ICc2NjovLzg2LmRlLycKCQljNyA9IGMuMmEoZCkKCQljNy4xZSgnNGUtM2InLCAnOTgvNS4wICg0OTsgMTExOyA0OSBmNiA1LjE7IGYxLWY4OyBmZDoxLjkuMC4zKSBhYy83MiA5YS8zLjAuMycpCgkJOCA9IGMuMmIoYzcpCgkJMzM9OC40YSgpCgkJOC41YygpCgkJCgkJZDUgNzQKCQk3NCA9IDcoMzMsICdmNDs4OC1hZTogMTAwOyI+JywgJzwvYT4nKQoJCWQ1IDUwCgkJNTAgPSA3KDMzLCAnYzI6PC9kOT48YTYgM2E9IjUxLWE3OmE0OyI+JywgJzwvYTY+JykKCQlkNSAzOQoJCTM5ID0gNygzMywgJzljOjwvZDk+PGE2IDNhPSI1MS1hNzphNDsiPicsICc8L2E2PicpCgkJZDUgNmYKCQk2ZiA9IDcoMzMsICcxMGM6PC9kOT48YTYgM2E9IjUxLWE3OmE0OyI+JywgJzwvYTY+JykKCTdlOgoJCTc0ID0gIiIKCgkKCQoJMmQgNzQgPT0gIiI6CgkJCgkJZCA9ICdlNzovLzEwNS42ZC5kZS9lOC9lNS1mZi03NC8nCgkJYzcgPSBjLjJhKGQpCgkJYzcuMWUoJzRlLTNiJywgJzk4LzUuMCAoNDk7IDExMTsgNDkgZjYgNS4xOyBmMS1mODsgZmQ6MS45LjAuMykgYWMvNzIgOWEvMy4wLjMnKQoJCTggPSBjLjJiKGM3KQoJCTMzPTguNGEoKQoJCTguNWMoKQoJCQoJCSNkNSA3NAoJCTc0ID0gNygzMywgJzExNyBjZjo8MzUgM2E9IjUxLTY4OjhhIj4gJywgJzwvMzU+JykKCQkjZDUgNTAKCQk1MCA9IDcoMzMsICdjMjwvMzU+OjwzNSAzYT0iNTEtNjg6OGEiPiAnLCAnPC8zNT4nKQoJCSNkNSAzOQoJCTM5ID0gNygzMywgJzljOjwzNSAzYT0iNTEtNjg6OGEiPiAnLCAnPC8zNT4nKQoJCSNkNSA2ZgoJCTZmID0gNygzMywgJ2JkIGQyIGM1OjwzNSAzYT0iNTEtNjg6OGEiPiAnLCAnPC8zNT4nKQoKCQkKCQkKCWQ1IDNjCQoJM2MgPSAyMy4xMSgnMzcuNjInKQoJCQoJN2EgM2MgPT0gImEwIjoKCQkzYyA9IDIzLjExKCczNy42MicpCQoJCQoJCglkNSA5NAkKCTk0ID0gMjMuMTEoJzM3LjQyJykKCQoJN2EgOTQgPT0gImEwIjoKCQk5NCA9IDIzLjExKCczNy40MicpCgkJCgkKCWQ1IDQ3CQoJNDcgPSAyMy4xMSgnMzcuNWEnKQoJCQkKCTdhIDQ3ID09ICJhMCI6CgkJNDcgPSAyMy4xMSgnMzcuNWEnKQoJCQoJCglkNSAyMgoJMjIgPSAyMy4xMSgnOTkuNzAnKQoJCQkKCTdhIDIyLjkzKCc6JykgPT0gLTE6CgkJMjIgPSAyMy4xMSgnOTkuNzAnKQ==")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|2|3|4|5|setSetting|regex_from_to|response|9|a|debuglog|urllib2|url|keyboard|f|staff_override|getInfoLabel|print|xbmcplugin|rating|addon|userChoice|datetime|email|password|getSetting|config|basephpfile|settingsfile|add_header|accountstatus|20|string|mac|xbmc|areswizard|aresagent|nameinput|points|passwordinput|emailinput|Request|urlopen|name|if|true|import|strftime|ares|occurred|link|ok|span|str|System|problem|country|style|Agent|cpufreq|from_string|int|nospaces|Keyboard|activate|VideoEncoderInfo|argv|activationinput|Please|rated|kernel|action|Windows|read|json|getText|doModal|User|replace|city|font|showadult|to_string|Duplicate|was|sys|firstpart|def|ares_rate_url|KernelVersion|translatePath|close|error|there|Sorry|Inserted|with|CpuFrequency|autopassword|isinresponse|accepted|http|result|weight|registration|Thanks|else|Already|privateinternetaccess|already|isp|MacAddress|open|2008092417|Your|ip|dialog|user|jsonstring|time|enter|while|getsysinfo|activation|awaiting_activation|except|Incorrect|select|rateaddon|xbmcaddon|now|ratebuild|excluding|whatismyipaddress|incorrectpassword|text|userinfo|bold|your|colortag|this|ares_rate_result|datapath|closetag|register|raterepo|find|gpu|stars|addonid|stripcolortags|Mozilla|Network|Firefox|opentag|Country|setHiddenInput|activationcode|return|Busy|getAddonInfo|search|dump|14px|as|td|size|An|many|device|uk|Gecko|Registered|decoration|registered|group|check|Activation|co|username|resources|activated|emailsent|try|rateresult|translate|How|You|Internet|be|settings|path|from|City|CAPITALS|load|Provider|True|req|n|bypassed|deviceid|S|through|address|r|Address|strings|minutes|Service|profile|command|global|random|script|base64|th|unique|os|nojson|urllib|com|wizard|shutil|couple|forget|re|folder|whats|dumps|https|pages|enjoy|COLOR|Addon|build|sent|come|like|spam|en|to|pass|26px|Hope|NT|repo|GB|glob|wish|is|join|rv|take|my|none|must|may|too|w|www|don|php|registerresult|you|ALL|xbmcgui|ISP|for|It|s|of|U|i|in|Dialog|an|code|IP|t".split("|")))