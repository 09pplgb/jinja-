import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def hello_world():

 orang = {'nama': 'albardani', 'umur':'21thn'}

 komentar = [

  {
   'penulis': {'nama': 'Khalid'},
   'ucapan': 'hai albardani, artikel yang keren'
  },
  {
   'penulis': {'nama': 'Ariqa'},
   'ucapan': 'artikel ini sangat bermanfaat'
  }
 ]
 return render_template('index.html', title='Beranda', orang=orang, komentar=komentar)
