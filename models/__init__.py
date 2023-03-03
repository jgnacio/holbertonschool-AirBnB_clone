# -*- coding: utf-8 -*-
"""Initalizes the main models package."""

from .engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
