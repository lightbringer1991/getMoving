# coding: utf-8
from django.db import models
from django.conf import settings
from jsonfield import JSONField
import requests
from datetime import datetime, date, time
import sys, getopt
import csv
import json

from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name

class Tile(models.Model):
    title = models.CharField(max_length=24)
    category = models.ForeignKey(Category, default=1, on_delete=models.SET_DEFAULT)
    content_template = models.CharField(max_length=60)

    def __str__(self):
        return self.title

    def get_weather(self):
        r = requests.get('http://www.bom.gov.au/fwo/IDV60801/IDV60801.94852.json')
        r.headers['content-type']
        jsonout = r.json()
        f = jsonout['observations']['data'][0]
        string = str(f['name']) + ' is currently ' + str(f['air_temp'])
        string = string.decode('utf-8') + u'°'
        return string

    def get_temp(self):
        r = requests.get('http://www.bom.gov.au/fwo/IDV60801/IDV60801.94852.json')
        r.headers['content-type']
        jsonout = r.json()
        f = jsonout['observations']['data'][0]
        string = str(f['air_temp'])
        string = string.decode('utf-8') + u'°'
        return string

    def get_date(self):
        now = timezone.now().date()
        year = now.year
        month = now.month
        if month < 10 :
           month=str("0")+str(month)
        day = now.day
        if day < 10 :
           day = str("0")+str(day)
        return str(year)+str(month)+str(day)

    def data_convertor(self):
        json_file = '/Users/mayur/Desktop/file2.json'
        csv_file = '/Users/mayur/Desktop/PH1.csv'
        csv_rows = []
        csvfile = open(csv_file, 'r')
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        f = open(json_file, "w")
        if format == "pretty":
           f.write(json.dumps(csv_rows, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
        else:
            f.write(json.dumps(csv_rows))

        return str("worked")

class Tile_Data(models.Model):
    name = models.CharField(max_length=24, default="Tile")
    time = models.DateTimeField('refresh time')
    data = JSONField(default={})
    url = models.CharField(max_length=260,default="gov.data.au")

    def __str__(self):
        return self.name

    def filter_by_date(self):
        today = timezone.now().date()
        entries = []

        for h in self.data:
            try:
                hdate = datetime.strptime(h['Date'], '%Y%m%d').date()
            except:
                continue

            applicable_to = h.get('Applicable_To')

            if applicable_to and (not 'VIC' in applicable_to and not 'NAT' in applicable_to):
                continue

            if hdate >= today:
                h['Date'] = hdate
                h['DaysAway'] = (hdate - today).days
                entries.append(h)

        return entries

    def next(self):
        entries = self.filter_by_date()
        if entries:
            return entries[0]
        else:
            return None

class Tile_tileData(models.Model):
    tileId = models.ForeignKey('Tile')
    dataId = models.ForeignKey('Tile_Data')



"""
    Converts CSV to JSON  - Workes yeh
"""



"""
    today = timezone.now().date()
    today = datetime.datetime.now()


    def get_content(content_path):

        # Open content file and return as a string
        try:
            content_file = open(content_path, 'r')
            self.content = content_file.read()
            # return self.content
            return "got file"

        except IOError, exeObj:
            print str(exeObj)
            return "test"

    # tile_content = "testContent"
    tile_content = get_content(content_path)
"""
