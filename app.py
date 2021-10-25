{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "80f3bc11",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0c6b3614",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "932254ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/')\n",
    "def hello_world():\n",
    "    return 'Hello world'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f54b1b1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
