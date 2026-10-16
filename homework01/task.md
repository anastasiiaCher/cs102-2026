Эта первая лабораторная работа, которая посвящена базовым конструкциям языка Python. Также в этой работе описан общий подход к выполнению заданий.

Шаблоны периодически обновляются и дополняются, поэтому следите за тем, чтобы вы сдавали работу по максимально новым шаблонам. Обязательно проверяйте, что у вас загружены все тесты.


💡 При выполнении работ используйте переменные, которые уже введены в шаблоне. Не удаляйте из шаблона уже написанный код. Единственное, что удалить можно – это строчки `#PUT YOUR CODE HERE` и команду `pass`, когда функции начинают возвращать значения.


## Прежде чем приступить к выполнению работы

Перед тем как начать выполнять задания не забудьте перейти в рабочую директорию и активировать ваше виртуальное окружение:

```python
$ gocs102 && cd homework01
$ workon cs102
```

При выполнении работ мы будем придерживаться простого подхода к ветвлению под названием GitHub flow (есть и другие подходы, например, gitflow). Приступая к новой практической работе создавайте ветку с именем этой работы:

```python
(cs102) $ git checkout -b homework01 master
Switched to a new branch 'homework01'
```

Чтобы отобразить список локальных веток можно воспользоваться командой `git branch`:

```python
(cs102) $ git branch
* homework01
  master
```

Символ `*` указывает на какой ветке вы находитесь. Для переключения между ветками используйте команду `git checkout имя_ветки`.

## Шифр Цезаря

[Шифр Цезаря](https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%A6%D0%B5%D0%B7%D0%B0%D1%80%D1%8F) является одним из самых простых методов шифрования. Для кодирования сообщения все буквы алфавита сдвигают на три символа вперед:

`A -> D, B -> E, C -> F, и так далее`

Сдвиг трёх последних букв алфавита:

`X -> A, Y -> B, Z -> C`

Используя шифр Цезаря, слово `PYTHON` будет закодировано следующим образом:

```python
PYTHON
||||||
SBWKRQ
```

Вам необходимо написать тело для следующих двух функций в файле `caesar.py`:

```python
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    return plaintext
```

Обратите внимание, что вторым аргументом функции является сдвиг (`shift`), например, при сдвиге равном нулю сообщение останется без изменений (`A -> A, B -> B, ...`).

<aside>
💡 Воспользуйтесь встроенными функциями `ord()` и `chr()`. Функция `ord()` позволяет получить код указанного символа, а `chr()` работает наоборот - возвращает символ по его коду.

</aside>

**Info**

