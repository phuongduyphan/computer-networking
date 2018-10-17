# Installation and setup
Install PIL packet python from pip:
```bash
$ pip install image
```
Run server scripts first before running any client scripts
Example of sending image through TCP: 
* Server:
    ```bash
    $ python TCPServerImage.py
    The server is ready to receive
    ```
* Client:
    ```bash
    $ python TCPClientImage1.py
    From Server: image received
    $ python TCPClientImage2.py
    From Server: image received
    ```
