# Chat Project



This is a group chat application that allows users to send messages to a common room. It also enables interaction with a number identifier ranging from 0 to 9, with the results sent to the common chat.

After logging in, you can enter the name of the common room, as well as change your profile picture.

To build the image, use the following command:

```cmd
docker build -t elchat_image .
```

To verify that TensorFlow is installed correctly, run:

```cmd
docker run -it --rm elchat_image bash
```

To start the service, execute:

```cmd

docker run -it --rm -p 8000:8000 elchat_image
```

Access the chat application at:link

http://localhost:8000