> О кодировках можно почитать [тут](http://kunststube.net/encoding/).
> 

В результате переменные `ciphertext` и `plaintext` должны содержать зашифрованное и расшифрованное сообщения соответственно.

Проверить работу функций можно с помощью примеров, приведенных в [доктестах](https://docs.python.org/3.5/library/doctest.html) (текст внутри функции, который заключен в тройные кавычки и похож на работу с интерпретатором в интерактивном режиме). Запустить доктесты можно с помощью следующей команды (при условии, что файл с программой называется `caesar.py`):

```python
(cs102) $ python -m doctest -v caesar.py
```

Доктесты обычно играют роль примеров и не используются в качестве полноценного фреймворка для автоматического тестирования. Поэтому мы будем использовать стандартную библиотеку [unittest](https://docs.python.org/3/library/unittest.html) для тестирования наших приложений (наиболее популярной альтернативой является [pytest](https://docs.pytest.org/en/stable/)). Для запуска тестов можно воспользоваться следующей командой:

```python
(cs102) $ python -m unittest -v tests.test_caesar
```

или для запуска всех тестов:

```python
(cs102) $ python -m unittest discover
```

Также обратите свое внимание на официальное руководство по стилю pep8.

Если вы добились успешного прохождения тестов, не забудьте сделать коммит, который зафиксирует ваши изменения, например:

```python
(cs102) $ git add homework01/caesar.py
(cs102) $ git commit -m "Реализована функция encrypt_caesar()"
```

и аналогично:

```python
(cs102) $ git add homework01/caesar.py
(cs102) $ git commit -m "Реализована функция decrypt_caesar()"
```

**Note**

> Вы можете воспользоваться приложением [Source Tree](https://www.sourcetreeapp.com/) для наглядного отслеживания вносимых изменений.
> 

Также не забывайте периодически отправлять ваши изменения на сервер:

```python
(cs102) $ git push origin homework01
```

## Шифр Виженера

[Шифр Виженера](https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%92%D0%B8%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B0) очень похож на шифр Цезаря, за тем исключением, что каждый символ сообщения сдвигается на определяемое ключом значение. Ключ - это слово, каждый символ которого указывает на сколько позиций должен быть сдвинут соответствующий символ в шифруемом сообщении. Так, `A` означает сдвиг на `0` символов, `B` на `1` и т.д.

Если длина ключа меньше длины слова, подлежащего шифрованию, то ключ повторяется необходимое число раз, например:

```python
Простой текст: ATTACKATDAWN
Ключ: LEMONLEMONLE
Зашифрованный текст: LXFOPVEFRNHR
```

Ваша задача написать тело для следующих двух функций в файле `vigenere.py` так, чтобы переменные `ciphertext` и `plaintext` содержали зашифрованное и расшифрованное сообщения соответственно:

```python
def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    return plaintext
```

**Note**

> Обратите внимание, что символы `A` и `a` в ключе не оказывают никакого влияния на шифруемое сообщение. Если же в качестве ключа мы будем использовать `C` или `c`, то получим шифр Цезаря.
> 

По окончании работы над каждой функцией не забудьте запустить тесты и сделать соответствующие коммиты, как в примере с шифром Цезаря.

## RSA шифрование

Одним из современных методов шифрования является алгоритм шифрования RSA, названный так по первым буквам фамилий его авторов (Rivest, Shamir и Adleman).

Мы не будем вдаваться в [подробности работы](https://www.youtube.com/watch?v=wXB-V_Keiu8) этого алгоритма, но [следующего объяснения](https://www.quora.com/How-do-you-explain-how-an-RSA-public-key-works-to-a-child) должно быть достаточно для понимания принципов шифрования с открытым ключом:

**Quote**

> Show your kid a padlock. This is a kind of lock that locks when you click it (i.e it doesn't require a key) but requires the key to open the lock.
So, I can send these padlocks to all my friends who want to communicate with me. I will send them only the lock but will keep the key with me.
My friends can write me messages, put it in a box, lock it with my padlock (by clicking it) and send it to me, even over high risk networks. If the box is intercepted, it's contents will not be compromised since I still have the key with me.
When the box reaches me, I can open my padlock with my key and read the contents. This way, I can send padlocks (public keys) to people outside which they can use to lock boxes (encrypt messages) without being in danger of the contents being compromised as the padlock key (the private key) is always with me and never exchanged over the network.
> 

Следует понимать, что здесь мы будем реализовывать общие принципы алгоритма, а не полноценный RSA. Потому работу алгоритма разобьем на три шага:

1. Генерация ключей
2. Шифрование
3. Расшифровка

От вас в этом задании требуется выполнить только шаг генерации ключей, остальные два шага уже представлены в шаблоне работы.

На этапе генерации создаётся два ключа: открытый (public key, с помощью которого кто угодно может зашифровать сообщение и отправить его нам) и закрытый (private key, с помощью которого мы будем расшифровать полученные сообщения). Для генерации пары ключей необходимо выбрать два [простых числа](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE) `p` и `q`. Мы предоставим пользователю возможность выбирать эти числа. От вас требуется написать тело функции `is_prime(n)`, которая проверяет число на простоту:

```python
def is_prime(n: int) -> bool:
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    # PUT YOUR CODE HERE
    pass
```

Если вы закончили работу над функцией `is_prime(n)`, то запустите тесты и сделайте коммит:

```python
(cs102) $ git commit -am "Реализована функция is_prime(n)"
```

**Info**

> Для фиксации изменений мы использовали команду `git commit -am`, которая является аналогом последовательности команд `git add .` и `git commit -m`.
> 

После того как были выбраны два простых числа требуется найти их произведение `n = p * q`:

```python
def generate_keypair(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    # n = pq
    # PUT YOUR CODE HERE

    # phi = (p-1)(q-1)
    # PUT YOUR CODE HERE

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))
```

Затем вычисляется функция Эйлера по формуле:

$$
ϕ=(p−1)(q−1)
$$

Далее выбирается число `e`, отвечающее следующим критериям:

- `e` — простое;
- `e < phi`;
- `e` [взаимно простое](https://ru.wikipedia.org/wiki/%D0%92%D0%B7%D0%B0%D0%B8%D0%BC%D0%BD%D0%BE_%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%8B%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%B0) с `phi`.

Определить, являются ли числа взаимно простыми можно с помощью алгоритма Евклида. Для этого необходимо вычислить наибольший общий делитель (НОД) и проверить равен ли он единице. На этом этапе вашей задачей является реализация данного алгоритма:

```python
def gcd(a: int, b: int) -> int:
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    # PUT YOUR CODE HERE
    pass
```

Не забудьте зафиксировать реализацию функции `gcd(a, b)`:

```python
(cs102) $ git commit -m "Реализована функция поиска НОД"
```

Заключительным этапом на шаге генерации ключей является вычисление `d` такого что `d * e mod phi = 1`. Для его вычисления используется расширенный (обобщенный) алгоритм Евклида (см. стр. 23 [этого учебного пособия](http://kpfu.ru/docs/F366166681/mzi.pdf) с подробными объяснениями).

```python
def multiplicative_inverse(e: int, phi: int) -> int:
    """
    >>> multiplicative_inverse(7, 40)
    23
    """
    # PUT YOUR CODE HERE
    pass
```

Таким образом, полученные пары `(e,n)` и `(d,n)` являются открытым и закрытым ключами соответственно.

Снова запустите тесты и зафиксируйте изменения:

```python
(cs102) git commit -am "Реализованы функции multiplicative_inverse() и generate_keypair()"
```

## После выполнения всех заданий

В процессе выполнения заданий не забудьте проверить, что у вас проходят все тесты. А когда убедитесь, что все уже хорошо, отправьте изменения на сервер:

```python
(cs102) $ git push origin homework01
```

Затем создайте пул-реквест, дождитесь проверки в `Github Actions` и защитите свою работу.
