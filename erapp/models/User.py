#!/usr/bin/ python
# -*- coding: utf-8 -*-

import re, os
from Base import Base
from bcrypt import hashpw, gensalt
from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean
from datetime import datetime
from flask.ext.login import UserMixin

__roles__ = ('patient', 'admin', 'operator')

class User(Base, UserMixin):

    __tablename__ = 'users'

    id                  = Column(Integer, primary_key=True)
    username            = Column(String(50), unique=True, nullable=False)
    password            = Column(String(60))
    first_name          = Column(String(50))
    last_name           = Column(String(50))
    phone_number        = Column(String(15))
    dob                 = Column(String(10))
    ssn                 = Column(String(9))
    address             = Column(String(95))
    role                = Column(Enum(*__roles__), default='patient', nullable=False)    
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)
    validation_token    = Column(String(64))
    last_login          = Column(DateTime)

    def __init__(self, username, password=None, first_name=None, last_name=None, 
                 phone_number=None, dob=None, ssn=None, address=None, role='patient',
                 last_login=None):
        timestamp = datetime.now()
        self.username           = username
        self.password           = (self.pass_hash(password)) if password else None
        self.first_name         = first_name
        self.last_name          = last_name
        self.phone_number       = self.parse_phone(phone_number)
        self.dob                = dob
        self.ssn                = ssn
        self.address            = address
        self.role               = role
        self.created_at         = timestamp
        self.updated_at         = timestamp
        self.validation_token   = os.urandom(32).encode('hex')
        self.last_login         = last_login

    @staticmethod
    def pass_hash(password):
        return hashpw(password.encode('utf-8'), gensalt())

    @staticmethod
    def parse_phone(phone_number):
        if phone_number:
            return re.compile(r'[^\d]+').sub('', phone_number)
        else:
            return None

    def valid_password(self, attempt):
        return (self.password 
            and hashpw(attempt.encode('utf-8'), self.password.encode('utf-8')) == self.password)

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.username)