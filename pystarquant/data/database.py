#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from enum import Enum
from abc import ABC, abstractmethod
from typing import Optional, Sequence, TYPE_CHECKING


class Driver(Enum):
    SQLITE = "sqlite"
    MYSQL = "mysql"
    POSTGRESQL = "postgresql"
    MONGODB = "mongodb"


class BaseDatabaseManager(ABC):

    @abstractmethod
    def load_bar_data(
        self,
        symbol: str,
        interval: "Interval",
        start: datetime,
        end: datetime
    ) -> Sequence["BarData"]:
        pass

    @abstractmethod
    def load_tick_data(
        self,
        symbol: str,
        start: datetime,
        end: datetime
    ) -> Sequence["TickData"]:
        pass

    @abstractmethod
    def save_bar_data(
        self,
        datas: Sequence["BarData"],
    ):
        pass

    @abstractmethod
    def save_tick_data(
        self,
        datas: Sequence["TickData"],
    ):
        pass

    @abstractmethod
    def get_newest_bar_data(
        self,
        symbol: str,
        interval: "Interval"
    ) -> Optional["BarData"]:
        """
        If there is data in database, return the one with greatest datetime(newest one)
        otherwise, return None
        """
        pass

    @abstractmethod
    def get_newest_tick_data(
        self,
        symbol: str,
    ) -> Optional["TickData"]:
        """
        If there is data in database, return the one with greatest datetime(newest one)
        otherwise, return None
        """
        pass

    @abstractmethod
    def clean(self, symbol: str):
        """
        delete all records for a symbol
        """
        pass
