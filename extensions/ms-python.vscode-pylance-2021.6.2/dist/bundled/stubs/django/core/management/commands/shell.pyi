from django.core.management import BaseCommand as BaseCommand, CommandError as CommandError
from django.utils.datastructures import OrderedSet as OrderedSet
from typing import Any, List

class Command(BaseCommand):
    shells: List[str] = ...
    def ipython(self, options: Any) -> None: ...
    def bpython(self, options: Any) -> None: ...
    def python(self, options: Any) -> None: ...
