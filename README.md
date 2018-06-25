# ConfReader

Configuration files are files used to configure the parameters and initial settings used in scripts without hardcoding them.

To write a configuration file, the rules are the following :
- It must be "key" = "value" in the file, one per line only
```
login = mylogin
password = mypassword
```
- At the beginning of the file, you can put an Environment value "ENV" that enables you to have a different sets of parameters.
For example, the following file will return "mytest" for the key "login". You can also setup different values in the different environment.
You must only remember that it will ONLY take the values between [test] and the next [] or the end.  

```
ENV = test

[test]

login = mytest

[prod]

login = myprod
```
- The usage is the following:
```python
from Classes_SG.conf.ConfReader import *
config = ConfReader("my_config_file.conf", path=path_conf)
login = config.get_value("login")
```