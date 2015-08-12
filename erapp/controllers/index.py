#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, Response, abort

index = Blueprint('index', __name__)

@index.route('/')
def main():
    return 'index page'
