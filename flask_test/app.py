{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled5.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K7Bq6GnScMSU",
        "outputId": "d38ea244-cd38-45b7-e52f-862f7c7f949e"
      },
      "source": [
        "!pip install flask-ngrok"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Collecting flask-ngrok\n",
            "  Downloading https://files.pythonhosted.org/packages/af/6c/f54cb686ad1129e27d125d182f90f52b32f284e6c8df58c1bae54fa1adbc/flask_ngrok-0.0.25-py3-none-any.whl\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.6/dist-packages (from flask-ngrok) (2.23.0)\n",
            "Requirement already satisfied: Flask>=0.8 in /usr/local/lib/python3.6/dist-packages (from flask-ngrok) (1.1.2)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.6/dist-packages (from requests->flask-ngrok) (2020.12.5)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.6/dist-packages (from requests->flask-ngrok) (1.24.3)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.6/dist-packages (from requests->flask-ngrok) (3.0.4)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.6/dist-packages (from requests->flask-ngrok) (2.10)\n",
            "Requirement already satisfied: itsdangerous>=0.24 in /usr/local/lib/python3.6/dist-packages (from Flask>=0.8->flask-ngrok) (1.1.0)\n",
            "Requirement already satisfied: Jinja2>=2.10.1 in /usr/local/lib/python3.6/dist-packages (from Flask>=0.8->flask-ngrok) (2.11.2)\n",
            "Requirement already satisfied: click>=5.1 in /usr/local/lib/python3.6/dist-packages (from Flask>=0.8->flask-ngrok) (7.1.2)\n",
            "Requirement already satisfied: Werkzeug>=0.15 in /usr/local/lib/python3.6/dist-packages (from Flask>=0.8->flask-ngrok) (1.0.1)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.6/dist-packages (from Jinja2>=2.10.1->Flask>=0.8->flask-ngrok) (1.1.1)\n",
            "Installing collected packages: flask-ngrok\n",
            "Successfully installed flask-ngrok-0.0.25\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OeZf9a9VbwCH",
        "outputId": "3fa496e5-91af-49f6-dcbc-b16907ee9568"
      },
      "source": [
        "import os\n",
        "from flask import Flask, render_template, request, redirect, url_for, abort\n",
        "from flask_ngrok import run_with_ngrok\n",
        "from werkzeug.utils import secure_filename\n",
        "\n",
        "app = Flask(__name__)\n",
        "run_with_ngrok(app)\n",
        "app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024\n",
        "app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.pdf', '.gif']\n",
        "app.config['UPLOAD_PATH'] = './uploads'\n",
        "\n",
        "\n",
        "\n",
        "@app.route('/', methods=['POST'])\n",
        "def upload_files():\n",
        "    uploaded_file = request.files['file']\n",
        "\n",
        "    filename = secure_filename(uploaded_file.filename)\n",
        "    print(filename)\n",
        "    if filename != '':\n",
        "        file_ext = os.path.splitext(filename)[1]\n",
        "        if file_ext not in app.config['UPLOAD_EXTENSIONS']:\n",
        "            abort(400)\n",
        "        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))\n",
        "    return \"file uploaded\"\n",
        "\n",
        "app.run()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            " * Serving Flask app \"__main__\" (lazy loading)\n",
            " * Environment: production\n",
            "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
            "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
            " * Debug mode: off\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            " * Running on http://f7fe070e5962.ngrok.io\n",
            " * Traffic stats available on http://127.0.0.1:4040\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "stream",
          "text": [
            "127.0.0.1 - - [24/Jan/2021 17:35:12] \"\u001b[31m\u001b[1mGET / HTTP/1.1\u001b[0m\" 405 -\n",
            "127.0.0.1 - - [24/Jan/2021 17:35:14] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n",
            "127.0.0.1 - - [24/Jan/2021 17:35:29] \"\u001b[31m\u001b[1mPOST / HTTP/1.1\u001b[0m\" 400 -\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6o2G6c8EcJcL"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}