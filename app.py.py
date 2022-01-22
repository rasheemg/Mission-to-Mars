#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping


# In[ ]:


app = Flask(__name__)


# In[ ]:


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# In[ ]:




